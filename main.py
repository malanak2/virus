import os
import socket
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 6942
BUFFER_SIZE = 1024
basedir = os.path.abspath(os.path.dirname(__file__))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))
def run():
    if False: # os.path.exists(basedir + 'data.json'):
        f = open('data.json')
        data = json.loads(f)
        s.send(data['id'].encode('utf-32'))
        f.close()
        while False:
            print("...ok")
        s.send(b'closeConn')
        s.close()
    else:
        s.send('newU'.encode('utf-32'))
        recData = s.recv(BUFFER_SIZE)
        if recData.decode('utf-32') == 'sendData':
            data = os.getlogin()
            s.send(data.encode('utf-32'))
        recId = s.recv(BUFFER_SIZE).decode('utf-32')
        list = {'id': recId}
        with open('data.json', 'w') as f:
            json.dump(list, f)
        s.send(b'closeConn')
        s.close()
        #run()
        # Un-comment upper statement after implemented writing to file
    #while 1:
    #data = s.recv(BUFFER_SIZE)
    #if not data: break
    #print ('received data: ', data)

if __name__ == '__main__':
    run()

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

    