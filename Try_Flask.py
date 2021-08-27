from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import webbrowser
import time
from selenium import webdriver
from flask import Flask,render_template,url_for,request,redirect
from requests.api import post

contacts=[]
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])

def index():
    if request.method=="POST":
        contact=request.form['name']
        contacts.append(contact)
        for i in contacts:
            print(contacts)
        
        return render_template('index.html',contacts=contacts)
    else:
        return render_template("index.html")
    




#def submit():
 #   if request.method=="POST":
  #      contacts.append(request.form['name']) 
   # return redirect('/')



dist = 50
date = '01-06-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com/")







def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    
    
    for i in data:
        if((i["available_capacity"] > 0) & (i["min_age_limit"] == 45)):
                
            counter += 1
            counting=1
            ls=(i["name"])
            print(i["name"])
            print(i["pincode"])
            print(i["vaccine"])
            print(i["available_capacity"])
            msg='Covid slot available at:{} &date: {} and {} vaccines'.format(i["name"], date,i["available_capacity"])
            user=input()
            for i in contacts:
                user = driver.find_element_by_xpath("//span[@title='{}']".format(i))
                user.click()
                element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'main')))
                msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                for index in range(counting):
                        msg_box.send_keys(msg)
                        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
            
            return True
    if(counter == 0):
        print("No Available Slots")
        return False
   
if(__name__)=='__main__':
    app.run(debug=True)    
  
while(findAvailability() != True):
    time.sleep(5)
    findAvailability()  
    

 

    



