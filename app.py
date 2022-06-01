#these are the imports for flask
from flask import Flask,render_template,request,url_for

#these are the imports for selenium
from selenium import webdriver
from main import Chrome

#this is the step used to declare the flask app
app = Flask(__name__)

#this is used the security key
app.secret_key='Varun'

#this is used to create the page
@app.route("/")
def select_browsers():
        return render_template('index.html',data=[{'name':'firefox'},{'name':'chrome'},{'name':'IE'}])


@app.route("/browser",methods=["POST"])
def browser():
# this class is to invoke the chrome from the main file
    chrome_1 = Chrome()

#this method is to return the driver from remote 
    driver = chrome_1.driver()

#this is used to navigate to the respected url
    driver.get("https://varun-resume.herokuapp.com")

    print(driver.page_source)

if __name__=='__main__':
    app.run(port=5000,debug=True)