import src.databaseManager.Utilities as util
from src.scraping.scraper import Scraper

# util examples
# DATABASE_URL = "fakeDatabase.db"
# types = [("col1", "TEXT"), ("col2", "REAL"), ("col3", "REAL")]
# # table creation
# util.create_table("my_table", ["col1", "col2", "col3"], types, DATABASE_URL, True)
# # table data entry
# util.data_entry("my_table", ["text", "1", "2"], types, DATABASE_URL, True)
# # query is specific to stocks
#
# # plot example
# data = Scraper.scrape("GS", ["3-17-2019", "3-20-2020"], True)
# util.create_plot("Goldman Sachs", data)

# updating database example
DATABASE_URL = "stocksInfo.db"
data = Scraper.scrape("GS", ["2-17-2005", "3-20-2020"], True)
Scraper.update_symbol("GS", ["2-17-2005", "3-20-2020"], DATABASE_URL, "test_scraper_GS_01", False)