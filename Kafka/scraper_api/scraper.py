from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
from random import randint

class Scraper() :

    def weather_hourly(self, city) :
        
        weather_info= []

        driver = webdriver.Firefox(executable_path= "/home/adnaneeee/Bureau/Apache kafka/kafka-app-demo/scraper_api/geckodriver")
        driver.get("https://en.sat24.com/en/forecast/h/3313735/rabat")

        time.sleep(3)

        #Look for the class
        search_box = driver.find_element(By.XPATH, '//*[@id="location"]')
            
        #Write what we be searched#
        search_box.send_keys(city)

        time.sleep(2)
        #Submit the text
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)
        url = str(driver.current_url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        weather_data = soup.findAll("div", attrs = {"class" : ["row", "row more"]}) # Find weather section
        time.sleep(randint(2, 8)) # To avoid crashing

        for weather in weather_data : # Loop through each item

            try :

                item = {
                            "date" : weather.find("div", class_ = "date").text.strip(),

                            "hour" : weather.find("div", class_ = "hour").text.strip(),
                                
                            "temperature" : weather.find("div", style = "float: left;").text.strip(),

                            "wind" : weather.select('div.wind > div')[1].text.strip(),

                            "precipitation" : weather.select('div.precipitation > div')[1].text.strip(),

                            "pressure" : weather.select('div.pressure > div')[1].text.strip()

                            }

                weather_info.append(item)

            except :

                print("Error fetching the data")

        return weather_info