from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver = webdriver.Chrome("chromedriver.exe")
webdriver.get("https://web.whatsapp.com")
time.sleep(25)  # For scan the qr code
# Plese make sure that you have done the qr code scan successful.
confirm = int(input("Press 1 to proceed if sucessfully login or press 0 for retry : "))
if confirm == 1:
    print("Continuing...")
elif confirm == 0:
    webdriver.close()
    exit()
else:
    print("Sorry Please Try again")
    webdriver.close()
    exit()
while True:
    chat = webdriver.find_element(By.XPATH, r"/span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
    # In the above line Change the xpath's class name from the current time class name by inspecting span element
    # which containing the number of unread message showing the contact card inside a green circle before opening the chat room.
    chat.click()
    time.sleep(2)
    # For getting message to perform action
    message = webdriver.find_element(By.XPATH, "//span[@class='i0jNr selectable-text copyable-text']")
    # In the above line Change the xpath's class name from the current time class name by inspecting span element
    # which containing received text message of any chat room.
    for i in message:
        try:
            if "ок" in str(i.text):
                # Here you can use you code to preform action according to your need
                print("Perform Your Action")
        except:
            pass
