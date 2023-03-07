from celery import shared_task
from mpesa.models import MpesaExpress


@shared_task(name="retreive_transaction")
def get_express_payement(phone:int,amount:int):
    obj = MpesaExpress.objects.filter(phone = phone).filter(amount = amount).filter(is_confirmed = False).exits()
    return obj