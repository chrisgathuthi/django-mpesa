import requests
from django.conf import settings

def enable_validation_urls(shortcode:str,response_type:str,confirmation_url:str,validation_url:str,access_token:str):
    headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_token}'
}
    payload = {
    "ShortCode": shortcode,
    "ResponseType": response_type,
    "ConfirmationURL": confirmation_url,
    "ValidationURL": validation_url,
  }
    response = requests.post( 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, json = payload)
    return response.json()["ResponseDescription"]


