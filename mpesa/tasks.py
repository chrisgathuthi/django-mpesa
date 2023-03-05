from celery import shared_task
from mpesa.models import MpesaExpress


@shared_task(name="retreive_transaction")
def get_details(phone:int):
    obj = MpesaExpress.objects.filter(phone = phone).filter(is_confirmed = False)
    return obj