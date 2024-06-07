import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

# def model():
data = pd.read_csv('label.csv')
df = pd.DataFrame(data)

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df['标题'], df['情绪'], test_size=0.1, random_state=4)

# 使用TF-IDF向量化器
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 使用多项式朴素贝叶斯分类器
clf = MultinomialNB()
clf.fit(X_train_tfidf, y_train)

# 预测
y_pred = clf.predict(X_test_tfidf)

# 评估
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=1)  # 设置zero_division参数为1
for title, prediction in zip(df["标题"], y_pred):
    print(f'标题: "{title}" 预测得分: {prediction}')
print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')


# 保存模型
joblib.dump(clf, 'model.pkl')

# 保存TF-IDF向量化器
joblib.dump(vectorizer, 'vectorizer.pkl')

