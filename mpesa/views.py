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
            items = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["CallbackMetadata"]["Item"] 
            for i in range(len(items)):
                for item in items:
                    print(item.items())
                    MpesaExpress.objects.create(
                        amount = ["item"][0]["Value"],
                        receipt_no = ["item"][1]["Value"],
                        transaction_date = datetime.strptime(["item"][2]["Value"],"%Y%m%d%H%M%S"),
                        phone = ["item"][3]["Value"]
                    )
        print(MpesaExpress.objects.last())
        print(MpesaExpress.objects.first())
        

