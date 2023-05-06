from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
import keys
from twilio.rest import Client
import sys


url = 'https://www.coingecko.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)

client = Client(keys.accountSID, keys.authtoken)

TwilioNumber = "+14072891580"
mycellphone = "+13038804356"

tables = soup.findAll('table')
updated_tables = tables[0]
rows = updated_tables.findAll('tr')

workbook = xl.Workbook()
worksheet = workbook.active
worksheet.title = "Top 5 Cryptocurrencies"

Font1 = Font(name= 'Times New Roman', size=14, bold=True, underline='single')

worksheet['A1'] = 'Number'
worksheet['A1'].font = Font1
worksheet['B1'] = 'Type'
worksheet['B1'].font = Font1
worksheet['C1'] = 'Current Price'
worksheet['C1'].font = Font1
worksheet['D1'] = 'Percent change \n within 24 hours'
worksheet['D1'].font = Font1
worksheet['E1'] = 'Price based \n on change'
worksheet['E1'].font = Font1

worksheet.column_dimensions['A'].width = 15
worksheet.column_dimensions['B'].width = 15
worksheet.column_dimensions['C'].width = 20
worksheet.column_dimensions['D'].width = 20
worksheet.column_dimensions['E'].width = 20

for cell in worksheet[2:2]:
    cell.font = Font(name="Times New Roman")
for cell in worksheet[3:3]:
    cell.font = Font(name="Times New Roman")
for cell in worksheet[4:4]:
    cell.font = Font(name="Times New Roman")
for cell in worksheet[5:5]:
    cell.font = Font(name="Times New Roman")
for cell in worksheet[6:6]:
    cell.font = Font(name="Times New Roman")



for row in range(1, 6):
    td = rows[row].findAll('td')
    num = td[1].text
    crypto = td[2].text + ""
    price = float(td[3].text.replace(",", "").replace("$", ""))
    perc_chg = float(td[5].text.replace("%", ""))
    total_change = round((price + perc_chg), 2)
    new_price = int(total_change - price)
    if new_price <= -5 or new_price >= 5:
        text = client.messages.create(to=mycellphone, from_=TwilioNumber, body="There has been an increase or decrease of $5 or more.")
        print(text.status)

    worksheet['A' + str(row+1)] = num
    worksheet['B' + str(row+1)] = crypto
    worksheet['C' + str(row+1)] = '$' + str(format(price, ',.2f'))
    worksheet['D' + str(row+1)] = str(format(perc_chg, ',.2f') + '%') 
    worksheet['E' + str(row+1)] = '$' + format(total_change, ',.2f')

    workbook.save("Cryptoreport.xlsx")