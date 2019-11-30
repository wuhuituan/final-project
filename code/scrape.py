import requests
from bs4 import BeautifulSoup
import pandas
page = requests.get("https://weather.com/weather/tenday/l/29a61b0981a8fc0cd73ae4bf79421c52a6acf4974575052fb57ceeafacb0ccf5")
content = page.content
soup = BeautifulSoup(content, 'lxml')
l=[]
all = soup.find("div", {"class": "locations-title ten-day-page-title"}).find("h1").text
table = soup.find_all("table", {"class": "twc-table"})
for data in table:
    for i in range(len(data.find_all("tr"))-1):
        d = {}
        try:
            d["day"]=data.find_all("span",{"class":"date-time"})[i].text
            d["date"]=data.find_all("span",{"class":"day-detail"})[i].text
            d["desc"]=data.find_all("td",{"class":"description"})[i].text
            d["temp"]=data.find_all("td",{"class":"temp"})[i].text
            d["wind"]=data.find_all("td",{"class":"wind"})[i].text
        except:
            d["day"]="None"
            d["date"]="None"
            d["desc"]="None"
            d["temp"]="None"
            d["wind"]="None"
        l.append(d)
df = pandas.DataFrame(l)
df.to_csv('Future weather')












