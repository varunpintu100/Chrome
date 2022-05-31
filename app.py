from selenium import webdriver
from main import Chrome

# this class is to invoke the chrome from the main file
chrome_1 = Chrome()

#this method is to return the driver from remote 
driver = chrome_1.driver()

#this is used to navigate to the respected url
driver.get("https://varun-resume.herokuapp.com")

print(driver.page_source)