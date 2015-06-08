# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:58:44 2015

@author: yx1992
"""
from string import whitespace
import csv
import os

for root, dirs, files in os.walk('../Data'):
    for filename in files:
        openname="..//Data//"+filename
        outname="..//tag//"+filename
        fout=open(outname,'w')
        header="wordlist,countlist,maxlike,totallike,avelike\n"
        fout.write(header)
        with open(openname, 'rb') as csvfile:
            wordlist=[]
            countlist=[]
            maxlike=[]
            totallike=[]
            avelike=[]
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                s=''
                for i in range(4,len(row)-1):
                    s+=row[i]
                    #s=s[1:len(s)-1]
                #print s
                s=s[2:len(s)-2]
                s=''.join(s.split())
                #print s
                lines=s.split("Tag:")
                #print len(lines)
                #print lines
                if row[3]=='Number of Likes':
                    continue
                like=int(row[3])
                for i in range(1,len(lines)):
                    if lines[i] not in wordlist:
                        wordlist.append(lines[i])
                        countlist.append(1)
                        
                        maxlike.append(like)
                        totallike.append(like)
                        avelike.append(like)
                    else:
                        j=(k for k,v in enumerate(wordlist) if v==lines[i]).next()
                        countlist[j]+=1
                        if like> maxlike[j]:
                            maxlike[j]=like
                        totallike[j]+=like
                        avelike[j]=totallike[j]/countlist[j]
                        
            for i in range(len(wordlist)):
                line=wordlist[i]+","+str(countlist[i])+","+str(maxlike[i])+","+str(totallike[i])+","+str(avelike[i])+"\n"
                fout.write(line)    
        
        fout.close()
                