from email import header
import time
import csv
from turtle import window_height
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("C:/Users/hp/Downloads/Python/web_scaping_pro/chromedriver")
browser.get(START_URL)
time.sleep(10)



def scrape():
    headers=["V Mag. (mV)"	"Proper_name"	"Bayer_designation"  "Distance (ly)	""Spectral_class"	"Mass (M☉)""	Radius (R☉)"	"Luminosity (L☉)"]
    planet_data=[]
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0]) 
                    except:
                        temp_list.append("")     
            planet_data.append(temp_list)     
        browser.find_element_by_xpath('//*[@id="primary_colums"]/footer/div/div/div/nav/span[2]/a').click()  
        print(f"{i} page done 1")
    with open("scraper.csv","w") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)    
scrape()                   



