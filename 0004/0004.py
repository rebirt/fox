# -*- coding: utf-8 -*-

import re

with open ('e:\\text1.txt','r') as f:
    text = f.read()
    words = re.findall('\\w+',text)
    
    worddict = dict()
    
    for word in words:
        if word.lower() in worddict:
            worddict[word.lower()] += 1
        else:
            worddict[word] = 1
            
for key,value in worddict.items():
    print('%s:%s' % (key,value))                