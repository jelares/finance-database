from sklearn import svm
from sklearn import datasets
from joblib import dump, load

''' Showing classification below: '''

digits = datasets.load_digits()
# data is a 2d array of (n_samples, n_features)

clf = svm.SVC(gamma=0.001, C=100.)  # Support Vector Classification
clf.fit(digits.data[:-1], digits.target[:-1])

# save a model with Pickle
dump(clf, 'digitsClassifier.joblib')
clf2 = load('digitsClassifier.joblib')

prediction = clf2.predict(digits.data[-1:])

print("Predicted class: " + str(prediction[0]))


''' Showing regression below '''
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
Y = np.dot(X, np.array([1,2])) + 3

# print(X)
# print(Y)
reg = LinearRegression().fit(X, Y)
score = reg.score(X, Y)
print("Score: " + str(score))
# print(reg.coef_)
# print(reg.intercept_)

pred = reg.predict(np.array([[3, 5]]))
print("Prediction: " + str(pred[0]))