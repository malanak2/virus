import os
import requests
import json
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from unidecode import unidecode
load_dotenv()
TARGET_URL = 'http://127.0.0.1:5000/f92095e6-5d49-44ae-b6aa-a3941414e97d' #gitignore

KEY = os.getenv('KEY')
fernet = Fernet(KEY)
data = os.getlogin() + '?default notes?1'
btrData = unidecode(data)
encMsg = fernet.encrypt(btrData.encode('utf-8'))
S = requests.session()
R = S.post(TARGET_URL, data=encMsg)

if R.ok:
    print("Text: ", str(R.text))
    print("Content", R.content)
else:
    R.raise_for_status()