import csv

def readCSV():
    with open('微博信息20200310-20200630-评论.csv','r',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        for i in reader:
            mytxt=open('comment4.txt', mode='a', encoding='utf-8')
            print(dict(i)['正文'],file=mytxt)



readCSV()