import os
import time
from datetime import datetime
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  config import argument1, argument2

# Replace YOUR_GROUP_NAME with the name of the group from which you want to download photos and videos
GROUP_NAME = "МИТ-21-3нк2 өзіміз"
saved_contacts = ['Сымбат-ИС4/а']

# Replace YOUR_DOWNLOAD_LOCATION with the path to the directory where you want to save the downloaded photos and videos
DOWNLOAD_LOCATION = r"C:\Users\OFFICE\PycharmProjects\whatsapp-project\stuf\1"

# Create the download directory if it doesn't exist
if not os.path.exists(DOWNLOAD_LOCATION):
    os.makedirs(DOWNLOAD_LOCATION)

# Launch a new Chrome browser
options = webdriver.ChromeOptions();
options.add_argument(argument1);
options.add_argument(argument2)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
input("Press Enter after scanning the QR code")

# Find the chat for the group
group_chat = driver.find_element_by_xpath("//span[@title='{}']".format(GROUP_NAME))

# Click on the chat to open it
group_chat.click()

# Scroll down to load more messages
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for the messages to load
time.sleep(3)

# Find all the media messages (photos and videos)
media_messages = driver.find_elements_by_css_selector('.message-in .media-wrap')

# Download each media file
for media in media_messages:
    # Find the sender's name
    sender = media.find_element_by_css_selector('.message-author').text

    # Check if the sender is a saved contact
    if sender in saved_contacts:
        # Click on the media to open it
        media.click()

        # Wait for the media to load
        time.sleep(3)

        # Find the download button
        download_button = driver.find_element_by_css_selector('.download-button')

        # Click the download button
        download_button.click()

        # Wait for the download to complete
        time.sleep(3)

        # Find the downloaded file
        downloaded_file = driver.find_element_by_css_selector('#app .chat .message-out .media-wrap .media')

        # Get the file name and extension
        file_name, file_ext = os.path.splitext(downloaded_file.text)

        # Construct the new file name
        new_file_name = "{}_{}{}".format(datetime.now().strftime("%Y%m%d%H%M%S"), sender, file_ext)

        # Rename the file
        os.rename(os.path.join(DOWNLOAD_LOCATION, file_name + file_ext), os.path.join(DOWNLOAD_LOCATION, new_file_name))

# Close the browser
driver.quit()