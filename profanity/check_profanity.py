'''
Created on Feb 27, 2018

@author: guan
'''
from urllib.request import urlopen
import re
def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    contents_of_file = re.sub("\W", "", contents_of_file)
    print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()
    
def check_profanity(text_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()
    