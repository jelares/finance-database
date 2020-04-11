import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import sqlite3
import datetime as dt
from sklearn import metrics
import seaborn as sns

DB_FILE_LOC = '../scraping/data/stockInfo.db'
table_name = 'GS'

conn = sqlite3.connect(DB_FILE_LOC)
df = pd.read_sql_query("SELECT * FROM " + table_name, conn)
conn.commit()
conn.close()

# split into X and Y. Use everything but close to predict close
X = df[['Timestamp', 'Open', 'High', 'Low', 'Volume']].values
y = df["Close"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and fit the model
lm = LinearRegression()
model = lm.fit(X_train, y_train)

model.fit(X_train, y_train)
y_pred = lm.predict(X_test)

# plotting
f, ax = plt.subplots(figsize=(10, 6))
corr = df.corr()
hm = sns.heatmap(round(corr, 2), annot=True, ax=ax, cmap="coolwarm", fmt='.2f',
                 linewidths=.05)
f.subplots_adjust(top=0.93)
f.suptitle('Stock Correlation Heatmap', fontsize=14)

# plotting predictions
g, ax2 = plt.subplots(figsize=(10, 6))
ax2.scatter(y_test, y_pred)
ax2.set_xlabel("Truth value")
ax2.set_ylabel("Predictions")
g.suptitle("Actual values vs predictions")

prediction_dates = [dt.datetime.fromtimestamp(ts) for ts in X_test[:, 0]]
h, ax3 = plt.subplots(figsize=(10, 6))
ax3.scatter(prediction_dates, y_test)
ax3.scatter(prediction_dates, y_pred)
ax3.set_xlim(min(prediction_dates), max(prediction_dates))
ax3.set_xlabel("Timestamp")
ax3.set_ylabel("Close price ($)")
ax3.legend(('y test', 'prediction'))
h.suptitle("Timestamp vs Close price on predictions vs actual")

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.show()
