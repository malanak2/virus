import os
import socket
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 6942
BUFFER_SIZE = 1024
basedir = os.path.abspath(os.path.dirname(__file__))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

if os.path.exists(basedir + 'data.json'):
    f = open('data.json')
    data = json.loads(f)
    s.send(data['id'])
    f.close()
    s.close()
else:
    s.send(b'newU')
    recData = s.recv(BUFFER_SIZE)
    if recData == b'sendData':
        data = os.getlogin()
        s.send(data.encode('utf-32'))
    recId = s.recv(BUFFER_SIZE)
    list = {'id': recId}
    print(list)
    s.close()
""" while 1:
    data = s.recv(BUFFER_SIZE)
    if not data: break
    print ('received data: ', data) """

#
#import os
#import requests
#from cryptography.fernet import Fernet
#from dotenv import load_dotenv
#from unidecode import unidecode
a = 'b'
""" load_dotenv() # Loads dotenv
TARGET_URL = os.getenv('ROUTE') # Gets url from env file
KEY = os.getenv('KEY') # Gets key from .env
fernet = Fernet(KEY) # Inits fenet
data = os.getlogin() + '?default notes?1' # Preset for note
encMsg = fernet.encrypt(data.encode('utf-32')) # Encrypts message
S = requests.session() # Idk
R = S.post(TARGET_URL, data=encMsg) # Sends message
if R.ok:
    print("Text: ", str(R.text))
    print("Content", R.content)
else:
    R.raise_for_status() # Just raises err for now.... """