from selenium import webdriver
from os import getcwd, environ,path
from selenium.webdriver.common.by import By 


ass_path = path.dirname(path.dirname(__file__))

driver_bin = f'{ass_path}/geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_bin)
driver.get("https://www.jiosaavn.com/song/raawadi/QCAGQjNiYHw")

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/main/div[2]/figure/figcaption/div/p[1]/a').click()
print("okkkkkk")
