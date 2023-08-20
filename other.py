import base64
from pyDes import *

enc_url = "ID2ieOjCrwfgWvL5sXl4B1ImC5QfbsDyrMMaqFa6s6Os6GVgSh4UNoD6dtLqV8sQ99v1DDMDS4bWihCDdZYG0Bw7tS9a8Gtq"

def decrypt_url(url):
    des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",pad=None, padmode=PAD_PKCS5)
    enc_url = base64.b64decode(url.strip())
    dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8').replace("_96.mp4", "_320.mp4")
    print(dec_url)
    return dec_url

decrypt_url(enc_url)