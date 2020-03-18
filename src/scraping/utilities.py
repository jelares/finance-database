import sqlite3

'''
Utilities file to insert a certain stock into the stocks database
'''

conn = sqlite3.connect("../database/stocksInfo.db")
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stocks(company TEXT, dateStamp "
              "TEXT, stock_price REAL, market_capitalization REAL")


def data_entry(company, dateStamp, stock_price, market_capitalization):
    c.execute("INSERT INTO goldmanSachs VALUES('", company, "', '", dateStamp,
              "', ", str(stock_price), ", ", str(market_capitalization), ")")
    c.close()
    conn.close()

