from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.binary_location = "/usr/bin/chromium"
options.add_argument("--user-data-dir=./sessions/chrome")

driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"),
    options=options
)

driver.get("https://web.whatsapp.com")

time.sleep(15)

print(driver.title)
print(driver.current_url)

driver.save_screenshot("whatsapp.png")

input("Press Enter...")