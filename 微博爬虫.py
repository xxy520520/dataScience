import requests,random,bs4,time,re,csv,json,os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
from tqdm import tqdm

'''修改程序运行路径'''
# os.chdir(r"D:\vscode\py_bank\171250619\code") #修改自己的运行路径

'''打开文件夹,准备写入'''
word_name='微博信息20191208-20200122'  #爬取文件名字（这个是自己选取内容时进行更改的）
# fp = open(r'../out_put/'+word_name+'.csv','w',encoding = 'gb18030',errors='ignore',newline = '')
fp = open(word_name+'.csv','w',encoding = 'utf-8',errors='ignore',newline = '')
writer = csv.writer(fp)
header = ['名字','正文']
writer.writerow(header)
headers = {
        'User-Agent':UserAgent().random,
        'Cookie': '_T_WM=71684594584; WEIBOCN_FROM=1110006030; SCF=AmUw98emhahMgXvZwoANU7lhckxdUibWuaO3QOtfDtQ7LyKJCnsgF3QKVBEZJCBknNrm9tg0ANXWeV2a9KLbe34.; SUB=_2A25NCllwDeRhGeBK7lsS9i7OzDiIHXVu9Wc4rDV6PUNbktAKLRH6kW1NR7PcUReZucwthAhQZCRrMEssbo25CKew; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWh4aV2v7TrAnyZcrkj8Fqd5JpX5KMhUgL.FoqXSK.0So5ES0B2dJLoIEXLxK-L1KeL1hnLxK-L1KeL1hnLxK-LBo5L12qLxK-LBo5L12qLxK.L1KMLB-zt; SSOLoginState=1611540768; ALF=1614132768' ##使用自己的cookie
        }

def save_data(datas):
    writer.writerow(datas)          

def get_txt():
    start=1
    end=19   #控制爬取页数
    url = 'https://s.weibo.com/weibo?q=%E7%96%AB%E6%83%85&xsort=hot&suball=1&timescope=custom:2019-12-08:2020-01-22&Refer=SWeibo_box&page={}'
    for page in tqdm(range(start, end+1)):
        url_0 = url.format(page)
    # url='https://s.weibo.com/weibo?q=%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E&xsort=hot&suball=1&timescope=custom:2019-12-08:2020-01-22&Refer=g'
        response=requests.get(url_0,headers=headers,timeout=60)
        bs = bs4.BeautifulSoup(response.text,'html.parser')  #翻译
        txts=bs.find(class_='m-con-l').find_all(class_='card-wrap')
        for txt in txts:
            try:
                text=txt.find_all(class_='txt')[1].text.replace(' ','')
            except:
                text=txt.find(class_='txt').text.replace(' ','')
            name=txt.find(class_='name').text.replace(' ','')
            tm=txt.find(class_='from').text.replace(' ','')
            datas=[name,text,tm]
            save_data(datas)
            # print(name,text,tm)

def get_pinglun(mid):
    # url='https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4569792616335323&page=1'
    start=1
    end=300
    url='https://weibo.com/aj/v6/comment/big?ajwvr=6&id='+mid+'&page={}'
    for page in tqdm(range(start, end+1)):
        try:
            url_1 = url.format(page)
            headers = {
            'Cookie':'SINAGLOBAL=6724017172360.135.1589953599360; ALF=1639707749; SCF=AudkK3cK3Lgk2mt7eZjqhseOiGS0AHeJI8R5tVaWQdUMUx0ycGDfGwK86cyvEFE94dXyMIiymb3Ww7yaRW7-2Kw.; SUB=_2A25y3oXKDeRhGedG4lMX8SvNzzyIHXVuICuCrDV8PUJbkNANLW3ekW1NUOlHA2NH5fIasTRofeSEvBWMggjK-yyk; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWMWxz-qrW.ZMNG.x4QnFD25NHD95Qp1h.pSo2feKB7Ws4DqcjVi--Ri-8siKL2i--Xi-zRiKy2i--fi-2XiKLWi--fiKnfiKnRi--NiK.XiKLsC5tt; UOR=www.ujiuye.cn,widget.weibo.com,www.baidu.com; wvr=6; _s_tentry=www.baidu.com; Apache=9297895961589.357.1611540283733; ULV=1611540283851:15:2:1:9297895961589.357.1611540283733:1610502750041; webim_unReadCount=%7B%22time%22%3A1611542228829%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A999%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1217%2C%22msgbox%22%3A0%7D; WBStorage=8daec78e6a891122|undefined', ##使用自己的cookie
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44',
            }

            response=requests.get(url_1,headers=headers,timeout=60)
            # response.encoding='ks_c_5601'
            json_html = json.loads(response.text)
            text=json_html['data']['html']
            # print(text)
            bs = bs4.BeautifulSoup(text,'html.parser')  #翻译
            pingluns=bs.find(class_='list_box').find_all(class_='list_li S_line1 clearfix')
            for pinglun in pingluns:
                pinglun_1=pinglun.find(class_='list_con').find(class_='WB_text').text.split('：')
                name_pinlun=pinglun_1[0]
                try:
                    pinglun_text=pinglun_1[1].split(':')[1]
                except:
                    pinglun_text=pinglun_1[1]

                # dianzan_pinlun=pinglun.find(class_='WB_func clearfix').find(class_='line S_line1').text
                # datas.append([name,zw,name_pinlun,pinglun_text])
                datas=[name_pinlun,pinglun_text]
                save_data(datas)
                # print(name_pinlun,pinglun_text)
        except Exception as e:
            print(str(e))


def main():
    get_txt() #获取微博正文

    # mids=['4469445265017563','4469413552023980']
    # for mid in mids:
    #     get_pinglun(mid) #获取微博评论


if __name__ == "__main__":
    
    main()
    fp.close()


