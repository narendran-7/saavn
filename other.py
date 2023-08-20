
"""
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

"""





import requests
from bs4 import BeautifulSoup as soup
import json
req = requests.get("https://www.jiosaavn.com/song/gasolina/RAAjZENnT0s").content

data1 = soup(req, "html.parser")
data = str(data1.find_all("script")[4])[1400:]
# get_json = json.dumps(str(dat))

# print(get_json):
# print("--------", len(json.loads(get_json)))
# sss = json.loads(get_json)




field_name = "encrypted_media_url"
start_index_key = data.index(field_name) + 22
# print(data[start_index: ])



end_data = data[start_index_key : ]


end_index_key = end_data.index('"') 

s_data = data[start_index_key : ]

print(s_data[: end_index_key])
# end_index_key = end_data.index(',')
# print(data[start_index_key: end_index_key + 1])


# print(type(dat))

# for i in sss:
#     print(i)

