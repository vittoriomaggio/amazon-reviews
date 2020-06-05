import pandas as pd
from afinn import Afinn


reviews_df = pd.read_csv(r'./Documents/università/DataAnalytics/amazon_review/data/reviews_clean.csv')
reviews= reviews_df[:1000]
reviews_text_score = pd.DataFrame()
reviews_text_score['text'] = reviews['body']
reviews_text_score['score'] = reviews['rating']

''' Bag of words '''
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(stop_words=None, lowercase=True, max_features=5000)
bow = count_vect.fit_transform(reviews_text_score['text'])
print(bow.shape)
print(bow.toarray())


''' Split train and test '''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(
        bow.toarray(), 
        reviews_text_score.score,
        train_size=0.60, 
        random_state=1234)


'''Logistic regresion '''
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(max_iter = 200)
log_model = log_model.fit(X=X_train, y=y_train)

y_pred = log_model.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

''' Support Vector Machine '''
from sklearn import svm
svm = svm.SVC(decision_function_shape='ovr')
svm = svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))