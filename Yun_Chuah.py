from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

# scrape the website below to retrieve the top 5 countries with the highest GDPs. Calculate the GDP per capita
# by dividing the GDP by the population. You can perform the calculation in Python natively or insert the code
# in excel that will perform the calculation in Excel by each row. DO NOT scrape the GDP per capita from the
# webpage, make sure you use your own calculation.

#Calc GDP per capita: GDP/Population
#no. country 
#gdp $
#population
#gdp per capita $

### REMEMBER ##### - your output should match the excel file (GDP_Report.xlsx) including all formatting.

webpage = 'https://www.worldometers.info/gdp/gdp-by-country/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()			
soup = BeautifulSoup(webpage, 'html.parser')
title = soup.title
print(title.text)

workbook = xl.Workbook()

worksheet = workbook.active

worksheet.title = 'Countries with highest GDPs'

worksheet['A1']='No. Country'
worksheet['B1']='GDP'
worksheet['C1']='Population'
worksheet['D1']='GDP Per Capita'

table_rows = soup.findAll('tr')

for i in range(1,6):
    td = table_rows[i].findAll('td')
    no = td[0].text
    name = td[1].text
    gdp = int(float(td[2].text.replace(',','').replace('$','')))
    format_gdp = '{:,}'.format(gdp)
    population = int(td[5].text.replace(',',''))
    format_population = '{:,}'.format(population)
    
    gdp_per_capita = round((gdp/population),2)
    format_gdp_per_capita = '{:,}'.format(gdp_per_capita)

    worksheet['A'+str(i+1)]=(no + ' ' + name)
    worksheet['B'+str(i+1)]=('$' + str(format_gdp))
    worksheet['C'+str(i+1)]=format_population
    worksheet['D'+str(i+1)]= ('$' + str(format_gdp_per_capita))

worksheet.column_dimensions['A'].width = 20
worksheet.column_dimensions['B'].width = 20
worksheet.column_dimensions['C'].width = 25

header_font = Font(size=15, bold=True)

for cell in worksheet[1:1]:
    cell.font = header_font

workbook.save('TopGDPs.xlsx')



    





