from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Using chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://demo.nopcommerce.com/")
driver.maximize_window()

# Click on link
driver.find_element(By.LINK_TEXT, "Digital download").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

# Find number of links in a range
# alllinks=driver.find_elements(By.TAG_NAME,'a')
alllinks = driver.find_elements(By.XPATH, "//a")

print(len(alllinks))

# print all the link names
for link in alllinks:
    print(link.text)

