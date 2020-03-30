import requests
import csv
url = "https://query1.finance.yahoo.com/v7/finance/download/ABT?period1=1553930588&period2=1585552988&interval=1d" \
      "&events=history "

r = requests.get(url) # create HTTP response object

decoded_content = r.content.decode('utf-8')
cr = csv.reader(decoded_content.splitlines(), delimiter=',')
for row in list(cr):
    print(row)