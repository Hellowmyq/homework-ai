import imageio
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from pyecharts import options as opts
from pyecharts.charts import Bar


plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def visual1(code):
    path = "./data2/"+code+".csv"
    text = open(path,encoding='UTF-8').read()
    # print(text)
    mylist=list(text)
    word_list=[" ".join(jieba.cut(sentence)) for sentence in mylist]
    new_text=''.join(word_list)
    # 优化
    con_words=[x for x in jieba.cut(new_text) if len(x)>=2]
    frequency=Counter(con_words)
    with open('stopwords.txt', 'r', encoding='utf-8') as file:
        stopwords = file.readlines()

    # 去除停用词表中的换行符
    stopwords = [word.strip() for word in stopwords]
    # 从词频计数器中移除停用词
    i=0
    for word in stopwords:
        i+=1
        del frequency[str(i)]
        del frequency[word]
    # print(frequency)
    frequencies=dict(frequency)
    # 词云图
    maskImg = imageio.imread('img_2.png')


    # 创建词云
    word_cloud = WordCloud(font_path="msyh.ttc",
                           width=1000,
                           height=700,
                           background_color='white',
                           max_words=200,
                           mask=maskImg,
                           max_font_size=90,
                           min_font_size=10).fit_words(frequencies)

    #fit_words 根据词频字典生成
    plt.figure()
    plt.imshow(word_cloud)
    plt.axis('off')
    # plt.show()
    word_cloud.to_file('pic/'+code+'.jpg')

    frequency=frequency.most_common(10)
    frequencies=dict(frequency)

    # 创建柱状图
    bar = Bar()
    bar.add_xaxis(list(frequencies.keys()))
    bar.add_yaxis("词频", list(frequencies.values()))

    # 设置全局配置选项
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="词频前10的词汇"),
        toolbox_opts=opts.ToolboxOpts(),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(frequencies.values()),
            max_=max(frequencies.values()),
        )
    )
    bar.render('html/' + code + 'bar_chart.html')

def visual2(gu,l1=[10],l2=[20]):

    # 创建DataFrame
    df = pd.DataFrame({'股票代码': gu,'得分': l1,'积极情绪占比': l2})
    # 设置颜色
    # colors = plt.cm.viridis(np.linspace(0, 1, len(gupiao)))
    colors = ['#ff9999', '#66b3ff']
    # 条形图
    df.plot(x='股票代码',y=['得分','积极情绪占比'],kind='barh',figsize=(10, 6),color=colors)
    plt.title('股票数据')
    plt.xlabel('值')
    plt.ylabel('股票代码')
    plt.grid(True, linestyle='--', alpha=0.7)
    # 显示图表
    plt.savefig('pic/情绪分析.png')
    # plt.show()


def visual(gu,l1,l2):
    visual1(gu)
    visual2(gu,l1,l2)
if __name__ == "__main__":
    gu = '000737'
    visual(gu)