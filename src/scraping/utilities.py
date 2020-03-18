import sqlite3

'''
Utilities file to insert a certain stock into the stocks database
'''


def create_table(table_name):
    conn = sqlite3.connect("../database/stocksInfo.db")
    c = conn.cursor()

    create_info = (
            "CREATE TABLE IF NOT EXISTS " + table_name +
            "(company TEXT, date_stamp TEXT, stock_price REAL, "
            "market_capitalization REAL)"
    )

    c.execute(create_info)

    c.close()
    conn.close()


def data_entry(table_name, company, date_stamp, stock_price,
               market_capitalization):
    conn = sqlite3.connect("../database/stocksInfo.db")
    c = conn.cursor()

    stock_info = (
            "INSERT INTO " + table_name + " VALUES('" + company + "', '" +
            date_stamp + "', " + str(stock_price) + ", " +
            str(market_capitalization) + ")"
    )

    c.execute(stock_info)
    c.close()
    conn.close()

