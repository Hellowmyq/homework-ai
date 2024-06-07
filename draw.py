import pandas as pd
import numpy as np
from matplotlib import pyplot as plt, ticker
import mpl_finance as mpf
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体显示
def format_date(x, pos=None):
    if x < 0 or x > len(df['date']) - 1:
        return ''
    return df['date'][int(x)]

def draw(code):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(15, 10))
    fig.suptitle(f"股票 {code} 的 K 线图和成交量", fontsize=16, y=0.98)
    ax1, ax2 = axes.flatten()
    mpf.candlestick2_ochl(ax1, df["open"], df["close"], df["high"], df["low"], width=0.6, colorup='r',colordown='green',alpha=1.0)

    df["SMA5"] = df["close"].rolling(5).mean()
    df["SMA10"] = df["close"].rolling(10).mean()
    df["SMA30"] = df["close"].rolling(30).mean()
    ax1.plot(np.arange(0, len(df)), df['SMA5'], label='5日均线')  # 绘制5日均线，并添加标签
    ax1.plot(np.arange(0, len(df)), df['SMA10'], label='10日均线')  # 绘制10日均线，并添加标签
    ax1.plot(np.arange(0, len(df)), df['SMA30'], label='30日均线')  # 绘制30日均线，并添加标签

    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    red_pred = np.where(df["close"] > df["open"], df["vol"], 0)
    blue_pred = np.where(df["close"] < df["open"], df["vol"], 0)
    ax2.bar(np.arange(0, len(df)), red_pred, facecolor="red",label='上涨成交量')
    ax2.bar(np.arange(0, len(df)), blue_pred, facecolor="blue",label='下跌成交量')

    ax1.legend()
    ax2.legend()

    plt.savefig(f'pic/{code}.png')
    #显示出来
    # plt.show()

if __name__ == "__main__":
    gupiao = ['000737', '600016', '600036', '601919','000767','002594','300001','605499','000777','000788']
    for code in gupiao:
            df = pd.read_csv("./data3/"+code+".csv")
            draw(code)