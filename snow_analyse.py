from snownlp import SnowNLP
from snownlp import sentiment
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

higher=0
high=0
soso=0
low=0
lower=0

with open('微博信息20200123-20200207.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        mytxt = open('snow_comment4.txt', mode='a', encoding='utf-8')
        s=SnowNLP(dict(i)['正文'])
        print(dict(i)['正文'], s.sentiments, file=mytxt)

        if s.sentiments>0.8:
            higher = higher + 1
        if s.sentiments>0.6 and s.sentiments<=0.8:
            high = high + 1
        if s.sentiments>0.4 and s.sentiments<=0.6:
            soso = soso + 1
        if s.sentiments>0.2 and s.sentiments<=0.4:
            low =low +1
        if s.sentiments>0 and s.sentiments<=0.2:
            lower=lower+1

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
fig1=plt.figure(figsize=(10,8))
labels=['非常积极','比较积极','中性','比较消极','非常消极']
counts=[higher,high,soso,low,lower]
colors=['red','yellow','green','blue','purple']

plt.axes(aspect='equal')
plt.xlim(0,8)
plt.ylim(0,8)
plt.pie(x=counts,labels=labels,colors=colors,autopct='%3.1f %%')
plt.title(r'snowNLP新冠新闻情感分析')
plt.show()

print(higher,high,soso,low,lower)