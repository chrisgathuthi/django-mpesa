import requests    
from django.conf import settings
payload = {
    "MerchantName": "TEST SUPERMARKET",
    "RefNo": "Invoice Test",
    "Amount": 1,
    "TrxCode": "BG",
    "CPI": 174379,
}
response = requests.post("https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query",headers={'Authorization': "Bearer RDvVuq1GLdgGBrujhB7GZatVoARb"},json=payload)
print(response.text)



