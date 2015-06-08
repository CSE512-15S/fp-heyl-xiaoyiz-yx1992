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

filename="Seattle"
openname=".\\Data\\"+filename+".csv"
outname=filename+"_resample.csv"
fout=open(outname,'w')
header="score,countlist,totallike,avelike,img1,img2\n"
fout.write(header)
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
        if c[i]>=4:
            line=f[i]+","+str(c[i])+","+str(a[i])+","+str(l[i][0])+","+str(l[i][1])+","+str(l[i][2])+","+str(l[i][3])+"\n"
            fout.write(line)    

fout.close()
        