from bs4 import BeautifulSoup
import requests
import csv

stock_information = {}
csv_file = open('tech_companies.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Symbol', 'Company', 'Price', 'change', 'Percent Change', 'Market Cap'])

offset = 0
url = "https://finance.yahoo.com/screener/predefined/ms_technology?count=100&offset=0"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
stocks = soup.find_all(True, {'class':
                                  ['simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)',
                                   'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc($altRowColor)']
                              })

while (stocks != []):
    for stock in stocks:
        symbol = stock.find(True, {'class':['Fw(600)']}).text
        name = stock.find(True, {'class':['Va(m) Ta(start) Px(10px) Fz(s)']}).text
        pricecap = stock.find_all(True, {'class':['Trsdu(0.3s)']})
        price = pricecap[0].text
        changes = stock.find_all(True, {'class':['Trsdu(0.3s) Fw(600) C($dataRed)', 'Trsdu(0.3s) Fw(600) C($dataGreen)', 'Trsdu(0.3s) Fw(600)']})
        change = changes[0].text
        percent_change = changes[1].text

        try:
            market_cap = pricecap[3].text
        except:
            market_cap = "N/A"

        print(symbol, name, price, change, percent_change, market_cap)
        csv_writer.writerow([symbol, name, price, change, percent_change, market_cap])

    # Getting next 100 results
    offset += 100
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?count=100&offset=" + str(offset)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    stocks = soup.find_all(True, {'class':
                                      [
                                          'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)',
                                          'simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc($altRowColor)']
                                  })

csv_file.close()