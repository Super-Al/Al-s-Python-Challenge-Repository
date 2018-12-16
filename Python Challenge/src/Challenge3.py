'''
Created on 9 Dec 2018

@author: Alisdair
'''

with open("Challenge 3 Text File.txt") as f:
    read_data = f.read()
f.closed

for n in range(4,len(read_data)):
    if read_data[n-4].islower() and \
     read_data[n-3].isupper() and \
     read_data[n-2].isupper() and \
     read_data[n-1].isupper() and \
     read_data[n].islower() and \
     read_data[n+1].isupper() and \
     read_data[n+2].isupper() and \
     read_data[n+3].isupper() and \
     read_data[n+4].islower():
        print(read_data[n],end="")
        