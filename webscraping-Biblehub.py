import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


url = 'https://biblehub.com/asv/john/1.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

verses_list = soup.findAll('p',class_='reg')
#class_='reg' selects all elements with class attribute
#of "reg", the 'reg' is specific to the website
#on website it says <p class='reg'>

#for verse in verses_list:
    #print(verse.text) #.text extracts text content of element
    #input()

verse_list = [v.text.split('.') for v in verses_list]
#splits the first 5 verses based on the period
#first 5 verses is classified as one element

print(verse_list)

print(random.choice(random.choice(verse_list)))

#within john 1 each para is sort of a list, we have a para
#within that list we hv a block of each para within that list

