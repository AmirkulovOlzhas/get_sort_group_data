from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import config
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("chromedriver.exe")

options = webdriver.ChromeOptions()

preference = {"download.default_diretory": r"D:\temp\p"}

options.add_experimental_option("prefs", preference)

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://web.whatsapp.com/")

time.sleep(25)

"""
if number in config.py
    driver(xpath)...
    

"""
driver.find_element(By.XPATH,"/html[@class='js no-touch serviceworker adownload cssanimations csstransitions webp exiforientation webp-alpha webp-animation webp-lossless wf-loading']/body[@class='web dark']/div[@id='app']/div[@class='_1ADa8 _3Nsgw app-wrapper-web font-fix os-win']/span[4]/div[@class='o--vV']/ul[@class='_1HnQz']/div/li[@class='_2qR8G _1wMaz _19zgN _18oo2']/div[@class='_2oldI dJxPU']").click()