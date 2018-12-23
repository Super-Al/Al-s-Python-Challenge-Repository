'''
Created on 22 Dec 2018

@author: Alisdair
'''
import pickle
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/peak.html"
src = "http://www.pythonchallenge.com/pc/def/banner.p"

databytes = urllib.request.urlopen(src).read()

print (databytes)

_list = pickle.loads(databytes)
print(_list)

for element in _list:
    for item in element:
        for n in range(item[1]):
            print(item[0],end="")
    print()            