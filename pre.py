import pandas as pd


def pre(gu):
    df = pd.read_csv('./data/' + gu + '.csv')
    df = df[~df['标题'].str.contains('？')]
    df = df[~df['标题'].str.contains('\?')]
    df = df[~df['标题'].str.contains('吗')]
    df = df[~df['标题'].str.contains('怎么')]
    df = df[~df['标题'].str.contains('哪里')]
    df['最后更新'] = pd.to_datetime(df['最后更新'], format='%m-%d %H:%M', errors='coerce')
    # 丢弃包含空日期时间的行
    df.dropna(subset=['最后更新'], inplace=True)
    df['最后更新'] = df['最后更新'].dt.date
    df = df.sort_values(by=['最后更新', '阅读', '评论'], ascending=False)
    df[['标题']].to_csv('./data2/' + gu + '.csv', index=False, encoding='UTF-8')
    df.to_csv('./data1/' + gu + '.csv', index=False, encoding='UTF-8')

if __name__ == "__main__":
    gupiao = '000737'
    pre(gupiao)
