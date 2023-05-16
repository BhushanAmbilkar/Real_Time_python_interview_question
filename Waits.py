# import classes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions

# create driver object
driver=webdriver.Chrome(service=Service(ChromeDriverManager.install()))

# Get url to open the website
driver.get("url of website")

# wait for 30 sec
wait=WebDriverWait(driver,30)
element=wait.until(expected_conditions.element_to_be_clickable(By.ID,""))

driver.close()

"""
•	title_is
•	title_contains
•	presence_of_element_located
•	visibility_of_element_located
•	visibility_of
•	presence_of_all_elements_located
•	text_to_be_present_in_element
•	text_to_be_present_in_element_value
•	frame_to_be_available_and_switch_to_it
•	invisibility_of_element_located
•	element_to_be_clickable
•	element_to_be_selected
•	element_located_to_be_selected
•	element_selection_state_to_be
•	element_located_selection_state_to_be
•	alert_is_present



"""
