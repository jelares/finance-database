# import databaseManager.Utilities as util
import Utilities as util
# import scrapeADT as scrape

'''
Test File for Utility functions
'''

DATABASE_URL = "../../database/stocksInfo.db"

table_name = "stocks"
columns = {"company": "TEXT",
           "date_stamp": "TEXT",
           "stock_price": "REAL",
           "market_capitalization": "REAL"}

util.create_table(table_name, list(columns.keys()), list(columns.values()), DATABASE_URL, True)

curr_vals = ["Goldman", "3-19-2020", "50", "500"]
util.data_entry(table_name, curr_vals, columns, DATABASE_URL, True)

curr_vals = ["Goldman", "3-20-2020", "52", "510"]
util.data_entry(table_name, curr_vals, columns, DATABASE_URL, True)

curr_vals = ["Goldman", "3-21-2020", "51", "509"]
util.data_entry(table_name, curr_vals, columns, DATABASE_URL, True)

# Example for how to query and plot
data = util.data_query(table_name, "Goldman", DATABASE_URL, [None, "3-21-2020"], True)

dates = [row[1] for row in data]
stock_prices = [row[2] for row in data]
util.create_scatterplot("Goldman", dates, stock_prices)