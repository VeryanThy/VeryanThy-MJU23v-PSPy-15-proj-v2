# This program scrapes the slutpris data from hemnet for östergötland and saves it to file 
#using selenium as a headless webbrowser with chromedriver as a webdriver
import requests
import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

DRIVER_PATH = '/Applications/chromedriver_mac64'

def scrape_page(link):
  options = Options()
  options.headless = True
  driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
  driver.get(link)
 # finds elements by class name holding the relevant data I want to collect
  location_data = driver.find_elements(By.CLASS_NAME, "sold-property-listing__location")
  size_data = driver.find_elements(By.CLASS_NAME, "sold-property-listing__size")
  price_data =  driver.find_elements(By.CLASS_NAME, "sold-property-listing__price-info")  
  
  # creates a list of lists with the text from the html elements found, and writes them to file
  i = 0
  property_data = []
  while i < len(location_data):
    property_data.append([location_data[i].text, size_data[i].text, price_data[i].text]) 
    i += 1
  for property in property_data:
      with open('hemnet_slutpris_södermanland.csv', 'a') as f:
        f.write(property[0] + "," + property[1] + "," + property[2] + ",")

# runs a loop through the number of pages on the website
number_of_pages = 50
i = 1
while i <= number_of_pages:
  link = "https://www.hemnet.se/salda/bostader?item_types%5B%5D=villa&location_ids%5B%5D=17746&page=" + str(i)
  scrape_page(link)
  i +=1


