# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:27:36 2016

@author: Danai
"""

import re   
import os
computername2="F:/Dropbox/Dani"
computername1="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
#create a csv file that we will put the results in
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/unique_words.csv','w')
#import the first line with the titles
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/unique_words.csv','a') as the_file:
    the_file.write('range'+';'+'company'+';'+'unique_words'+';')
alist =[]
sitelist = []
k=0
for page in LIST500:
    page_A = page.rstrip()
    parts = page_A.split(';')
   # print (parts[2])
    sites=parts[2]
    i = parts[0]
    companyname = parts[1]
    alist.insert(k,companyname)
    sitelist.insert(k,sites)
    k=k+1
for num in range(0,500):   
    i=str(num+1)  
    print('Site number: ', i)
    count = 0
    with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/unique_words.csv','a') as the_file2:
        the_file2.write('\n'+i+';'+alist[num]+';')
    file = open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/words.csv')
    for line in file:
        line = line.rstrip()
        row = line.split(';')
        range_element = row[0]
        company_element = row[1]
        occurencies_element = row[3]
        if company_element == str(alist[num]):
            if occurencies_element == '1':
                count = count +1
    with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/unique_words.csv','a') as the_file3:
        the_file3.write(str(count)+';')            