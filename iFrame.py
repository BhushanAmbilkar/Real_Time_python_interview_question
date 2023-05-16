
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# web page url
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

# switch to 1st frame
driver.switch_to.frame("packageListFrame")

# click on 1st frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium.opera").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 2nd frame
driver.switch_to.frame("packageFrame")

# click on  2nd frame
driver.find_element(By.LINK_TEXT, "OperaOptions").click()

# back to default web page frame
driver.switch_to.default_content()

# switch to 3rd frame
driver.switch_to.frame("classFrame")

# click on  2nd frame
driver.find_element(By.XPATH, '/html/body/div[1]/ul/li[4]/a').click()
