from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# key = b'\x10/\xce\xd1\x87BP\x81\x9b\x0e(\xa5\x99g\xd4\x8f'
key = get_random_bytes(16)
# key = b"This is the keyy"

def encrypt(msg):
    
    ecip = AES.new(key,AES.MODE_EAX)
    nonce = ecip.nonce
    ct = ecip.encrypt(msg)
    return key,nonce,ct 


def decrypt(key,obj,ct):
    
    dcip = AES.new(key, AES.MODE_EAX,obj)
    cd = dcip.decrypt(ct).decode()
    return cd
