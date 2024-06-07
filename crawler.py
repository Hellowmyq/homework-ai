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
    # select寻找文档中相应标签，得到集合[],迭代获取内容
    # 其中'#'为id标签，'.'为class标签
    # get_text()# 获取文本值
    return([w.get_text() for w in info.select(word)])#跟find差不多
    # return([w.text for w in info.select(word)])也行

def gupiao_page(Soup):  #单个网页信息
    gupiao=pd.DataFrame()
    gupiao['阅读']=html_text(Soup,'.read')  #.info
    gupiao['评论']=html_text(Soup,'.reply')
    gupiao['标题']=html_text(Soup,'.title')
    # gupiao['作者']=html_text(Soup,'.author')
    gupiao['最后更新'] = html_text(Soup, '.update')#update mod_time
    # print(gupiao)
    return(gupiao)

def find_all(url,long): #所有网页信息
    info=pd.DataFrame()
    for i in range(5,long+5):
        web=read_html(url+str(i)+'.html')# 第i页的网址
        print(url+str(i)+'.html')
        soup=BeautifulSoup(web,'lxml')
        gupiao_pages=gupiao_page(soup)
        info=pd.concat([info,gupiao_pages])# 进行数据的合并
        sleep(10)
    return(info)
def crawer():
    # n 为列表长度
    n = int(input("输入股票个数："))
    num = int(input("爬取的页数："))
    gupiao=['002594']#用作emotion
    # gupiao = ['000737']
    # gupiao = ['600016', '600036', '601919']
    # gupiao = ['000767', '002594', '300001', '605499', '000777', '000788']
    # gupiao = ['301205','603178','002855','000628','301096','300114','300765','002229']
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
        # data.to_csv('./data/'+code+'.csv',index=False,encoding='UTF-8',mode='a')
        data.to_csv('./data/' + code + '.csv', index=False, encoding='UTF-8')
    return gupiao
if __name__ == "__main__":
    crawer()