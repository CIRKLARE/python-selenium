from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get('https://github.com/CIRKLARE/python-selenium/')
print('Title: %s' % browser.title)
#browser.quit()
