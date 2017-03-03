import bs4
from bs4 import *


'''
        In this function reviews are extracted and stored in another file scrapedText.xml
'''


def review_extraction():
        try:

                raw_content = BeautifulSoup(open("review2.xml"), "html.parser")
                try:
                        reviews = raw_content.find_all("review_text")
                        openfile = open("scrapedText.xml", "w")
                        for r in reviews:
                                openfile.write(r.encode())
                                #print r.getText()
                        openfile.close()
                except Exception, e:
                        print e

        except Exception, e:
                print e


review_extraction()