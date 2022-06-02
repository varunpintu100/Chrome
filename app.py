#these are the imports for flask
from curses.ascii import NUL
from flask import Flask,render_template,request
#these are the imports for selenium
from driv import Chrome

#this is the step used to declare the flask app
app = Flask(__name__)

#this is used the security key
app.secret_key='Varun'

#this is to use the driver globally
global driver

#this is used to create the page
@app.route("/")
def select_browsers():
        return render_template('index.html',data=[{'name':'firefox'},{'name':'chrome'},{'name':'IE'}],actions=[{'action':'click'},{'action':'getText'},{'action':'Input'}])


@app.route("/browser",methods=["POST"])
def browser():
    #this medthod is used to try and find the exceptions if needed.
    try:
        browser_name = request.form.get('browsers')
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
            url="https:"+url
            #this is used to get the type of action that needs to be performed
            action_item = request.form.get('Actions')
            #this is used to get the xpath info from the forms
            xpath = str(request.form["Xpath_info"])
            #this is o get the url in the console
            print(url)
#this is used to navigate to the respected url
            driver.get(url)

            #this is used to perform the action item and based on the if condition respective action will happen
            if action_item == "click":

                driver.find_element_by_xpath(xpath=xpath).click()

            if action_item == "getText":

                temp = driver.find_element_by_xpath(xpath=xpath).text
        
            if action_item == "Input":

                driver.find_element_by_xpath(xpath=xpath).send_keys("Varun")

            #this is used to store the source of the page as a string
            source = str(driver.page_source)
            driver.quit()
            #this is used to check weather we are getting any text if no text is found then it returns the webpage source
            if temp=="":
                return source,200
            return temp
        return browser_name
#this is used to quit the driver when some exception occurs all of a sudden.
    except:
        driver.quit() 
            

if __name__=='__main__':
    app.run(port=5000,debug=True)