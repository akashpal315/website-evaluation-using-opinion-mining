import sqlite3

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

def create_table():
        c.execute('CREATE TABLE IF NOT EXIST stuffToPlot(unix REAL, date_stamp TEXT, namedEnt TEXT, relatedWord TEXT)')


create_table()