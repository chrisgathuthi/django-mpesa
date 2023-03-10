import requests
from django.conf import settings

def enable_validation():
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

    payload = {
    "ShortCode": settings.BUSINESS_SHORT_CODE,
    "ResponseType": settings.RESPONSE_TYPE.capitalize(),
    "ConfirmationURL": settings.CONFIRMATION_URL,
    "ValidationURL": settings.VALIDATION_URL,
  }

    response = requests.post( 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, json = payload)
    return response.json()["ResponseDescription"]


