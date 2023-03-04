#importing Modules
import bs4
import requests as rq
import json 
import time
from datetime import datetime 
from zoneinfo import ZoneInfo
import pandas as pd


time_stamp = time.time()                                 #getting the timestamp for price fetch
date_time = datetime.fromtimestamp(time_stamp,ZoneInfo('America/New_York'))


#Getting the price by scraping the Google Finance

source_code = rq.get("https://www.google.com/finance/quote/GOOGL:NASDAQ")

html = bs4.BeautifulSoup(source_code.content,features="html.parser")    #getting html source of the page.
price_div = str(html.find_all("div",{"class":"YMlKec fxKbKc"})[0])      #getting price division
price = float(price_div[28:33])                                         #getting price



attributes = ['Previous close','Day range','Year range','Market cap','Avg Volume','P/E ratio',
 'Dividend yield','Primary exchange','CDP Climate Change Score','CEO','Founded',
 'Headquarters','Website','Employees','Price']

quarterly_financial_features = ['Revenue','Operating expense', 'Net income', 'Net profit margin', 'Earnings per share',
 'EBITDA', 'Effective tax rate', 'Cash and short-term investments', 'Total assets', 'Total liabilities',
 'Total equity', 'Shares outstanding', 'Price to book', 'Return on assets', 'Return on capital',
 'Net income', 'Cash from operations', 'Cash from investing', 'Cash from financing', 'Net change in cash',
 'Free cash flow']

values = " "
for i in range(14):
    values +=  html.find_all("div",{"class":"P6K39c"})[i].text + "," 
    #attributes.append(html.find_all("div",{"class":"mfs7Fc"})[i].text)   


quarter = str(html.find_all("th",{"class":"yNnsfe"})[1].text)[:8]

#quarterly_financial_features = html.find_all("div",{"class":"rsPbEe"})

quarterly_financial_values = []
quarterly_financial_y_y_change = []
for index in range(len(quarterly_financial_features)):
    quarterly_financial_values.append(html.find_all("td",{"class":"QXDnM"})[index].text)
    quarterly_financial_y_y_change.append(html.find_all("td",{"class":"gEUVJe"})[index].text)



val = pd.Series(values)
val = val.add(str(price))




"""
stockprice = pd.DataFrame([[str(date_time).split(".")[0],price]],columns = ['DateTime','Price'])
stockprice.set_index(['DateTime'],inplace=True)
prev_price = pd.read_csv('/home/opc/scripts/GoogleStock.csv')
prev_price.set_index(['DateTime'],inplace=True)
stockprice = pd.concat([prev_price,stockprice])
stockprice.to_csv('/home/opc/scripts/GoogleStock.csv')
"""
file = open('example_csv.csv','a')
file.write(f"\n{price} + "," + {val}")
file.close()

