import requests

import datetime
import base64

from django.conf import settings

class ExpressExceptions(Exception):
    pass

def mpesa_express(phone_no: int, amount: int, description="payment"):
    """Return a json object
    args:
      - phone_no:int
      - amount: int
      - descripint: string

    make a request to mpesa express api
    """
    pass_key = settings.PASS_KEY
    short_code = settings.BUSINESS_SHORT_CODE

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    password = str(short_code) + pass_key + timestamp
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
        "PartyB": short_code,
        "PhoneNumber": phone_no,
        "CallBackURL": "https://squid-app-9xncj.ondigitalocean.app/stk-callback/",
        "AccountReference": settings.ACCOUNT_REFERENCE[:12],
        "TransactionDesc": description[:13],
    }
    header = {"Authorization": "Bearer  ATEAa2TnjTvC988NbznxqaLRVIvM","Content-Type": "application/json"}
    response = requests.post(
        "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        headers=header,
        json= payload
    )
    print(response.json())
    
    if 'errorCode' in  response.json():
        return "failed"
    else:
        print(response.json()["ResponseDescription"])
        return "success"
    # return None
    # try:
    #     if 'errorCode' in  response.json():
    #         raise ExpressExceptions("Tranasaction failed, invalid access tokens")
    # except ExpressExceptions:
    #     pass
    # finally:
    #     return None


# mpesa_express(254757164343, 1)
