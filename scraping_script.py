
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


parties_list = soup.find("div", id="ember44").find_next("div").nav.span.div.find_next("div")

country = parties_list.find("strong").get_text()

colorUrl = parties_list.find("img").get('src')  
colorNumber = colorUrl[-5] # colors: 1:green, 2: yellow, 3:red
color = "red"
if colorNumber == 1:
	color = "green"
elif colorNumber == 2:
	color = "yellow"	


#cases = parties_list.strong.find_next("strong").get_text()

print(parties_list.prettify())

print(country)
print(color)
