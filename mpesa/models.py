from django.db import models

# Create your models here.'
class MpesaExpress(models.Model):
    amount = models.PositiveIntegerField(verbose_name="Amount")
    receipt_no = models.CharField(max_length=10,verbose_name="MpesaReceiptNumber")
    transaction_date = models.DateTimeField(verbose_name="TransactionDate")
    phone = models.PositiveBigIntegerField(verbose_name="PhoneNumber")
