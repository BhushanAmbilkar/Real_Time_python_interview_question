"""
Consider the following HTML page source.

<html>
<body>
<form id="EmployeeForm">
<input name="employee_name"type="text"/>
<input name="email"type="email"/>
<input name="next"type="submit" value="Login"/>
</form>
</body>
</html>

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager.install()))
driver.get("url")
driver.find_element(By.NAME, "email")

driver.close()
driver.quit()
