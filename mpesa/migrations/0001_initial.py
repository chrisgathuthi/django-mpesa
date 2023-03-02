# Generated by Django 4.1.6 on 2023-03-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MpesaExpress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(verbose_name="Amount")),
                (
                    "receipt_no",
                    models.CharField(max_length=10, verbose_name="MpesaReceiptNumber"),
                ),
                (
                    "transaction_date",
                    models.DateTimeField(verbose_name="TransactionDate"),
                ),
                ("phone", models.PositiveBigIntegerField(verbose_name="PhoneNumber")),
            ],
        ),
    ]
