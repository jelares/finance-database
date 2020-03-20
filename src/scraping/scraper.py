from bs4 import BeautifulSoup
import requests
import datetime


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
        Get stock data from Yahoo for a company with symbol `symbol` between a time `interv
        @param symbol: The stock ticker for a given company
        @param interval: A tuple or array of date values in the format 'm-d-Y'
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

                stock_data.append({"date": stock_data_soup[0].text,
                                   "open": stock_data_soup[1].text,
                                   "high": stock_data_soup[2].text,
                                   "low": stock_data_soup[3].text,
                                   "close": stock_data_soup[4].text,
                                   "adj_close": stock_data_soup[5].text,
                                   "volume": stock_data_soup[6].text
                                   })

        return stock_data


data = Scraper.scrape("GS", ["3-10-2020", "3-20-2020"], True)
print(data)