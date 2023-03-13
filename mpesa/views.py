import json
from datetime import datetime

from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import JsonResponse

from .models import MpesaExpress, ApiResponses,LipaNaMpesa
from .forms import ExpressNumberForm
from .transactions import mpesa_express
from .tasks import get_express_payement

# Create your views here.


class ExpressNumber(View):
    def setup(self, request, *args, **kwargs):
        self.form = ExpressNumberForm()
        return super().setup(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = ExpressNumberForm()
        return render(self.request,"express.html",context={"form":form})
    
    def post(self, request, *args, **kwargs):
        form = ExpressNumberForm(request.POST)
        if form.is_valid():
            phone_num = form.cleaned_data["phone"]
            amount = form.cleaned_data["amount"]
            status =  mpesa_express(phone_num,1)
            if status == "success":
                result = get_express_payement.delay(phone_num,amount)
                result = result.get()
                result.is_confirmed = True
                result.save()
                return render(self.request,"express_success.html")
        else:
            # redirect(reverse("phone"))
            return render(self.request,"express.html",{"form":self.form})

class MpesaExpressCallBack(View):
    """
    safaricom sandbox callback,
    save api results in the database

    """
    def post(self,request,*args, **kwargs):
        print(json.loads(request.body))
        stk_results = json.loads(request.body)
        ApiResponses.objects.create(stk_results)
        if not stk_results["Body"]["stkCallback"]["ResultCode"] == 0:
            pass
        else:
            MpesaExpress.objects.create(
                        amount = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"],
                        receipt_no = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"],
                        transaction_date = datetime.strptime(str(stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][2]["Value"]),"%Y%m%d%H%M%S"),
                        phone = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
                    )
        print(MpesaExpress.objects.last())
        return HttpResponse("")
        
class ValidationView(View):
    """C2B validation view, return accecepted"""
    def post(self,request,*args,**kwargs):
        print(json.loads(request.body))
        return JsonResponse({"ResultCode": 0,"ResultDesc": "Accepted"})

class ConfirmationView(View):
    """C2B validation view, return nothing"""
    def post(self,request, *args, **kwarg):
        resp = json.loads(request.body)
        ApiResponses.objects.create(resp)
        LipaNaMpesa.objects.create(
            type = resp["TransactionType"],
            receipt_no = resp["TransID"],
            transaction_date = datetime.strptime(resp["TransTime"],"%Y%m%d%H%M%S"),
            amount = resp["TransAmount"],
            ref_no = resp["BillRefNumber"],
            invoice_no = resp["InvoiceNumber"],
            acc_balance = resp["OrgAccountBalance"],
            third_party = resp["ThirdPartyTransID"],
            phone = resp["MSISDN"],
            first_name = resp["FirstName"]
        )
        return HttpResponse("")
