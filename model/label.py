import pandas as pd
from snownlp import SnowNLP

def get_sentiment_cn(text):
    s = SnowNLP(text)
    return s.sentiments
if __name__ == "__main__":
    df = pd.read_csv('emotion.csv')
    df = df[~df['标题'].str.contains('？')]
    df = df[~df['标题'].str.contains('\?')]
    df = df[~df['标题'].str.contains('吗')]
    df = df[~df['标题'].str.contains('怎么')]
    df = df[~df['标题'].str.contains('哪里')]
    df['情绪'] = df.标题.apply(get_sentiment_cn)>0.5
    df['情绪分数'] = df.标题.apply(get_sentiment_cn)
    df.to_csv('label' + '.csv', index=False, encoding='UTF-8')
