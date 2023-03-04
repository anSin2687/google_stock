#importing Modules
import bs4
import requests as rq
import json 
import time
from datetime import datetime 
from zoneinfo import ZoneInfo
import pandas as pd

# attributes = ['DateTime','Previous close','Day range','Year range','Market cap','Avg Volume','P/E ratio',
#  'Dividend yield','Primary exchange','CDP Climate Change Score','CEO','Founded',
#  'Headquarters','Website','Employees','Price']

# quarterly_financial_features = ['Revenue','Operating expense', 'Net income', 'Net profit margin', 'Earnings per share',
#  'EBITDA', 'Effective tax rate', 'Cash and short-term investments', 'Total assets', 'Total liabilities',
#  'Total equity', 'Shares outstanding', 'Price to book', 'Return on assets', 'Return on capital',
#  'Net income', 'Cash from operations', 'Cash from investing', 'Cash from financing', 'Net change in cash',
#  'Free cash flow']

# features_quater = "Quarter,"
# for feature in quarterly_financial_features:
#     features_quater += feature + ","
# file = open('quarterly_report.csv','a')
# file.write(features_quater)
# file.close()

#attributes.append(html.find_all("div",{"class":"mfs7Fc"})[i].text)   

def quaterly_report_dataset_creation(html):
    print("gethering quarter attributes")
    quarter = str(html.find_all("th",{"class":"yNnsfe"})[1].text)[:8]
    rpt_data = html.find_all("td",{"class":"QXDnM"})
    yr_chg_data = html.find_all("td",{"class":"gEUVJe"})
    #quarterly_financial_features = html.find_all("div",{"class":"rsPbEe"})

    quarterly_financial_values = ""
    quarterly_financial_y_y_change = ""
    for index in range(21):
        quarterly_financial_values += rpt_data[index].text + ","
        quarterly_financial_y_y_change += yr_chg_data[index].text + ","

    print("writing to file1")
    file = open('quarterly_y_y_change.csv','a')
    file.write(f"\n{quarterly_financial_y_y_change}")
    file.close()
    
    print("writing to file2")
    file = open('quarterly_report.csv','a')
    file.write(f"\n{quarterly_financial_values}")
    file.close()

def daily_attributes_dataset_creation(html):
    print("gethering daily attributes")
    total_attributes = 16
    values = ""
    price_div = str(html.find_all("div",{"class":"YMlKec fxKbKc"})[0])      #getting price division
    price = float(price_div[28:33])                                         #getting price
    data = html.find_all("div",{"class":"P6K39c"})
    for i in range(total_attributes):
        if i == 0:
            values += str(date_time) + ","
        elif i == 15:
            values += str(price) + ","
        else:
            values +=  data[i-1].text + "," 
            
    print("writing to file")
    file = open('daily_attributes.csv','a')
    file.write(f"\n{values}")
    file.close()


if __name__ == "__main__":
    time_stamp = time.time()                                                        #getting the timestamp for price fetch.
    date_time = datetime.fromtimestamp(time_stamp,ZoneInfo('America/New_York'))     #converting time to Newyork time.
    source_html = rq.get("https://www.google.com/finance/quote/GOOGL:NASDAQ")       #getting html source of the page.
    html = bs4.BeautifulSoup(source_html.content,features="html.parser")           
    daily_attributes_dataset_creation(html)
    quaterly_report_dataset_creation(html)
    
    
    

