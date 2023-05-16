from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import webdriver_manager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Using chrome driver
driver = webdriver.Chrome(service=Service(webdriver_manager().install()))

# Web page url
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

#dropcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
dropcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#select option for the dropdown---1
#dropcountry.select_by_visible_text("India")

#----2
#dropcountry.select_by_value("10")

#---3
#dropcountry.select_by_index(18)  # 18 is index

#select all the options and print them
alloptions=dropcountry.options

print("total number of options",len(alloptions))
# for i in alloptions:
#     print(i.text)

#select option without using built-in method
for i in alloptions:
    if i.text=="India":
        i.click()
        break



"""
Common Error While Working with Dropdowns: Handling ElementNotInteractable Exception
When you’re interacting with dropdowns, make sure:

The element is clickable.
The element is visible.
The element is enabled.
Use the try-except-finally approach in Python.

"""





dropcountry.select_by_value("IND")
print(len(dropcountry.options))
all_country= dropcountry.options
# for i in all_country:
#     print(i.text)

# for opt in dropcountry.options:
#     dropcountry.select_by_visible_text("India")

