#find crypto website, scrape top 5 currencies
#create excel sreadsheet, display name of 
#currency, symbol, current price, % change in 
#last 24 hous and corresponding price(based on
#% change)
#for bitcoin and ethereum, program needs to alert
#you via text if value increase or decrease within
#$5 of current value
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)

soup = BeautifulSoup(page, 'html.parser')
title = soup.title

print(title.text)

workbook = xl.Workbook()

worksheet = workbook.active

worksheet.title = 'Tope 5 Cyrptocurrencies'

worksheet['A1']='Name'
worksheet['B1']='Symbol'
worksheet['C1']='Current Price'
worksheet['D1']='%change in 24hrs'
worksheet['E1']='Price based on change' #what is this? calclate?

crypto_rows = soup.findAll('tr')

#scrape from webpage 
for i in range(1,5):
    #finding td tags
    td = crypto_rows[i].findAll('td')
    #read from webpage & write to new file
    name = td[1].text
    symbol =td[2].text
    current_price = float(td[3].text.replace(',','').replace('$',''))
    percent_change =int(td[4].text.replace(','''))
    
    new_price = current_price*(1-percent_change)

#write to excel 

workbook.save('TopCryptos.xlsx')
