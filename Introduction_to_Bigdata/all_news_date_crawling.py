from tqdm.notebook import tqdm
import bs4
from urllib.request import urlopen
import bs4
import pandas as pd
import re
import time
import numpy as np
def number2date(news):
    p = re.compile('[^0-9]')
    number = re.sub(p,'',news)[:8]
    date = number[:4]+'-'+number[4:6]+'-'+number[6:8]
    return date
def all_site_crawling(url_ls):
    df = pd.DataFrame(columns = ['url','date'])
    df['url'] = url_ls
    fix_date = []
    for idx,i in enumerate(tqdm(url_ls)):
        site = i.split('/')[2]
        news = i
        try:
            source = urlopen(i).read()
            source = bs4.BeautifulSoup(source,'html.parser')
        except:
            pass
        korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
        if site == 'news.mk.co.kr': # 크롤링만이 답
            time.sleep(4)
            fix_date.append(source.find_all('li',{'class':'lasttime'})[0].text.split()[-2])
        elif site == 'www.hankyung.com': # 고침
            date  = number2date(news)
            fix_date.append(date)
        elif site == 'www.sedaily.com': # 크롤링만이 답
            time.sleep(4)
            da = source.find_all('span',{'class':'url_txt'})[0].text
            date = re.sub(korean,'',da.split(' ')[0])
            fix_date.append(date.replace('-','.'))
        elif site == 'www.etnews.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'news.heraldcorp.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'view.asiae.co.kr': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.fnnews.com': # 고침
            number = news.split('/')[-1]
            date = number[:4]+'-'+number[4:6]+'-'+number[6:8]
            fix_date.append(date)
        elif site == 'news.kmib.co.kr': # 크롤링만이 답
            time.sleep(4)
            ls = source.find_all('span',{'class':'t11'})[0].text
            fix_date.append(ls.split()[0])
        elif site == 'www.donga.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.edaily.co.kr': # 예외 존재(크롤링만이 답)
            time.sleep(4)
            try:
                ls = source.find_all('div',{'class':'dates'})[0].text.strip()
            except:
                ls = source.find_all('div',{'class':'newsdate'})[0].find('li').text
            ls = re.sub(korean,'',ls).strip().split()[0]
            fix_date.append(ls)
        elif site == 'www.chosun.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.dt.co.kr': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.segye.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'news.mt.co.kr': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'news.joins.com': # 크롤링만이 답
            time.sleep(4)
            date = source.find_all('p',{'class':'date'})[0].text.split()[1]
            fix_date.append(date)
        elif site == 'www.hankookilbo.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.munhwa.com': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.hani.co.kr': # 크롤링만이 답
            time.sleep(4)
            ls = source.find_all('p',{'class':'date-time'})[0].find('span').text
            fix_date.append(ls.split(':')[1].split()[0])
        elif site == 'news.khan.co.kr': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.joongang.co.kr': # 크롤링만이 답
            time.sleep(4)
            ls = source.find_all('p',{'class':'date'})[0].text
            fix_date.append(ls.split()[1])
        elif site == 'www.seoul.co.kr': # 고침
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.busan.com':
            date = number2date(news)
            fix_date.append(date)
        elif site == 'news.imaeil.com':
            date = number2date(news)
            fix_date.append(date)
        elif site == 'biz.khan.co.kr':
            date = number2date(news)
            fix_date.append(date)
        elif site == 'www.khan.co.kr': # 고침
            date = number2date(news)
            fix_date.append(date)
        else:
            fix_date.append(np.nan)
        
        if len(fix_date) != idx+1: # error check
            print(fix_date)
            print(i)
            raise IOError
    df['date'] = fix_date
    return df