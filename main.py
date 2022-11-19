import os
import requests
import json
from cryptography.fernet import Fernet
API_ENDPOINT = 'http://127.0.0.1:5000/addPc'

KEY = 'WQP6UqEHK5EvsKeCI2EsKe4oEWL9rbMKVPbcYk2MdF8='
fernet = Fernet(KEY)
data = os.getlogin() + '?default notes?1'
encMsg = fernet.encrypt(data.encode())
#print(encMsg)
print(json.dumps(data))
S = requests.session()
R = S.post(API_ENDPOINT, data=data)

if R.ok:
    print("Text: ", str(R.text))
    print("Content", R.content)
else:
    R.raise_for_status()