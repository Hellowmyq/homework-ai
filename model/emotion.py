from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
def read_html(url):    #定义读取html网页函数
    headers = {'User-Agent':  "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
  }
    response =requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    return(response.text)

def html_text(info,word): #按关键词解析文本
    return([w.get_text() for w in info.select(word)])#跟find差不多


def gupiao_page(Soup):  #单个网页信息
    gupiao=pd.DataFrame()
    # gupiao['阅读']=html_text(Soup,'.read')  #.info
    # gupiao['评论']=html_text(Soup,'.reply')
    # # print(gupiao['房屋价格'])
    gupiao['标题']=html_text(Soup,'.title')
    # gupiao['作者']=html_text(Soup,'.author')
    # gupiao['最后更新'] = html_text(Soup, '.update')#update mod_time
    # print(gupiao)
    return(gupiao)

def find_all(url,long): #所有网页信息
    info=pd.DataFrame()
    for i in range(1,long+1):
        web=read_html(url+str(i)+'.html')# 第i页的网址
        print(url+str(i)+'.html')
        soup=BeautifulSoup(web,'lxml')
        gupiao_pages=gupiao_page(soup)
        info=pd.concat([info,gupiao_pages])# 进行数据的合并
        sleep(5)
    return(info)
if __name__ == "__main__":
    # n 为列表长度
    n = int(input("输入股票个数："))
    num = int(input("爬取的页数："))
    gupiao=['000875']#用作emotion
    i=0
    while(i<n):
        x=input("请输入第" + str(i+1) + "只股票的6位股票编码：")
        if len(x) == 6:
            gupiao.append(x)
        else:
            i-=1
            print("错误，请重输")
        i+=1
    for code in gupiao:
        url = 'https://guba.eastmoney.com/list,' + code + '_'
        data = find_all(url, num)
        # data.to_csv('./data/'+code+'.csv',index=False,encoding='UTF-8')
        data.to_csv('emotion' + '.csv', index=False, encoding='UTF-8', mode='a')
