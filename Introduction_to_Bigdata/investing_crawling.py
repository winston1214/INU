import bs4
from selenium.webdriver import Chrome
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import time
import datetime as dt
from datetime import timedelta
import re
import argparse

def investing(opt):
    # selenium start
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized"); # 시작할때 최대창을 띄워라
    browser = webdriver.Chrome('chromedriver', options=options)

    url = f'https://kr.investing.com/equities/{opt.company}-scoreboard'
    browser.get(url) # 사이트 접속
    time.sleep(1)
    html = browser.page_source
    soup = bs4.BeautifulSoup(html, 'html')
    # compare up & down
    up_string = 'newSiteIconsSprite newSmallBullIcon2 inlineblock middle'
    down_string = 'newSiteIconsSprite newSmallBearIcon2 inlineblock middle'
    up_string = up_string.replace(' ','.')
    down_string = down_string.replace(' ','.')
    # feature setting
    start = 1
    last = 0
    date_index = []
    matrix = soup.select('#sentiments_table > tbody >tr')

    korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')

    # start date & end_date
    START_DATE = opt.START_DATE
    END_DATE = opt.END_DATE
    start_date = dt.datetime.strptime(START_DATE, "%Y-%m-%d")
    end_date = dt.datetime.strptime(END_DATE, "%Y-%m-%d")

    while (end_date >= start_date):
        date_index.append(end_date.strftime("%Y-%m-%d"))
        end_date = end_date - timedelta(days = 1)

    st = dt.datetime.strptime(START_DATE, "%Y-%m-%d")
    end = END_DATE
    # counting = 0
    df = pd.DataFrame({'date':date_index,'up_count':0,'down_count':0})
    

    while dt.datetime.strptime(end, "%Y-%m-%d") >= st:

        matrix = soup.select('#sentiments_table > tbody >tr')
        last += len(matrix)
        for i in range(start,last+1):
           
            today_date = browser.find_element_by_css_selector(f'#sentiments_table > tbody > tr:nth-child({i}) > td.first.left').text.strip()
            today_date = today_date.replace(' ','')
            end = re.sub(korean,'-',today_date)[:-1]
            if dt.datetime.strptime(end, "%Y-%m-%d") >= dt.datetime.strptime(END_DATE,"%Y-%m-%d"):
                browser.find_element_by_css_selector('#moreLink').click() # 더보기 클릭
                print('HI')
                break
            icon = browser.find_element_by_css_selector(f'#sentiments_table > tbody > tr:nth-child({i}) > td.center')
            try:
                icon.find_element_by_class_name(down_string)
                df.loc[df.date == end,'down_count'] += 1
            except:
                icon.find_element_by_class_name(up_string)
                df.loc[df.date == end,'up_count'] += 1

        time.sleep(3)
        browser.find_element_by_css_selector('#moreLink').click() # 더보기 클릭
        start = last
        time.sleep(3)
        print(f'{opt.company} = ~{end} : {last} counts')
    df.to_csv(f'{opt.company}_investing.csv',index=False)
    browser.quit()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--START_DATE',type=str,help='start date',default = '2019-01-23')
    parser.add_argument('--END_DATE',type=str,help='end date',default = '2021-01-23')
    parser.add_argument('--company',type=str,help="['samsung-electronics-co-ltd','nhn-corp','industrial-bank-of-korea','celltrion-inc','seegene-inc']",default='samsung-electronics-co-ltd')
    opt = parser.parse_args()
    investing(opt)
