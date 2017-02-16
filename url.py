import urllib.request #for opening and reading URLs
from bs4 import BeautifulSoup #Python library for pulling data out of HTML and XML files.

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India" #link for testing

page = urllib.request.urlopen(wiki) 

soup = BeautifulSoup(page) #page will store the webpage data. 

print(soup.prettify()) #prints data in a structured manner.
