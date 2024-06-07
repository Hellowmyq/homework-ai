import pandas as pd
from matplotlib import pyplot as plt

import crawler
import Visual
from pre import pre
from sentment import model
from tushare1 import tu

l1 = []
l2 = []
def analyze(gu):
    df=pd.read_csv('./data1/' + gu + '.csv')
    df['情绪']= model(df.标题)
    # 定义一个新的变量来表示长度
    length = int(len(df) * 0.01)
    for i in range(length):
        for j in range(length-i):
            current_row = df.iloc[i]
            # 将当前行的数据添加到数据框中
            df.loc[len(df)] = current_row
    # print(df['情绪'])
    a=df['情绪'].mean()
    b=len(df[df['情绪']>0.7])/len(df)
    l1.append(a)
    l2.append(b)
    # df.to_csv('./data1/' + gu + '.csv')
        # print(a,b)
if __name__ == "__main__":

    gupiao = ['000737', '600016', '600036', '601919','000767',
              '002594','300001','605499','000777','000788']
        # ,'301205','603178','002855','000628','301096','300114','300765','002229']
    # gupiao = crawler.crawer()
    df = pd.DataFrame()
    df["code"] = gupiao


    for gu in gupiao:
        pre(gu)
        analyze(gu)
        # Visual.visual1(gu)

    Visual.visual2(gupiao,l1,l2)
    change = tu(gupiao)
    df["sign"] = [value>0.7 for value in l1]
    df["truth"] = [value>0 for value in change]
    df["change"] = change
    df.to_csv("结果.csv",index=False)

    matched_rows = len(df[df["sign"] == df["truth"]])
    total_rows = len(df)
    r = matched_rows / total_rows
    print("正确率：",r)
# 晚上十点多，那个网站可能是在更新数据，得到的数据会不稳定，不对好像是被ban了,数据能爬出来，但是链接看不了。
# 柱状和折线图考虑子弹图(实际与目标可以结合一下)，复合图，词云
# 动态图*
#可以和实际数据进行对比，实际上涨和下跌