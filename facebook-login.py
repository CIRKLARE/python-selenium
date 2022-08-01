from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox(executable_path="./geckodriver")
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_xpath("//button")
username.send_keys("example@email.com")
password.send_keys("password")
# Step 4) Click Login
submit.click()