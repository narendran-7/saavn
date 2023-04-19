from selenium import webdriver
from os import path
from selenium.webdriver.common.by import By 

class Saavn:
    def __init__(self, url):

        get_path = path.dirname(path.dirname(__file__))

        driver_bin = f'{get_path}/geckodriver.exe'

        driver = webdriver.Firefox(executable_path=driver_bin)

        driver.get(url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/main/div[2]/figure/figcaption/div/p[1]/a').click()
        
        logs = driver.get_log("browser")

        for tmp in logs:
            print("------> ", tmp)
        print("okkkkkk")



import httpx

if __name__ == "__main__":
    pass
    #spark = Saavn("https://www.jiosaavn.com/song/raawadi/QCAGQjNiYHw")

# 