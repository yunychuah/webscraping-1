# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)

#this is a library used to make a request 
from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup #beautifulsoup is a library


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#request w url that we had,dont need to know why just do it
req = Request(url, headers=headers) 

#will read the webpage
webpage = urlopen(req).read()

#make a soup object 
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

#finding all the tr tag
#findAll is a func from beautifulsoup that lets you look 
#for specific things
table_rows = soup.findAll('tr')
#print(table_rows[:20]) #finds firs 20 elements in the list

state_death_ratio = ''
state_best_testing = ''
state_worst_testing = ''
high_death_ratio = 0.0
high_test_ratio = 0.0
low_test_ratio = 100.0

for row in table_rows[2:52]:
    td = row.findAll("td")
    #print(td) #looks for all td tags within that first row
    state = td[1].text.strip('\n') #extracts table data from 2nd td 
    #which is california, first td refers to the USA total row
    total_cases = int(td[2].text.replace(",",""))
    #you put replace to get rid of comma b/c you can't
    #divide the comma later on so it's saying replace the 
    #, with empty "", and then convert to integer
    total_deaths = int(td[4].text.replace(",",""))
    total_tested = int(td[10].text.replace(",",""))
    total_population = int(td[12].text.replace(",",""))
    print(total_cases)

    death_ratio = total_deaths/total_cases
    test_ratio = total_tested/total_population

    #comparing to the initialized death ratio in line39-44
    if death_ratio > high_death_ratio:
        state_death_ratio = state 
        #replacing state with the state death ratio
        high_death_ratio = death_ratio
    
    if test_ratio > high_test_ratio:
        state_worst_testing = state
        high_test_ratio = test_ratio

    if test_ratio < low_test_ratio:
        state_best_testing =state
        low_test_ratio = test_ratio
    
print("State with the highest death ratio is:", state_death_ratio)
print("Death Ratio:", format(high_death_ratio,'.2%')) #highest_test_ratio
print()
print("State with the best testing ratio is:", state_best_testing)
print("Death Ratio:", format(high_test_ratio,'.2%')) 
print()
print()
print("State with the worst testing ratio is:", state_worst_testing)
print("Test Ratio:", format(low_test_ratio,'.2%')) 
print()

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")



