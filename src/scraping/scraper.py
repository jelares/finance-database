from bs4 import BeautifulSoup
import requests
import datetime
import databaseManager.Utilities as util

class Scraper:
    """
    A static class for scraping functions
    """

    @staticmethod
    def get_symbol(symbol):
        """
        Get a company name given a stock symbol
        @param symbol: The stock ticker for a given company
        @return: The company name associated with `symbol`
        """
        symbol_list = requests.get("http://chstocksearch.herokuapp.com/api/{}".format(symbol)).json()

        for x in symbol_list:
            if x['symbol'] == symbol:
                return x['company']

        return ""

    @staticmethod
    def scrape(symbol, interval=None, debug=False):
        """
        Get stock data from Yahoo for a company with symbol `symbol` between a time `interval`

        @param symbol: The stock ticker for a given company
        @param interval: A tuple or array of date values in the format 'm-d-Y'. If None is provided, will
        @param debug: A boolean flag whether to print debug statements or not
        @return: An array of dictionaries representing rows of data. Ex:
            [{'date': 'Mar 19, 2020', 'open': '137.38', 'high': '152.49', 'low': '130.85', 'close': '149.49', 'adj_close': '149.49', 'volume': '6,543,800'},
             {'date': 'Mar 18, 2020', 'open': '150.00', 'high': '155.97', 'low': '135.41', 'close': '140.02', 'adj_close': '140.02', 'volume': '9,543,200'},
            ]
        """

        if not symbol:
            print("Invalid request! No stock symbol provided")
            return

        url = ""

        if interval is None:
            url = "https://finance.yahoo.com/quote/GS/history?p=" + symbol
        else:
            if interval[0] is None or interval[1] is None:
                print("Invalid request! One of the intervals is None")
                return

            # convert date strings into epoch times
            begin_date = round(datetime.datetime.strptime(interval[0], '%m-%d-%Y').timestamp())
            end_date = round(datetime.datetime.strptime(interval[1], '%m-%d-%Y').timestamp())

            url = "https://finance.yahoo.com/quote/" + str(symbol) + "/history?period1=" + str(
                begin_date) + "&period2=" + str(end_date) + "&interval=1d&filter=history&frequency=1d"

        if debug:
            print("Querying URL: " + url)

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        stocks = soup.findAll('tr', class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
        stock_data = []  # output

        if stocks:
            for stock in stocks:
                stock_data_soup = stock.find_all('span')

                if len(stock_data_soup) > 2:  # want to exclude "Dividend" entries
                    stock_data.append({"date": stock_data_soup[0].text,
                                       "open": stock_data_soup[1].text,
                                       "high": stock_data_soup[2].text,
                                       "low": stock_data_soup[3].text,
                                       "close": stock_data_soup[4].text,
                                       "adj_close": stock_data_soup[5].text,
                                       "volume": stock_data_soup[6].text
                                       })

        return stock_data

    @staticmethod
    def update_symbol(symbol, interval, database_path, table_name, debug=False):
        """
        Updates the table table_name at the database specified by database_path
        with all the data on Yahoo finance for symbol within the time specified
        by interval

        :param symbol: The stock ticker for a given company
        :param interval: A tuple or array of date values in the format 'm-d-Y'.
        :param database_path: rel path of database
        :param table_name: name of table in which we will input data
        :param debug: A boolean flag whether to print debug statements or not
        """
        stock_data = Scraper.scrape(symbol, interval)

        if debug:
            print(stock_data)

        values = ['symbol', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']

        # list of tuples (col_name, data_type) strings
        table_data = [
            ("symbol", "TEXT"),
            ("date", "TEXT"),
            ("open", "REAL"),
            ("high", "REAL"),
            ("low", "REAL"),
            ("close", "REAL"),
            ("adj_close", "REAL"),
            ("volume", "REAL")
        ]

        util.create_table(table_name, values, table_data, database_path, debug)

        for row in stock_data:

            # values is a list of string literal values for this row/date
            values = [
                symbol,
                row["date"],
                row["open"],
                row["high"],
                row["low"],
                row["close"],
                row["adj_close"],
                row["volume"]
            ]

            util.data_entry(table_name, values, table_data, database_path, debug)


# Testing Methods for scraper:

DATABASE_URL = "../../database/stocksInfo.db"

# data = Scraper.scrape("GS", ["2-17-2005", "3-20-2020"], True)
# print(data)

# Scraper.update_symbol("GS", ["2-17-2005", "3-20-2020"], DATABASE_URL, "test_scraper_GS_01", False)

data = Scraper.scrape("GS", ["2-17-2019", "3-20-2020"], True)
print(data)
