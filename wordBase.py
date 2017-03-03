import sqlite3
from PyDictionary import PyDictionary


conn = sqlite3.connect('knowledgeBase.db')
conn.text_factory = str
c = conn.cursor()

'''
        In this a separate table of wordBase is used to store all the synonyms of good, bad, neutral and further there synonyms
        with a value of 1 for good, -1 for bad and 0 for neutral.
        PyDictionary is used to find the synonym and store in db with initial values.

'''

startingWord = 'good'
startingWordValue = 1.0

def machine_learning():
    dictionary = PyDictionary()   #used to find all the synonym of a word

    try:
        val = -1.0
        exe = "SELECT word FROM wordVals WHERE value=?"
        c.execute(exe, [(val)])
        for row in c.fetchall():
            print row
            synoNym = dictionary.synonym(row)
            print synoNym
            for eachSyn in synoNym:
                query = "SELECT * FROM wordVals WHERE word=?"
                c.execute(query, [(eachSyn)])
                data = c.fetchone()

                if data is None:
                    c.execute("INSERT INTO wordVals (word,value) VALUES (?,?)", (eachSyn, startingWordValue))
                    conn.commit()
                else:
                    print
    except Exception, e:
        print e

machine_learning()

#c.execute("INSERT INTO doneSyn (word) VALUES (?)",(startingWord))

#conn.commit()