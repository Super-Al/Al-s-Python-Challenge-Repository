'''
Created on 8 Dec 2018

@author: Alisdair
'''

with open("Challenge 2 Text File.txt") as f:
    read_data = f.read()
f.closed    

for c in read_data:
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        print(c,end="")        