import jieba
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

txt = open("comment4.txt", encoding="utf-8").read()
#加载停用词表
stopwords = [line.strip() for line in open("CS.txt",encoding="utf-8").readlines()]
words  = jieba.lcut(txt)
counts = {}
for word in words:
    #不在停用词表中
    if word not in stopwords:
        #不统计字数为一的词
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
items = list(counts.items())

items.sort(key=lambda x:x[1], reverse=True)
x=[]
y=[]
for i in range(30):
    word, count = items[i]
    x.append(word)
    y.append(count)
    mytxt = open('commentcipin.txt', mode='a', encoding='utf-8')
    print ("{:<10}{:>7}".format(word, count),file=mytxt)


fig = plt.figure(figsize=(18, 8),facecolor='snow')
plt.title('微博信息20200310-20200630-评论 词频分析')
p1 = plt.bar(x,y)


plt.show()

