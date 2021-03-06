# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 22:08:08 2015

@author: yx1992
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:58:44 2015

@author: yx1992
"""
from string import whitespace
import csv
import os
from os import walk

for root, dirs, files in os.walk('./Data'):
    for filename in files:

        if(filename!="total.csv"):
            outname=".//processed//"+filename
            fout=open(outname,'w')
            header="filter_name,score,avg_like,img1,img2,img3,img4\n"
            fout.write(header)
            openname=".//Data//"+filename
            with open(openname, 'rb') as csvfile:
                filterlist=[]
                countlist=[]
                totallike=[]
                avelike=[]
                linklist=[[]]
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    filtername=row[2]
                    if row[3]=='Number of Likes':
                        continue
                    like=int(row[3])
            
                    if filtername not in filterlist:
                        filterlist.append(filtername)
                        countlist.append(1)
                        
                        totallike.append(like)
                        avelike.append(like)
                        linklist.append([row[len(row)-1]])
                    else:
                        j=(k for k,v in enumerate(filterlist) if v==filtername).next()
                        countlist[j]+=1
                        totallike[j]+=like
                        avelike[j]=totallike[j]/countlist[j]
                        linklist[j].append(row[len(row)-1])
                        
                zipped=zip(filterlist,countlist,avelike,linklist)
                zipped.sort(key = lambda t: t[1],reverse=True)     
                f,c,a,l=zip(*zipped)
                for i in range(len(f)):
                    if len(l[i])>=4:
                        line=f[i]+","+str(c[i])+","+str(a[i])+","+str(l[i][0])+","+str(l[i][1])+","+str(l[i][2])+","+str(l[i][3])+"\n"
                        fout.write(line)
                    elif i<=3:
                        line=f[i]+","+str(c[i])+","+str(a[i])+","+str(l[i][0])
                        for j in range (len(l[i])):
                            line+=","+str(l[i][j])
                        for j in range(4-len(l[i])):
                            line+=","
                        line+="\n"
                        fout.write(line)    
            
            fout.close()
        