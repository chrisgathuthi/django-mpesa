import json
from datetime import datetime

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .models import MpesaExpress

# Create your views here.

def index(request,*args, **kwargs):
    return HttpResponse("hello world")


@method_decorator(csrf_exempt,name="dispatch")
class MpesaExpressCallBack(View):
    """

    """
    def post(self,request,*args, **kwargs):
        print(json.loads(request.body))
        stk_results = json.loads(request.body)
        if not stk_results["Body"]["stkCallback"]["ResultCode"] == 0:
            raise "Request cancelled by user "+stk_results["Body"]["stkCallback"]["ResultDesc"]
        else:
            MpesaExpress.objects.create(
                        amount = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"],
                        receipt_no = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"],
                        transaction_date = datetime.strptime(str(stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][2]["Value"]),"%Y%m%d%H%M%S"),
                        phone = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
                    )
        print(MpesaExpress.objects.last())
        print(MpesaExpress.objects.first())
        return HttpResponse("success")
        

