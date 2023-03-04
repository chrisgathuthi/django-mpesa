import datetime
from django.db import models

# Create your models here.'
class MpesaExpress(models.Model):
    amount = models.DecimalField(verbose_name="Amount",max_digits=5,decimal_places=2)
    receipt_no = models.CharField(max_length=10,verbose_name="MpesaReceiptNumber")
    transaction_date = models.DateTimeField(verbose_name="TransactionDate")
    phone = models.PositiveBigIntegerField(verbose_name="PhoneNumber")
    timestamp = models.DateTimeField(auto_now=True)

def dict_instance():
    return dict({"name":"hello world"})
class ApiResponses(models.Model):
    responses = models.JSONField(verbose_name="mpesa results",default=dict_instance)