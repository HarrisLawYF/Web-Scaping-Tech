# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#------------------------------------ Basic data extraction ----------------------------------
import requests

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

prop = "Prevous Close"
r = requests.get(url)
t = r.text

ind = t.index("Previous Close")
redText = t[ind:].split("</span>")[1]
redText = t[ind:].split("</td>")[1]
val = redText.split(">")[-1]
print(val)


#------------------------------------ Using Beautiful Soup on Google Finance ----------------------------------
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

prop = "Prevous Close"
r = requests.get(url)
t = r.text

soup = BeautifulSoup(t, features = "html.parser")
trs = soup.find_all("tr")
for tr in trs:
    try:
        print("Value: "+tr.find("td", attrs={"class":"Ta(end) Fw(600) Lh(14px)"}).text)
    except:
        pass
        
#------------------------------------ Using Beautiful Soup on all companies of Google Finance ----------------------------------
import requests
import time, datetime
import pandas as pd
import os
from bs4 import BeautifulSoup


def getFinancialInfo(name):
    url = "https://finance.yahoo.com/quote/"+name+"?p="+name
    r = requests.get(url)
    t = r.text
    
    soup = BeautifulSoup(t, features = "html.parser")
    tables = soup.find_all("table")
    trs1 = []
    trs2 = []
    try:
        trs1 = tables[0].find_all("tr")
    except:
        pass
    try:
        trs2 = tables[1].find_all("tr")
    except:
        pass
    trs = trs1 + trs2
    names = []
    values = []
    for tr in trs:
        try:
            name = tr.contents[0].text
            value = tr.contents[1].text
            names.append(name)
            values.append(value)
        except:
            continue
    return names, values

def getCompanyList():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"    
    r = requests.get(url)
    t = r.text
    
    soup = BeautifulSoup(t, features = "html.parser")
    table = soup.find("table", attrs={"id":"constituents"})
    trs = table.find_all("tr")
    del trs[0]
    names = []
    for tr in trs:
        try:
            name = tr.contents[1].text
            names.append(name.strip("\n"))
        except:
            continue
    return names

while(True):
    start = time.time()
    data = {"symbol":[], "metric":[], "value":[], "time":[]}
    symbols = getCompanyList()
    for symbol in symbols:
        names, values = getFinancialInfo(symbol)
        collectedAt = datetime.datetime.now().timestamp()
        for i in range(len(names)):
            data["symbol"].append(symbol)
            data["metric"].append(names[i])
            data["value"].append(values[i])
            data["time"].append(collectedAt)
    df = pd.DataFrame(data)
    
    filepath = "financial_data.csv"
    if os.path.isfile(filepath):
        df.to_csv("financial_data.csv", mode = "a", header = False, columns=["symbol","metric","value","time"])
    else:
        df.to_csv("financial_data.csv", columns=["symbol","metric","value","time"])
    time.sleep(15)
    