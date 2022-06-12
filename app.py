#these are the imports for flask
from flask import Flask,render_template,request
#these are the imports for selenium
from driv import Chrome
from selenium.webdriver.common.keys import Keys
import PIL.Image
#this is the step used to declare the flask app
app = Flask(__name__)

#this is used the security key
app.secret_key='Varun'

#this is to use the driver globally
global driver

data = [{'name':'firefox'},{'name':'chrome'},{'name':'IE'}]

actions = [{'action':'click'},{'action':'getText'},{'action':'Input'},{'action':'Enter'},{'action':'getTitle'},{'action':'Clear'}]

#this is used to create the page
@app.route("/")
def select_browsers():
        return render_template('index.html',data=data,actions=actions,test=0)

@app.route("/count",methods=["POST"])
def input_count():
    count = int(request.form['number_input'])
    return render_template('index.html',data=data,actions=actions,test=count)

@app.route("/browser",methods=["POST"])
def browser():

    browser_name = request.form.get('browsers')
    # list_of_files = os.listdir(os.getcwd())
    # for each_file in list_of_files:
    #     if each_file.startswith("ScreenShots"):
    #         for file in each_file:
    #             print(file)
    #             os.remove(file)
    #this medthod is used to try and find the exceptions if needed.
    try:
        lt=[]
        #this is the condition used to check the data whether the name of the browser is correct or not
        if browser_name=='chrome':

            #this temp is used to store the text form the xpath and store it statically
            temp=""
# this class is to invoke the chrome from the main file
            chrome_1 = Chrome()
#this method is to return the driver from remote
            driver = chrome_1.driver()
#this is used to get the data from the form in the html
            url = str(request.form["url_input"])
#this is used to add https: in the starting of the url
            url="https://"+url
            #this is used to get the type of action that needs to be performed
            action_item = request.form.getlist('Actions')
            #this is used to get the xpath info from the forms
            xpath = request.form.getlist("Xpath_info")

            input_data = request.form.getlist("Input_text")
            #this is o get the url in the console
            print(f"The given URL is : {url}")
#this is used to navigate to the respected url
            driver.get(url)
            j=0
            for i in range(0,len(action_item)):
                location = "image_"+str(i)+".png"
                if xpath[i]!="":
            #this is used to perform the action item and based on the if condition respective action will happen
                    if action_item[i] == "click":

                        driver.find_element_by_xpath(xpath=xpath[i]).click()

                        driver.get_screenshot_as_file(location)

                        image = PIL.Image.open(location)

                        image.show()

                        lt.append({"click":xpath[i]})

                    if action_item[i] == "getText":

                        temp = driver.find_element_by_xpath(xpath=xpath[i]).text

                        driver.get_screenshot_as_file(location)

                        image = PIL.Image.open(location)

                        image.show()

                        lt.append({"getText":xpath[i] + "--" + temp})

                    if action_item[i] == "Input":

                        driver.find_element_by_xpath(xpath=xpath[i]).send_keys(input_data[j])
                        j=j+1
                        driver.get_screenshot_as_file(location)

                        image = PIL.Image.open(location)

                        image.show()

                        lt.append({"Input":xpath[i] +"--"+ input_data[j-1]})

                    if action_item[i] == "Enter":

                        driver.find_element_by_xpath(xpath=xpath[i]).send_keys(Keys.ENTER)
                        driver.get_screenshot_as_file(location)

                        image = PIL.Image.open(location)

                        image.show()

                        lt.append({"Enter":xpath[i]})

                    if action_item[i] == "getTitle":

                        temp = driver.title()
                        driver.get_screenshot_as_file(location)

                        image = PIL.Image.open(location)

                        image.show()

                        lt.append({"getTitle":xpath[i] +"--"+ temp})
                    
                    if action_item[i] == "Clear":

                        driver.find_element_by_xpath(xpath=xpath[i]).clear()
                        driver.get_screenshot_as_file(location)

                        image = PIL.Image.open(location)

                        image.show()

                        lt.append({"Clear":xpath[i]})

            #this is used to store the source of the page as a string
            driver.quit()
            #this is used to check weather we are getting any text if no text is found then it returns the webpage source
            if temp=="":
                return {"message":lt},200
            return {"message":f"The data we got is {temp}"},200
        return browser_name
#this is used to quit the driver when some exception occurs all of a sudden.
    except Exception as e:
        driver.quit()

        return {"message":f"Exception{e}"}


if __name__=='__main__':
    app.run(port=5000,debug=True)
