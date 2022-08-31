from selenium import webdriver
from models.Cloudinary import Cloud
import os
from models.imageTable import IMG
from selenium.webdriver.common.keys import Keys

Cloud_upload = Cloud()

class Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")

    def driver(self,resolution):
        resolution = resolution.replace("*",",")
        res = "--window-size="+resolution
        self.chrome_options.add_argument(argument=res)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"),chrome_options=self.chrome_options)
        return driver

    def Click(self,driver,xpath,location,RunId,Action,UserId,xpath_name):
         driver.find_element("xpath",xpath).click()
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath=xpath,Name=location,RunId=RunId,Action=Action,UserId=UserId,xpath_name=xpath_name)
         img.save_to_db()
    
    def GetText(self,driver,xpath,location,RunId,Action,UserId,xpath_name):
        text = driver.find_element("xpath",xpath).text
        driver.get_screenshot_as_file(location)
        url = Cloud_upload.upload(location)
        img = IMG(img=url,Xpath=xpath,Name=location,RunId=RunId,Action=Action,UserId=UserId,xpath_name=xpath_name)
        img.save_to_db()
        return text

    def Input(self,driver,xpath,input_data,location,RunId,Action,UserId,xpath_name):
        driver.find_element("xpath",xpath).send_keys(input_data)
        driver.get_screenshot_as_file(location)
        url = Cloud_upload.upload(location)
        img = IMG(img=url,Xpath=xpath,Name=location,RunId=RunId,Action=Action,UserId=UserId,xpath_name=xpath_name)
        img.save_to_db()
    
    def Enter(self,driver,xpath,location,RunId,Action,UserId,xpath_name):
         driver.find_element("xpath",xpath).send_keys(Keys.ENTER)
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath=xpath,Name=location,RunId=RunId,Action=Action,UserId=UserId,xpath_name=xpath_name)
         img.save_to_db()
    
    def Title(self,driver,location,RunId,Action,UserId,xpath_name):
         title = driver.title()
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath="None",Name=location,RunId=RunId,Action=Action,UserId=UserId,xpath_name=xpath_name)
         img.save_to_db()
         return title
    
    def Clear(self,driver,xpath,location,RunId,Action,UserId,xpath_name):
         driver.find_element("xpath",xpath).click()
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath=xpath,Name=location,RunId=RunId,Action=Action,UserId=UserId,xpath_name=xpath_name)
         img.save_to_db()
    

    



                        
