# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 18:38:37 2016

@author: Danai
"""

import re   
import os
computername2="F:/Dropbox/Dani"
computername1="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
#create a csv file that we will put the results in
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/links.csv','w')
#import the first line with the titles
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/links.csv','a') as the_file:
    the_file.write('range'+';'+'company'+';'+'totallinks'+';'+'external_links'+';'+'internal_links'+';')
alist =[]
sitelist = []
k=0
for page in LIST500:
    page_A = page.rstrip()
    parts = page_A.split(';')
    print (parts[2])
    sites=parts[2]
    i = parts[0]
    companyname = parts[1]
    alist.insert(k,companyname)
    sitelist.insert(k,sites)
    k=k+1
for num in range(0,500):
    i=str(num+1)  
    if os.path.exists(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt'):
        hand = open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt')
        for line in hand:
            line = line.rstrip()
            href = re.findall('href',line)
            external = re.findall('href="https:',line)
            print(len(external))
            ex = (len(external))
            print(len(href))
            alllinks = len(href)
            internal = alllinks - ex
            print(internal)
            with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/links.csv','a') as the_file2:
                the_file2.write('\n'+i+';'+alist[num]+';'+str(alllinks)+';'+str(ex)+';'+str(internal)+';')
            
    