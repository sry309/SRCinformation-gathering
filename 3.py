#coding=utf8
import re
import os

def getlist():
    filename = raw_input('filename')
    print filename

    ft = open("url.txt",'w+')

    with open(str(filename), 'r') as f: 
        lines = [line.strip() for line in f.readlines()] 
        for x in lines:
            lists=x.split('-')
            result = lists[1]
            ft.write(result+'\n')
            print result

getlist()
print 'done'
