from selenium import webdriver
from main import Chrome


chrome_1 = Chrome
driver = chrome_1.driver()

driver.get("https://www.google.com")

print(driver.page_source)