from selenium import webdriver
from os import path
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class Saavn:
    def __init__(self, url):

        get_path = path.dirname(path.dirname(__file__))

        driver_bin = f'{get_path}/geckodriver.exe'

        firefox_options = Options()
        firefox_options.add_argument('-headless')

        driver_service = Service(driver_bin)

        driver = webdriver.Firefox(service=driver_service, options=firefox_options)

        driver.get(url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/main/div[2]/figure/figcaption/div/p[1]/a').click()
        
        # logs = driver.get_log('performance')

        # print(logs)

        # for tmp in logs:
        #     print("------> ", tmp)
        print("okkkkkk")
        print(driver.title)

        # Quit the WebDriver
        driver.quit()



import httpx

if __name__ == "__main__":
    # pass
    spark = Saavn("https://www.jiosaavn.com/song/raawadi/QCAGQjNiYHw")

# 