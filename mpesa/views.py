import json
from datetime import datetime

from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .models import MpesaExpress, ApiResponses
from .forms import ExpressNumberForm
from .transactions import mpesa_express

# Create your views here.


class ExpressNumber(View):
    def get(self, request, *args, **kwargs):
        form = ExpressNumberForm()
        return render(self.request,"express.html",context={"form":form})
    
    def post(self, request, *args, **kwargs):
        form = ExpressNumberForm(request.POST)
        if form.is_valid():
            phone_num = form.cleaned_data["phone"]
            print(phone_num)
            # mpesa_express(phone_num,1)
        else:
            reverse("phone")
        return render(self.request,"express_success.html")

class MpesaExpressCallBack(View):
    """

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
        

