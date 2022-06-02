#these are the imports for flask
from flask import Flask,render_template,request
#these are the imports for selenium
from driv import Chrome

#this is the step used to declare the flask app
app = Flask(__name__)

#this is used the security key
app.secret_key='Varun'

global driver

#this is used to create the page
@app.route("/")
def select_browsers():
        return render_template('index.html',data=[{'name':'firefox'},{'name':'chrome'},{'name':'IE'}],actions=[{'action':'click'},{'action':'getText'},{'action':'Input'}])


@app.route("/browser",methods=["POST"])
def browser():
    browser_name = request.form.get('browsers')
    if browser_name=='chrome':
# this class is to invoke the chrome from the main file
        chrome_1 = Chrome()
#this method is to return the driver from remote 
        driver = chrome_1.driver()

        url = str(request.form["url_input"])

        url="https:"+url
        action_item = request.form.get('Actions')

        xpath = str(request.form["Xpath_info"])

        print(url)
#this is used to navigate to the respected url
        driver.get(url)

        if action_item == "click":

            driver.click(xpath)

        if action_item == "getText":

            text = driver.text(xpath)

            print(text)
        
        if action_item == "Input":

            driver.send_keys(xpath)

        source = str(driver.page_source)
        driver.quit()
        return source,200
    return browser_name

if __name__=='__main__':
    app.run(port=5000,debug=True)