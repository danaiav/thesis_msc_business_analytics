# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:57:12 2016

@author: Danai
"""

import re   
import os
computername2="F:/Dropbox/Dani"
computername1="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
#create a csv file that we will put the results in
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/social_media.csv','w')
#import the first line with the titles
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/social_media.csv','a') as the_file:
    the_file.write('range'+';'+'company'+';'+'facebook'+';'+'twitter'+';'+'instagram'+';'+'pinterest'+';'+'youtube')
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
           #How many pictures
            sm = ['facebook','twitter','instagram','pinterest','youtube'] 
            sm2 =['Facebook','Twitter','Instagram','Pinterest','Youtube'] 
            number = 0 
            with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/social_media.csv','a') as the_file2:
                the_file2.write('\n'+i+';'+alist[num]+';')
            for index in range(len(sm)):
                x = sm[index]
                photo = re.findall(x,line) 
                y = sm2[index]
                photo2 = re.findall(y,line)
                if (len(photo)>0 or len(photo2)>0):
                    print ('The site of the company ', alist[num],' has ',x)
                    with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/social_media.csv','a') as the_file3:
                        the_file3.write('YES'+';') # write them to the file
                else:
                    print ('The site of the company ', alist[num],' does not have ',x)
                    with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/social_media.csv','a') as the_fileq:
                        the_fileq.write('NO'+';') # write them to the file
                    
