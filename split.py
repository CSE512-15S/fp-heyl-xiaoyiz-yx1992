# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:58:44 2015

@author: yx1992
"""

import csv
with open('.\\Data\\Boston.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        s=''
        for i in range(4,len(row)-1):
            s+=row[i]
            print s.encode
            #s=s[1:len(s)-1]
            lines=s.split("Tag:")
        #print lines
        print lines