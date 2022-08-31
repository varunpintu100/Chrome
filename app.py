'''
<copyright file="projectCode">
Authors = Varun Ramarthi, Sravan Chowdary
Copyright(c) PROJECTCODE. All rights reserved.
</copyright>

'''

import traceback
import os
#these are the imports for flask
from flask import Flask,render_template,request
from models.ApiTesting import API
#these are the imports for selenium
from models.driv import Chrome
from models.imageTable import IMG
import cloudinary

#this is the step used to declare the flask app
app = Flask(__name__)

cloudinary.config(
    cloud_name="dwxf7m3ok",
    api_key="355315699667415",
    api_secret="fyrznhQeyvg--HoLvGxgOPuOqus"
    )

uri = os.environ.get("DATABASE_URL","sqlite:///data.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI']=uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#this is used the security key
app.secret_key='Varun'
#this is to use the driver globally
global driver

data = [{'name':'firefox'},{'name':'chrome'},{'name':'IE'}]
method=[{'name':"GET"},{'name':"PUT"},{'name':"POST"}]
size=[{'size':"1270*1024"},{'size':"1366*768"},{'size':"1600*900"},{'size':"1920*1080"},{'size':"1920*1200"},{'size':"2560*1440"},{'size':"3440*1440"},{'size':"3840*2160"}]

#this is used to create the page
@app.route("/")
def select_browsers():
    return render_template('homepage.html')

@app.route("/uiautomation")
def uiautomation():
        testData = IMG.query.all()
        return render_template('uiautomation.html',data=data,size=size,testData=testData)

@app.route("/apiautomation")
def apiautomation():
        return render_template("apiautomation.html",data=method)

@app.route("/apiautomation/endpoint",methods=["POST"])
def Hitendpoint():
    api=API()
    method = request.form.get('method')
    print(method)
    url = request.form["Endpoint"]
    print(url)
    body = request.form["RequestBody"]
    print(body)
    try:
        if method=="GET":
            response = api.GET(url=url,body=body)
        if method == "POST":
            response = api.POST(url=url,body=body)
    except Exception as e:
        return {"message":f"{e}"}
    return render_template("apiresponse.html",response=response)
    


@app.route("/uiautomation/browser",methods=["POST"])
def browser():
    testData = IMG.query.all()
    runId =0 
    for test_data in testData:
        if(test_data.RunId >= runId):
            print(test_data.RunId)
            runId = test_data.RunId
    runId = runId+1
    browser_name = request.form.get('browsers')
    resolution = request.form.get('Dimensions')

    chrome_1 = Chrome()
#this method is to return the driver from remote
    
    
    
    driver = chrome_1.driver(resolution) 



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
            title=""
# this class is to invoke the chrome from the main file
            
#this is used to get the data from the form in the html
            url = str(request.form["url_input"]).replace("https://","")
#this is used to add https: in the starting of the url
            url="https://"+url
            #this is used to get the type of action that needs to be performed
            action_item = request.form.getlist('Actions')
           
            #this is used to get the xpath info from the forms
            xpath = request.form.getlist("Xpath_info")
            
            input_data = request.form.getlist("Input_text_1")
            
            #this is o get the url in the console
            print(f"The given URL is : {url}")
#this is used to navigate to the respected url
            driver.get(url)
            i,j=0,0
            for i in range(0,len(action_item)):
                location = "image_"+str(i)+".png"
                if xpath[i]!="":
            #this is used to perform the action item and based on the if condition respective action will happen
                    if action_item[i] == "click":

                        chrome_1.Click(driver=driver,xpath=xpath[i],location=location,RunId=runId,Action=action_item[i],UserId="Developer",xpath_name="Test")

                        lt.append({'action':action_item[i],'xpath':xpath[i]})

                    if action_item[i] == "getText":
                        
                        title = chrome_1.GetText(driver=driver,xpath=xpath[i],location=location,RunId=runId,Action=action_item[i],UserId="Developer",xpath_name="Test")

                        lt.append({'action':action_item[i],'xpath':xpath[i]})

                    if action_item[i] == "Input":

                        chrome_1.Input(driver=driver,xpath=xpath[i],input_data=input_data[j],location=location,RunId=runId,Action=action_item[i],UserId="Developer",xpath_name="Test")

                        j=j+1
                        
                        lt.append({'action':action_item[i],'xpath':xpath[i]})

                    if action_item[i] == "Enter":

                        chrome_1.Enter(driver=driver,xpath=xpath[i],location=location,RunId=runId,Action=action_item[i],UserId="Developer",xpath_name="Test")

                        lt.append({'action':action_item[i],'xpath':xpath[i]})

                    if action_item[i] == "getTitle":

                        title = chrome_1.Title(driver=driver,location=location,RunId=runId,Action=action_item[i],UserId="Developer",xpath_name="Test")
    
                        lt.append({'action':action_item[i],'xpath':'None'})
                    
                    if action_item[i] == "Clear":

                        chrome_1.Clear(driver=driver,xpath=xpath[i],location=location,RunId=runId,Action=action_item[i],UserId="Developer",xpath_name="Test")

                        lt.append({'action':action_item[i],'xpath':xpath[i]})

            #this is used to store the source of the page as a string
            driver.quit()
            #this is used to check weather we are getting any text if no text is found then it returns the webpage source
            test = IMG.query.all()
            url_list=[]
            for j in test:
                url_list.append(j.img)
            return render_template('report.html',i=i,urls=url_list,info_list=lt)
        return browser_name
#this is used to quit the driver when some exception occurs all of a sudden.
    except Exception as e:
        driver.quit()

        if "Exceptionlist" in e:
            return render_template('uiautomation.html',error="Please enter the xpath for the second object",data=data)
        
        return {"message":f"Exception{e}{traceback.print_exc()}"}


if __name__=='__main__':
    from database import db  # we are importing this as a part of circular imports
    db.init_app(app)
    app.run(port=5000,debug=True)
