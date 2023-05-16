from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("")


# create the object for Action Chains
actions = ActionChains(driver)

#
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
