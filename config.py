#list_p = {"alatau": "+774776065", "kasiret": "+7750261982", "nursat": "+77072891276", "pobeda": "+77056935245"}

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
contact = "Бату"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element(By.XPATH, "//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//div[@class="_22Msk copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element(By.XPATH, inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)
driver.quit()