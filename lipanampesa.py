import base64
from datetime import datetime

from requests.auth import HTTPBasicAuth
import requests

import keys

# timestamp
unformatted_time = datetime.now()
timestamp = unformatted_time.strftime("%Y%m%d%H%M%S")
# password
data_to_encode = keys.business_short_code + \
    keys.lipa_na_mpesa_passkey + timestamp
encoded = base64.b64encode(data_to_encode.encode())
password = encoded.decode('utf-8')


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

json_response = r.json()

my_access_token = json_response['access_token']


def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://edwinthedjangodev.com/lnm/",
        "AccountReference": "11568",
        "TransactionDesc": "pay school fees"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
