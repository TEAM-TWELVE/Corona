from datetime import datetime, timedelta
from threading import Timer
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
from flask import Flask, request
from flask_restful import Api, Resource


x=datetime.today()
y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def getCovidColor(imgURL):
    print(imgURL)
    #number = imageURL[-5] # colors: 1:green, 2: yellow, 3:red
    #if number == 1:
     #   return "green"
    #elif number == 2:
     #   return "yellow"
    #elif number == 3:
     #   return "red"
        

def web_scrape():
    print("SEBASTIAN SKAL LIGE SE OM NOGET VIRKER")
    url = "https://who.maps.arcgis.com/apps/opsdashboard/index.html#/ead3c6475654481ca51c248d52ab9c61"
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(20)
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, "html.parser")
    covid_soup = soup.find("div", id="ember44").div.nav.find_all("span", class_="flex-horizontal")
    covid_dict = {}
    for i in covid_soup:
	    country = i.find("strong").get_text(strip=True)
	    imgURL = i.p.find_next("p").find_next("p").find("img").get('src') 
        color = getCovidColor(imgURL)
	   #color = imgURL[-5] # colors: 1:green, 2: yellow, 3:red
	    covid_dict[country] = color
    with open('data.json', 'w') as fp:
        json.dump(covid_dict, fp)


t = Timer(secs, web_scrape)
t.start()
web_scrape()

time.sleep(20)

app = Flask(__name__)
api = Api(app)

#data for end point  
f = open('data.json',)
thisdict =  json.load(f) 
f.close() 

#Rest endpoint
class coronaStatus(Resource):
    def get(self):
        st = request.args.get('land')
        return {"status": thisdict.get(st)}

api.add_resource(coronaStatus, "/coronastatus") 


if __name__ == "__main__":
    app.run(debug=True)








#def cleanCountryName(country)
