from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Using chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#1 Select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

#2 select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
#Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#Approach 2
# for checkbox in checkboxes:
#     checkbox.click()

#Approach 3
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

# 4
#select last two checkboxes
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()

# 5
#select first two checkboxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

#clearing all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
