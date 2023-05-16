from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("")
driver.find_element(By.XPATH, "//button[@name='submit']").click()

# alert object creation and switching focus to alert
a = driver.switch_to.alert

# accept the alert
a.accept()

# dismiss the alert
a.dismiss()

# send keys text
a.send_keys("text")
