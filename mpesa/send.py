
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer cHUhZeX9Y4WXk5L2LCnK7Y1ZMDUv'
}
payload = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwMjIzMDkyNzUz",
    "Timestamp": "20230223092753",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254757164343,
    "PartyB": 174379,
    "PhoneNumber": 254757164343,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
  }
response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
print(response.json())