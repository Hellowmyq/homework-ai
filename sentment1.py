# 加载模型
import joblib
import pandas as pd

def model(data):
    loaded_clf = joblib.load('model/model.pkl')
    # 加载TF-IDF向量化器
    loaded_vectorizer = joblib.load('model/vectorizer.pkl')
    # 使用加载的向量化器转换新数据
    data_t = loaded_vectorizer.transform(data)
    # 使用加载的模型进行预测
    predict = loaded_clf.predict(data_t)
    # 打印预测结果
    # for title, prediction in zip(data, predict):
    #     print(f'标题: "{title}" 预测得分: {prediction}')
    # print(predict)
    return predict
if __name__ == "__main__":
    gu = '000737'
    df=pd.read_csv('./data2/' + gu + '.csv')
    df['情绪']=model(df.标题)
    # print(model(["这家公司前景看好，业绩增长强劲，值得投资。",]))