from requests import get
from bs4 import BeautifulSoup as soup
from base64 import b64decode
from pyDes import des, ECB, PAD_PKCS5

class Saavn:
    def __init__(self, url):
        req = get(url).content

        self.soup_obj = soup(req, "html.parser")
        data = str(self.soup_obj.find_all("script")[4])[1400:]

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
    
    def get_song_info(self):
        song_image_url = self.soup_obj.find_all("img")[0]["src"]

        song_title = self.soup_obj.find_all("h1", {"class":"u-h2 u-margin-bottom-tiny@sm"})[0].text

        s = song_title.index("(") 
        song_name = song_title[:s]
        song_album = song_title[s + 7 :-2]

        created_by_items = self.soup_obj.find_all("p", {"class":"u-color-js-gray u-ellipsis@lg u-margin-bottom@sm u-margin-bottom-tiny@lg"})[0]
        artist = created_by_items.find_all("a")
        art_list = ",".join([i["title"].strip() for i in artist])

        song_company = self.soup_obj.find_all("p", {"class":"u-color-js-gray u-ellipsis@lg u-visible@lg"})[0]
        song_company_name = song_company.find_all("a")[0]["title"]

        #song_lyrics = self.soup_obj.find_all("a", {"screen_name":"song_screen"})

        #print(song_lyrics)

        return {
            "song_name":song_name,
            "song_album":song_album,
            "artist_name":art_list,
            "song_owned":song_company_name,
            "song_img_url":song_image_url,
        }

if __name__ == "__main__":
    spark = Saavn("https://www.jiosaavn.com/song/glimpse-of-harold-das-from-leo/FT0RST5SdVo")
    spark.download_song()
    print(spark.get_song_info())