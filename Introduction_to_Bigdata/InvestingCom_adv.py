# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:43:56 2020

@author: Jayleen

for faster crawling
"""

from selenium import webdriver
import time
import datetime as dt
from datetime import timedelta
from bs4 import BeautifulSoup

import pandas as pd
# import numpy as np
import os


invesco = ["AAPL", "AMZN", "MSFT", "FB", "GOOGL", "TSLA", "GOOG", "NVDA", "ADBE", "NFLX"]
# START_DATE = '2019-12-01'
START_DATE = "2019-12-01"
# END_DATE = '2020-09-01'
END_DATE = '2020-01-26'
site = ["apple-computer-inc", "amazon-com-inc", "microsoft-corp", "facebook-inc", "google-inc",
         "tesla-motors", "google-inc-c", "nvidia-corp", "adobe-sys-inc", "netflix,-inc."]

# tick
k = 5

# basic Date Dataframe
date_index = []
bd = dt.datetime.strptime(END_DATE, '%Y-%m-%d')

while (bd >= dt.datetime.strptime(START_DATE, "%Y-%m-%d")):
    date_index.append(bd.strftime("%Y-%m-%d"))
    bd = bd - timedelta(days = 1)

DATE = pd.DataFrame({"date": date_index})

#%%
bullbear = pd.DataFrame({"Date": date_index, '%s_Bullish' %invesco[k]: 0, '%s_Bearish' %invesco[k]: 0})

# def FasterInvesting(url, qqq):
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.investing.com/equities/%s-scoreboard" %site[k]) #헤더 필요없음
time.sleep(1)
print("------ %s crawling ------" %invesco[k])


d = END_DATE
start = 1
c = 1

print("..start")
# try:
    
while (dt.datetime.strptime(d, "%Y-%m-%d") >= dt.datetime.strptime(START_DATE, "%Y-%m-%d")):

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    last = len(soup.select("#sentiments_table > tbody > tr"))

    for i in range(start, last + 1):
        
        counting = 1
        d = driver.find_element_by_css_selector("#sentiments_table > tbody > tr:nth-child(%d) > td.first.left" %i).text.strip()
        d = dt.datetime.strptime(d, "%b %d, %Y").strftime("%Y-%m-%d")
        
        if dt.datetime.strptime(d, "%Y-%m-%d") > dt.datetime.strptime(END_DATE, "%Y-%m-%d"):
            start = last
            break
        # r = driver.find_element_by_css_selector("#sentiments_table > tbody > tr:nth-child(%d) > td:nth-child(4)" %i).text.strip()
        # openRate.append(r)

        icon = driver.find_element_by_css_selector("#sentiments_table > tbody > tr:nth-child(%d) > td.center" %i)
        try :
            icon.find_element_by_class_name("newSiteIconsSprite.newSmallBullIcon2.inlineblock.middle")
            bullbear.loc[bullbear.Date == d, '%s_Bullish' %invesco[k]] += counting
        except :
            icon.find_element_by_class_name("newSiteIconsSprite.newSmallBearIcon2.inlineblock.middle")
            bullbear.loc[bullbear.Date == d, '%s_Bearish' %invesco[k]] += counting
            
        start = last

    driver.find_element_by_css_selector("#moreLink").click()
    print("%d click %s" %(c, d))
    c += 1
    time.sleep(2)

#%%    
if os.path.exists('BullBear_%s.csv' %invesco[k]):
    bullbear.to_csv('BullBear_%s.csv' %invesco[k], index = False, mode = 'a', encoding = 'utf-8', header = False) #utf-8-sig: 한글
else:
    bullbear.to_csv('BullBear_%s.csv' %invesco[k], index = False, mode = 'w', encoding = 'utf-8')
    
print("load data: 총 %d개" %last)
    
# df = pd.DataFrame({"date" : date, "Bullish": bullish, "Bearish": bearish})
driver.close()
    
    # return df

