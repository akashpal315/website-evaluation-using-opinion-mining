from bs4 import BeautifulSoup
import requests
startingWord = 'good'
startingWordVal = 1

synArray = []

def main():
    try:
        p = 'http://pydictionary-geekpradd.rhcloud.com/api/synonym/'+startingWord
        page = requests.get(p)
        data = page.text
        print data
    except Exception, e:
        print e