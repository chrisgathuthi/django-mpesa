import datetime
from django.db import models

# Create your models here.'
class MpesaExpress(models.Model):
    amount = models.DecimalField(verbose_name="Amount",max_digits=5,decimal_places=2)
    receipt_no = models.CharField(max_length=10,verbose_name="MpesaReceiptNumber")
    transaction_date = models.DateTimeField(verbose_name="TransactionDate")
    phone = models.PositiveBigIntegerField(verbose_name="PhoneNumber")
    is_confirmed = models.BooleanField(verbose_name="confirmed",default=False)
    timestamp = models.DateTimeField(auto_now=True)

def dict_instance():
    return dict({"name":"hello world"})
class ApiResponses(models.Model):
    responses = models.JSONField(verbose_name="mpesa results",default=dict_instance)

class LipaNaMpesa(models.Model):
    type = models.CharField(verbose_name="transaction type",max_length=10)
    transaction_date = models.DateTimeField(verbose_name="TransactionDate")
    receipt_no = models.CharField(verbose_name="transaction id",max_length=10)
    amount = models.PositiveIntegerField(verbose_name="amount")
    ref_no = models.CharField(verbose_name="reference number",max_length=15,null=True)
    invoice_no = models.CharField(verbose_name="invoice number",max_length=15,null=True)
    acc_balance = models.DecimalField(verbose_name="org account balance",decimal_places=2)
    third_party = models.CharField(verbose_name="third party ID",max_length=10)
    phone = models.PositiveBigIntegerField(verbose_name="phone number")
    first_name = models.CharField(verbose_name="first name",max_length=100)

