import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager



import pandas as pd
import numpy as np #进行具体的sum,count等计算时候要用到的
df=pd.read_csv('微博信息20200123-20200207-评论1.csv',encoding='utf-8') #这里绝对路径一定要用/,windows下也是如此,不加参数默认csv文件首行为标题行
df.head(20) #查看引入的csv文件前5行数据



def chinese_word_cut(mytext):
    return "/".join(jieba.cut(str(mytext)))

df['cut_comment'] = df['正文'].apply(chinese_word_cut)
df.head()



X_train = df['cut_comment'][:200]
Y_train = df['text_result'][:200]

X_test = df['cut_comment'][200:]
Y_test = df['text_result'][200:]



def get_custom_stopwords(stop_words_file):
    with open(stop_words_file,encoding='utf-8') as f:
        stopwords = f.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list
stop_words_file = 'CS.txt'
stopwords = get_custom_stopwords(stop_words_file)



Vectorizer = CountVectorizer(max_df = 0.8,
                            min_df = 3,
                            token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                            stop_words =frozenset(stopwords) )

test = pd.DataFrame(Vectorizer.fit_transform(X_train).toarray(),
columns=Vectorizer.get_feature_names())
test.head()

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

X_train_vect = Vectorizer.fit_transform(X_train)
nb.fit(X_train_vect, Y_train)
train_score = nb.score(X_train_vect, Y_train)
print(train_score)

X_vec = Vectorizer.transform(df['cut_comment'])
nb_result = nb.predict(X_vec)
df['nb_result'] = nb_result
m=df['nb_result'].sum()#积极评论总数

print(m/len(df))#积极评论的占比

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
fig1=plt.figure(figsize=(10,8))
labels=['积极','消极']
counts=[m,len(df)-m]
colors=['red','blue']

plt.axes(aspect='equal')
plt.xlim(0,8)
plt.ylim(0,8)
plt.pie(x=counts,labels=labels,colors=colors,autopct='%3.1f %%')
plt.title(r'新冠重点新闻评论情感分析')
plt.show()