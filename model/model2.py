import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report, r2_score

# 假设您有一个包含文本特征和目标值的CSV文件
# 读取数据集
data = pd.read_csv('label.csv')

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data['标题'], data['情绪分数'], test_size=0.3, random_state=42)

# 使用TF-IDF向量化器
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 使用线性回归模型
clf = LinearRegression()
clf.fit(X_train_tfidf, y_train)

# 预测
y_pred = clf.predict(X_test_tfidf)
for title, prediction in zip(data["标题"], y_pred):
    print(f'标题: "{title}" 预测得分: {prediction}')
# 评估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# 保存模型
joblib.dump(clf, 'model2.pkl')

# 保存TF-IDF向量化器
joblib.dump(vectorizer, 'vectorizer2.pkl')
