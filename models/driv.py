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
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--no-sandbox")
    


    def driver(self):
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"),chrome_options=self.chrome_options)
        return driver

    def Click(self,driver,xpath,location):
         driver.find_element("xpath",xpath).click()
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath=xpath,Name=location)
         img.save_to_db()
    
    def GetText(self,driver,xpath,location):
        text = driver.find_element("xpath",xpath).text
        driver.get_screenshot_as_file(location)
        url = Cloud_upload.upload(location)
        img = IMG(img=url,Xpath=xpath,Name=location)
        img.save_to_db()
        return text

    def Input(self,driver,xpath,input_data,location):
        driver.find_element("xpath",xpath).send_keys(input_data)
        driver.get_screenshot_as_file(location)
        url = Cloud_upload.upload(location)
        img = IMG(img=url,Xpath=xpath,Name=location)
        img.save_to_db()
    
    def Enter(self,driver,xpath,location):
         driver.find_element("xpath",xpath).send_keys(Keys.ENTER)
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath=xpath,Name=location)
         img.save_to_db()
    
    def Title(self,driver,location):
         title = driver.title()
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath="None",Name=location)
         img.save_to_db()
         return title
    
    def Clear(self,driver,xpath,location):
         driver.find_element("xpath",xpath).click()
         driver.get_screenshot_as_file(location)
         url = Cloud_upload.upload(location)
         img = IMG(img=url,Xpath=xpath,Name=location)
         img.save_to_db()
    

        
    

    



                        
