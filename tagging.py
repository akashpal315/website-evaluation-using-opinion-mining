import nltk
import numpy
import re
import time
import codecs
import bs4
from bs4 import *
import sqlite3
import datetime
conn = sqlite3.connect('knowledgeBasenew.db')
c = conn.cursor()

'''
    ScrapedText.xml is opened for a) tokenization
                                  b) Part of Speech tagging
                                  c) Feature extraction
    Features are stored in array/database
'''

infile = open("scrapedText.xml", "r")
contents = infile.read()
soup = BeautifulSoup(contents, 'html.parser')
review = soup.find_all("review_text")
#print content

def processLanguage():
    try:
        for item in review:
            tokenized = nltk.word_tokenize(item.getText())
            tagged = nltk.pos_tag(tokenized)
            print tagged
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            #print namedEnt
            entities = re.findall(r'NE\s(.*?)/', str(namedEnt))
            adjectives = re.findall(r'\(u\'(\w*)\',\s\'JJ\w?\'', str(tagged))
            if len(entities) > 1:
                pass
            elif len(entities) == 0:
                pass
            else:
                print '_________________________________'
                print 'Named: ', entities[0]
                print 'Adjectives:'
                for adj in adjectives:
                    print adj
                    currentTime = time.time()
                    date_stamp = datetime.datetime.fromtimestamp(currentTime).strftime('%y-%m-%d %H:%M:%S')
                    namedEntity = entities[0]
                    relatedWords = adj
                    c.execute('INSERT INTO stuffToPlot (unix, date_stamp, namedEnt,relatedWord) VALUES(?,?,?,?)',
                              (currentTime, date_stamp, namedEntity, relatedWords))
                    conn.commit()
    except Exception, e:
        print e

processLanguage()