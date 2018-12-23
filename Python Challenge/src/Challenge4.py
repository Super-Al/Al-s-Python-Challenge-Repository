'''
Created on 11 Dec 2018

@author: Alisdair
'''
import urllib.request
import re

"""
number="12345"

for n in range(86):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number
    urlref = urllib.request.urlopen(url)
    pagetext = urlref.read().decode('utf-8')
    urlref.close()
           
    print(n," " + url)
    print(pagetext)
    
    number = re.findall(r"\d+",pagetext)[0]
"""

number="16044"
number="8022"
number="49574"
number="32660"

for n in range(86):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(number)/1)
    urlref = urllib.request.urlopen(url)
    pagetext = urlref.read().decode('utf-8')
    urlref.close()
           
    print(n," " + url)
    print(pagetext)
    
    number = re.findall(r"(?<=and the next nothing is )\d+",pagetext)[0] 
 
