from snownlp import SnowNLP
from snownlp import sentiment
import csv


f1 = open('./pos.txt', 'a+',encoding='utf-8')  # 存放正面  名字也可自定义哦
f2 = open('./neg.txt', 'a+',encoding='utf-8')  # 存放负面

with open('微博信息20191208-20200122.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        mytxt = open('commentqinggan.txt', mode='a', encoding='utf-8')
        s=SnowNLP(dict(i)['正文'])
        if s.sentiments<0.25:
            f2.write(dict(i)['正文'])
            f2.write('\n')

        if s.sentiments>0.8:
            f1.write(dict(i)['正文'])
            f1.write('\n')
        print(dict(i)['正文'],s.sentiments, file=mytxt)


# 保存此次的训练模型
sentiment.train('neg.txt', 'pos.txt')
# 生成新的训练模型
sentiment.save('sentiment.marshal')