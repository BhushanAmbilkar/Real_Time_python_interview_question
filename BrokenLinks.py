import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By


capabilities = {
    "build": "[Python] Finding broken links on a webpage using Selenium",
    "name": "[Python] Finding broken links on a webpage using Selenium",
    "platform": "Windows 10",
    "browserName": "Chrome",
    "version": "85.0"
}

user_name = "user-name"
app_key = "access-key"
broken_links = 0
valid_links = 0

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
# driver=webdriver.Chrome(options=options)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
remote_url = "http://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)
driver.maximize_window()
driver.get('https://www.lambdatest.com/blog/')

# links = driver.find_elements_by_css_selector("a")
links = driver.find_elements(By.CSS_SELECTOR, "a")

for link in links:
    try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
        if request.status_code == 404:
            broken_links = (broken_links + 1)
        else:
            valid_links = (valid_links + 1)
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    else:
        print("Encountered Some other execption")

print("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(
    valid_links) + " valid links")

# First, we'll use selenium to get the page and grab all the links and images from the page:

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/")
links = driver.find_elements(By.CSS_SELECTOR, "a")
images = driver.find_elements(By.CSS_SELECTOR, "img")

# Now we'll hit each of the URLS using the head request from the Python Requests library


for link in links:
    r = requests.head(link.get_attribute('href'))
    print(r.status_code == 200)
# Do the same with the images
for image in images:
    r = requests.head(image.get_attribute('src'))
    print(r.status_code == 200)

# bad links
for link in links:
    r = requests.head(link.get_attribute('href'))
    if r.status_code != 200:
        print(link.get_attribute('href'))
