import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import sqlite3
import datetime as dt
from sklearn import metrics

DB_FILE_LOC = '../scraping/data/stockInfo.db'
table_name = 'GS'

conn = sqlite3.connect(DB_FILE_LOC)
df = pd.read_sql_query("SELECT Timestamp, Open FROM " + table_name, conn)
conn.commit()
conn.close()

# split into X and Y. Use timestamp to predict open price
X = df["Timestamp"].values.reshape(-1, 1)
y = df["Open"].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
# print(X_test)

lm = LinearRegression()
model = lm.fit(X_train, y_train)

model.fit(X_train, y_train)
y_pred = lm.predict(X_test)

# plotting predictions
prediction_dates = [dt.datetime.fromtimestamp(ts) for ts in X_test.flatten()]
plt.xticks(rotation=25)
ax=plt.gca()
ax.set_xlim(min(prediction_dates), max(prediction_dates))
plt.scatter(prediction_dates, y_test, color='blue')
plt.scatter(prediction_dates, y_pred, color='red')
plt.xlabel("Open ($)")
plt.ylabel("Dates")
plt.legend(('y test', 'prediction'))

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.show()