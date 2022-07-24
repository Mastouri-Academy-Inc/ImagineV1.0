from fastapi import FastAPI
from scraper import Scraper
import json
import csv

app = FastAPI() # Launching the app
scraper = Scraper() # Creating instance of Scraper object

@app.get("/{city}")
async def read_data(city) :

    return scraper.weather_hourly(city) # Return scraped list of weather datas