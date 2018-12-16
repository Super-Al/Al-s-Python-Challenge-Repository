'''
Created on 2 Dec 2018

@author: Alisdair
'''

_TEST_STRING = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

starttext = "abcdefghijklmnopqrstuvwxyz"
endtext = "cdefghijklmnopqrstuvwxyzab"

table = str.maketrans(starttext,endtext)

print(_TEST_STRING.translate(table))
