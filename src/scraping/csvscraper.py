import requests
import csv
from tkinter import *

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

        print(self.symbol.get())



root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()

# url = "https://query1.finance.yahoo.com/v7/finance/download/ABT?period1=1553930588&period2=1585552988&interval=1d" \
#       "&events=history "
#
# r = requests.get(url) # create HTTP response object
#
# decoded_content = r.content.decode('utf-8')
# cr = csv.reader(decoded_content.splitlines(), delimiter=',')
# for row in list(cr):
#     print(row)
