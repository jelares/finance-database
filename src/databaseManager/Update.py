import databaseManager.Utilities as util

'''

'''

DATABASE_URL = "../../database/stocksInfo.db"

table_name = "stocks"
values = ["company", "date_stamp", "stock_price", "market_capitalization"]
data_types = ["TEXT", "TEXT", "REAL", "REAL"]

util.create_table(table_name, values, data_types, DATABASE_URL, True)

curr_vals = ["Goldman", "3-19-2020", "50", "500"]
util.data_entry(table_name, curr_vals, data_types, DATABASE_URL, True)
