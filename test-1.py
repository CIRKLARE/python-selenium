from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get('https://dafk.net/what')
print('Title: %s' % browser.title)
#browser.quit()
