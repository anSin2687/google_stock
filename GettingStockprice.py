#importing Modules
import bs4
import requests as rq
import json 
import time
from datetime import datetime 
from zoneinfo import ZoneInfo
import pandas as pd

#Getting the price by scraping the Google Finance

source_code = rq.get("https://www.google.com/finance/quote/GOOGL:NASDAQ")
time_stamp = time.time()                                #getting the timestamp for price fetch
html = bs4.BeautifulSoup(source_code.content,features="html.parser")
divisions = str(html.find_all("div",{"class":"YMlKec fxKbKc"})[0])
price = float(divisions[28:33])

time_stamp = time.time()
date_time = datetime.fromtimestamp(time_stamp,ZoneInfo('America/New_York'))

stockprice = pd.DataFrame([[str(date_time).split(".")[0],price]],columns = ['DateTime','Price'])
stockprice.set_index(['DateTime'],inplace=True)
prev_price = pd.read_csv('/home/opc/scripts/GoogleStock.csv')
prev_price.set_index(['DateTime'],inplace=True)
stockprice = pd.concat([prev_price,stockprice])
stockprice.to_csv('/home/opc/scripts/GoogleStock.csv')

