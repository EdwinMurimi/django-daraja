
import base64

import keys


def generate_password(timestamp):
    # password
    data_to_encode = keys.business_short_code + \
        keys.lipa_na_mpesa_passkey + timestamp
    encoded = base64.b64encode(data_to_encode.encode())
    password = encoded.decode('utf-8')

    return password
