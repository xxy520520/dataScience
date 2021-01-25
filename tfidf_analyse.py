# -*-coding:utf-8-*-


import jieba.analyse
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

"""
       TF-IDF权重：
           1、CountVectorizer 构建词频矩阵
           2、TfidfTransformer 构建tfidf权值计算
           3、文本的关键字
           4、对应的tfidf矩阵
"""

# 读取文件
def read_news():
    news = open('news4.txt',encoding='utf-8').read()
    return news
x=[]
y=[]

# jieba分词器通过词频获取关键词
def jieba_keywords(news):

    keywords = jieba.analyse.extract_tags(news, topK=30,withWeight=True, allowPOS=('n','nr','ns'))

    for item in keywords:
        print(item[0], item[1])
        x.append(item[0])
        y.append(item[1])

    fig = plt.figure(figsize=(18, 8), facecolor='snow')
    plt.title('20200310-20200630 TF-IDF词频分析')
    p1 = plt.bar(x, y)

    plt.show()


if __name__ == '__main__':
    news = read_news()
    jieba_keywords(news)
