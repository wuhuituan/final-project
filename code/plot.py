import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus']=False

data=pd.read_csv(r'C:\Users\iwas\PycharmProjects\final project\Future weather')
data_=data.drop(index=[0])
data_['Highest Temp']=data_['temp'].str.slice(0,3)
data_['Lowest Temp']=data_['temp'].str.slice(3)
data_['Highest Temp']=data_['Highest Temp'].map(lambda x:int(x.replace('°','')))
data_['Lowest Temp']=data_['Lowest Temp'].map(lambda x:int(x.replace('°','')))
dates=data_['date']
highs=data_['Highest Temp']
lows=data_['Lowest Temp']

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.2)

plt.title('Future weather',fontsize=24)
plt.xlabel('Date',fontsize=12)
plt.ylabel('Temp',fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=10)
plt.xticks(dates[::1])
plt.show()