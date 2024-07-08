from cryptography.fernet import Fernet
from uuid import getnode as get_mac


def encode(message:str, key:str):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    print("encrypted string: ", encMessage)
    return encMessage

def decode(encMessage:str, key:str):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(encMessage).decode()
    print("decrypted string: ", decMessage)
    return decMessage


def get_mac_address():
    mac_id = (":".join(f"{b:02x}" for b in get_mac().to_bytes(6)))
    return mac_id