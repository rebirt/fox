# -*- coding: utf-8 -*-
import string,random

git = string.ascii_uppercase + string.digits

def get_random():
    return ''.join(random.sample(git,4))

def gert(group):
    return '-'.join([get_random() for i in range(group)])

def ck(n,result= None):
    if result is None:
        result = []
    for i in range(n):
        result.append(gert(4))
    return result

if __name__ == "__main__":
    L = ck(200)
    for i in L:
        print(i)