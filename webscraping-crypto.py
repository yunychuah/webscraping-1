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
from twilio.rest import Client

webpage = 'https://www.cryptocurrencychart.com/'

page = urlopen(webpage)

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

workbook = xl.Workbook()

worksheet = workbook.active

worksheet.title = 'Top 5 Cyrptocurrencies'

worksheet['A1']='Name & Symbol'
worksheet['B1']='Current Price'
worksheet['C1']='% Change in 24 hrs'
worksheet['D1']='Corresponding Price'

crypto_rows = soup.findAll('tr')

#scrape from webpage 
for i in range(1,6):
    #finding td tags
    td = crypto_rows[i].findAll('td')
    #read from webpage & write to new file
    name_symbol = td[1].text
    current_price = float(td[2].text.replace(',','').replace('$','').replace('.',''))
    format_current_price= '{:,.2f}'.format(current_price)
    change =float(td[4].text.replace('-','').replace('%',''))
    
    #calculation of price change
    if '-' in td[4].text:
        new_price = round(current_price*((change*-1)/100),2)
        format_new_price= '{:,.2f}'.format(new_price)
    else:
        new_price = round(current_price*(1+(change/100)),2)
        format_new_price= '{:,.2f}'.format(new_price)


    #write to excel 
    worksheet['A'+str(i+1)]=name_symbol
    worksheet['B'+str(i+1)]=('$' + str(format_current_price))
    worksheet['C'+str(i+1)]=(str(change) + '%')
    worksheet['D'+str(i+1)]= ('$' + str(format_new_price))

    #send message twilio
    phone = '+4084208855'
    twilionumber = '+15076836741'
    if 'BTC' or 'ETH' in name_symbol:
        if new_price-current_price < -5 or new_price-current_price > 5:
            textmsg = Client.messages.create(to=phone, from_=twilionumber, body= f'Alert {name_symbol} has changed over $5')
            
worksheet.column_dimensions['A'].width = 20
worksheet.column_dimensions['B'].width = 20
worksheet.column_dimensions['C'].width = 25

header_font = Font(size=15, bold=True)

for cell in worksheet[1:1]:
    cell.font = header_font

workbook.save('TopCryptos.xlsx')