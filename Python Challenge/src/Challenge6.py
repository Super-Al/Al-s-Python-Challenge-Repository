'''
Created on 23 Dec 2018

@author: Alisdair

welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
'''

import re
import zipfile

prog = re.compile(r"(?<=nothing is )\d+")
number = "90052"
zipref = zipfile.ZipFile("channel (challenge 6).zip","r")

n = 0

while True:
    fileref = zipref.open(number+".txt")
    data = fileref.read().decode("utf-8")
    
    """print(n,end="")
    print(data)"""
    
    info = zipref.getinfo(number+".txt")
    print(info.comment.decode("utf-8"),end="")
            
    n = n+1
    
    fileref.close()
    result = prog.search(data)
    if result:
        number = result.group(0)
    else:
        break

zipref.close()