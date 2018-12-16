'''
Created on 2 Dec 2018

@author: Alisdair
'''
_TEST_STRING = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

for c in _TEST_STRING: 
    a = ord(c)
    if a in range(97,120):
        a += 2
    elif a == 121:
        a = 97
    elif a == 122:
        a = 98

    print(chr(a),end="")
  
