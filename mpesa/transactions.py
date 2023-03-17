import requests

import datetime
import base64

from django.conf import settings
from .transaction_exceptions import ExpressExceptions

def mpesa_express(phone_no: int, amount: int, description="payment"):
    """Return a json object
    args:
      :phone_no:int
      :amount: int
      :description: string

    make a request to mpesa express api
    """

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    password = str(settings.BUSINESS_SHORT_CODE) + settings.PASS_KEY + timestamp
    byte_password = password.encode()
    new_password = base64.b64encode(byte_password)
    new_password = new_password.decode()
    payload = {
        "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
        "Password": new_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_no,
        "PartyB": settings.BUSINESS_SHORT_CODE,
        "PhoneNumber": phone_no,
        "CallBackURL": "https://squid-app-9xncj.ondigitalocean.app/mpesa/stk-callback/",
        "AccountReference": settings.ACCOUNT_REFERENCE[:12],
        "TransactionDesc": description[:13],
    }
    header = {"Authorization": f"Bearer {settings.ACCESS_TOKEN}","Content-Type": "application/json"}
    response = requests.post(
        "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        headers=header,
        json= payload
    )
    print(response.json())
    
    if 'errorCode' in  response.json():
        raise ExpressExceptions("Invalid access token, use a valid access token")
    else:
        print(response.json()["ResponseDescription"])
        return "success"
    # try:
    #     if 'errorCode' in  response.json():
    #         raise ExpressExceptions("Tranasaction failed, invalid access tokens")
    # except ExpressExceptions:
    #     pass
    # finally:
    #     return None


# mpesa_express(254757164343, 1)

def customer_to_business(type:str,phone:int,amount:int,account_number=None):
    if account_number == None:
        account_number = ""
    
    headers = {
  'Content-Type': 'application/json',
  'Authorization': f"Bearer {settings.ACCESS_TOKEN}"}

    payload = {
    "ShortCode": 600426,#change to use the settings in production
    "CommandID": type,
    "amount": amount,
    "MSISDN": phone,
    "BillRefNumber": account_number,}

    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers = headers, json = payload)
    print(response.text.encode('utf8'))
    if response.json()["ResponseCode"] == str(0):
        return "sucessful"
    else:
        return "failed"

    
