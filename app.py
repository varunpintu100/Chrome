from selenium import webdriver
from main import Chrome

driver = Chrome.driver()

driver.get("https://www.google.com")

print(driver.page_source)
