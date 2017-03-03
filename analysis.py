import sqlite3
import time

conn = sqlite3.connect('knowledgeBase.db')
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
        print negativeWords
    print 'negative words loaded'
    print '####################################'
    for posRow in c.execute(sql, [(1)]):
        positiveWords.append(posRow[0])
        print positiveWords
    print 'positive words loaded'


'''
        In the below function comparison is done with the both arrays and counting is done. If count>0 postive statement
        if count = 0 neutral , count <0 negative statement

'''

def testSentiment():
    readFile = "good"

    sentCounter = 0

    for eachPosWord in positiveWords:
        if eachPosWord in readFile:
            sentCounter = sentCounter + 1
            print sentCounter


    for eachnegWord in negativeWords:
        if eachnegWord in readFile:
            sentCounter = sentCounter - 1

    if sentCounter > 0:
        print 'this text is pos'

    if sentCounter < 0:
        print 'this text is neg'

    if sentCounter == 0:
        print 'this text is neutral'

    print sentCounter

loadWordArrays()
testSentiment()