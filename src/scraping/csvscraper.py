import sys
sys.path.append('../')
import requests
import csv
from tkinter import *
import datetime
import time
import databaseManager.Utilities as util


'''
Standalone script to update database with certain stock
'''

DATABASE_URL = "data/stockInfo.db"


def isBlank(string):
    if string and string.strip():
        # myString is not None AND myString is not empty or blank
        return False
    # myString is None OR myString is empty or blank
    return True


# GUI
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.symbol = None
        self.startDate = None
        self.endDate = None
        self.progressLabel = None
        self.init_window()

    # Creation of init window
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=True)

        titleFrame = Frame(self)
        titleFrame.pack(fill=BOTH)
        Label(titleFrame, text="Stock Updater").pack()

        frame = Frame(self)
        frame.pack(fill=BOTH)

        Label(frame, text="Symbol").grid(row=0)
        self.symbol = Entry(frame)
        self.symbol.grid(row=0, column=1)
        Label(frame, text="Start Date").grid(row=1)
        self.startDate = Entry(frame)
        self.startDate.grid(row=1, column=1)
        Label(frame, text="End Date").grid(row=2)
        self.endDate = Entry(frame)
        self.endDate.grid(row=2, column=1)

        submitFrame = Frame(self)
        submitFrame.pack(fill=BOTH, expand=True)
        Button(submitFrame, text="Submit", command=self.submit).pack(side=LEFT, padx=5)
        self.progressLabel = Label(submitFrame, text="Progress Label")
        self.progressLabel.pack(side=RIGHT)


    def submit(self):
        self.progressLabel["text"] = "Stock updating..."
        url = "https://query1.finance.yahoo.com/v7/finance/download/"

        begin_date = 0 if isBlank(self.startDate.get()) else round(
            datetime.datetime.strptime(self.startDate.get().strip(), '%m-%d-%Y').timestamp())
        end_date = round(time.time()) if isBlank(self.endDate.get()) else round(
            datetime.datetime.strptime(self.endDate.get().strip(), '%m-%d-%Y').timestamp())

        # build url
        url += str(self.symbol.get().strip()) + "?period1=" + str(begin_date) + "&period2=" + str(
            end_date) + "&interval=1d&events=history"

        # send request
        r = requests.get(url)  # create HTTP response object
        decoded_content = r.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data = list(cr)[1:]     # first line is header

        columns = {'Timestamp': "REAL",
                   'Open': "REAL",
                   'High': "REAL",
                   'Low': "REAL",
                   'Close': "REAL",
                   'Adj_Close': "REAL",
                   'Volume': "REAL"}

        table_name = self.symbol.get().strip().upper()
        util.create_table(table_name, list(columns.keys()), list(columns.items()), DATABASE_URL, True)

        for row in data:
            row_entry = [str(el) for el in row]
            row_entry[0] = str(datetime.datetime.strptime(row[0], '%Y-%m-%d').timestamp())   # change to unix timestamp
            util.data_entry(table_name, row_entry, list(columns.items()), DATABASE_URL, True)

        self.progressLabel["text"] = "Finished updating database!"


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()