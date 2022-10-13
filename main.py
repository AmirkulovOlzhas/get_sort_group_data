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