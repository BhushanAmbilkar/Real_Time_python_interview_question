import time

from selenium import webdriver

driver=webdriver.Chrome()

# scroll down page by pixel
driver.get("https://en.wikipedia.org/wiki/Software_testing")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,2000)","")
time.sleep(2)


value=driver.execute_script("return")
