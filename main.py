import os
import requests
import json
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from unidecode import unidecode
load_dotenv() # Loads dotenv
TARGET_URL = os.getenv('ROUTE') # Gets url from env file

KEY = os.getenv('KEY') # Gets key from .env
fernet = Fernet(KEY) # Inits fenet
data = os.getlogin() + '?default notes?1' # Preset for note
btrData = unidecode(data) # I dont know just...
encMsg = fernet.encrypt(btrData.encode('utf-8')) # Encrypts message
S = requests.session() # Idk
R = S.post(TARGET_URL, data=encMsg) # Sends message

if R.ok:
    print("Text: ", str(R.text))
    print("Content", R.content)
else:
    R.raise_for_status() # Just raises err for now....