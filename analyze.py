from math import log
import pandas as pd
from matplotlib import pyplot as plt
import crawler
import Visual
from pre import pre
from sentment1 import model
from tushare1 import tu

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体显示
l1 = []
l2 = []

def analyze(gu):
    df=pd.read_csv('./data2/' + gu + '.csv')
    df['情绪']= model(df.标题)
    # print(df['情绪'])
    positive = len(df[df['情绪']])
    negative = len(df[~df['情绪']])
    a=log((positive+1)/(negative+1))
    # # 计算a的最小值和最大值
    # min_a = log(1 / (negative + 1))
    # max_a = log((positive + 1) / 1)
    # # 归一化a
    # print(a,min_a,max_a)
    # print(positive,negative)
    # a = (a - min_a) / (max_a - min_a)
    b = positive/len(df)
    l1.append(a)
    l2.append(b)
    # df.to_csv('./data2/' + gu + '.csv')
    # print(a,b)
if __name__ == "__main__":

    gupiao = ['000737', '600016', '600036', '601919','000767','002594','300001','605499','000777','000788']
    # gupiao = crawler.crawer()
    df = pd.DataFrame()
    df["code"] = gupiao


    for gu in gupiao:
        pre(gu)
        analyze(gu)
        # Visual.visual1(gu)
    Visual.visual2(gupiao,l1,l2)
    change = tu(gupiao)
    df["sign"] = [value>0 for value in l1]
    df["truth"] = [value>0 for value in change]
    df["change"] = change
    df.to_csv("结果2.csv",index=False)

    matched_rows = len(df[df["sign"] == df["truth"]])
    total_rows = len(df)
    r = matched_rows / total_rows
    print("正确率：",r)
