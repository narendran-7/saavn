from requests import get
from bs4 import BeautifulSoup as soup
from base64 import b64decode
from pyDes import des, ECB, PAD_PKCS5

class Saavn:
    def __init__(self):
        req = get("https://www.jiosaavn.com/song/hukum-thalaivar-alappara-from-jailer/ACQeWj9ScVI").content

        soup_obj = soup(req, "html.parser")
        data = str(soup_obj.find_all("script")[4])[1400:]

        field_name = "encrypted_media_url"
        start_index_key = data.index(field_name) + 22

        end_data = data[start_index_key : ]
        end_index_key = end_data.index('"') 

        s_data = data[start_index_key : ]
        self.encrypted_url = s_data[: end_index_key]
        
    def decrypt_url(self):
        des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",pad=None, padmode=PAD_PKCS5)
        enc_url = b64decode(self.encrypted_url.strip())
        dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8').replace("_96.mp4", "_320.mp4")
        return dec_url

    def download_song(self):
        get_song = get(self.decrypt_url())
        totalbits = 0
        if get_song.status_code == 200:
            with open("song.mp3","wb+") as f:
                for chunk in get_song.iter_content(chunk_size=1024):
                    if chunk:
                        totalbits += 1024
                        #print("Downloaded",totalbits*1025,"KB...")
                        f.write(chunk)

if __name__ == "__main__":
    spark = Saavn()
    spark.download_song()