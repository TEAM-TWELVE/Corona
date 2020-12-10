import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://who.maps.arcgis.com/apps/opsdashboard/index.html#/ead3c6475654481ca51c248d52ab9c61"

#fetch html with selenium
driver = webdriver.Firefox()
driver.get(url)



html = driver.execute_script("return document.documentElement.outerHTML")

#Use BeautifulSoup for working with html
soup = BeautifulSoup(html, "html.parser")
covid_soup = soup.find("div", id="ember44").div.nav.find_all("span", class_="flex-horizontal")


covid_dict = {}

#fetch countries with corr
for i in covid_soup:
	country = i.find("strong").get_text(strip=True)
	imgURL = i.p.find_next("p").find_next("p").find("img").get('src') 
	color = imgURL[-5] # colors: 1:green, 2: yellow, 3:red
	
	covid_dict[country] = color


for country in covid_dict:
	print(country, covid_dict[country])




