'''
Created on 11 Dec 2018

@author: Alisdair
'''
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

urlref = urllib.request.urlopen(url)
data = urlref.read()
print(data)