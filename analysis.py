import sqlite3
import time
import nltk
import re
import csv
from bs4 import BeautifulSoup
conn = sqlite3.connect('knowledgeBasenew.db')
conn.text_factory = str
c = conn.cursor()

'''
    In this module analysis of the review is done based on the feature extracted and compared with word in the word bank.

'''


negativeWords = []
positiveWords = []

sql = "SELECT * FROM wordVals WHERE value=?"

'''
   Below function is used to load all the positive and negative word from the word bank database store in an array for comparision.
'''
def loadWordArrays():
    for negRow in c.execute(sql, [(-1)]):
        negativeWords.append(negRow[0])
    print 'negative words loaded'

    for posRow in c.execute(sql, [(1)]):
        positiveWords.append(posRow[0])
    print 'positive words loaded'


'''
        In the below function comparison is done with the both arrays and counting is done. If count>0 postive statement
        if count = 0 neutral , count <0 negative statement

'''
#readFile = open("Example.txt", "r").read()

with open('out.csv','r') as f:
    reader = csv.reader(f)
    list = []
    for item in reader:
        list.append(item)
        tagged = nltk.pos_tag(item)

        namedEnt = nltk.ne_chunk(tagged, binary=True)
        entities = re.findall(r'NE\s(.*?)/', str(namedEnt))
        adjectives = re.findall(r'\(u\'(\w*)\',\s\'JJ\w?\'', str(tagged))
        if len(entities) > 1:
            pass
        elif len(entities) == 0:
            pass
        else:
            for adj in adjectives:
                print


def testSentiment():

    sentCounter = 0

    for eachPosWord in positiveWords:
        if eachPosWord in list:
            if len(eachPosWord) > 2:
                sentCounter = sentCounter + .2


    for eachnegWord in negativeWords:
        if eachnegWord in list:
            if len(eachnegWord) > 2:
                sentCounter = sentCounter - 1.3


    if sentCounter > 0:
        print 'this site is good. You can buy from here.'

    if sentCounter < 0:
        print 'this site is not good. Buy at your own risk'

    if sentCounter == 0:
        print 'this site is OK OK(neutral).'


loadWordArrays()
testSentiment()
