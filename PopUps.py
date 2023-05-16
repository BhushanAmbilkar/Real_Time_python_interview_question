from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#  Authentication Pop Up 
driver.get("https://Username:Password@URL Address")
# verify the title
if (driver.title == "Authentication Successful"):
    print("Test Passed")
else:
    print("Test failed")
