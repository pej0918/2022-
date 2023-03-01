from webdriver_manager.chrome import ChromeDriverManager

from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
from pymongo import MongoClient
client = MongoClient('mongodb+srv://pej2834:pej09180429@cluster0.ceosi8e.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

url='http://mtweather.nifos.go.kr/mount/local'

res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver=webdriver.Chrome("C:\\Users\\samsung\\Desktop\\deep daiv\\chromedriver.exe")

url = 'http://mtweather.nifos.go.kr/mount/local'
driver.get(url)



list_tmp = []
list_rain = []
list_hm = []
list_ws = []
list_mt = []
list_addr=[]

url = 'http://mtweather.nifos.go.kr/mount/local'
driver.get(url)
driver.find_element_by_xpath('//*[@id="choiceTxt"]/ul/li[2]/a').click()


for i in range(1,125):
    for j in range(6):
        clicks='//*[@id="choiceTxt"]/div/div/a[{}]'.format(i)
        driver.find_element_by_xpath(clicks).click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        list_addr.append(soup.find('span', {'data-ajax':'addr'}).get_text())
        list_mt.append(soup.find('span', {'data-ajax': 'obsName'}).get_text())
        list_tmp.append(soup.find('span', {'data-ajax': 'tmpr'}).get_text())
        list_rain.append(soup.find('p', {'data-ajax': 'rain'}).get_text())
        list_hm.append(soup.find('p', {'data-ajax': 'hm'}).get_text())
        list_ws.append(soup.find('p', {'data-ajax': 'windspeed'}).get_text())

df=pd.DataFrame({'mt':list_mt,'hm':list_hm, 'tmp':list_tmp, 'rain':list_rain, 'ws':list_ws, 'addr':list_addr})
df.drop_duplicates(['mt'],inplace=True)
df=df.iloc[1:,:]

list_mt=list(df['mt'].values)
list_hm=list(df['hm'].values)
list_rain=list(df['rain'].values)
list_tmp=list(df['tmp'].values)
list_ws=list(df['ws'].values)
list_addr=list(df['addr'].values)

print(list_mt[0].split(' ')[1])

for i in range(len(list_mt)):
    db.Ganwon_forestweather.update_one({'mt': list_mt[i]}, {'$set': {'tmp':list_tmp[i], 'addr':list_addr[i],'hm':list_hm[i], 'rain':list_rain[i], 'ws':list_ws[i]}})