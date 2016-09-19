# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:27:28 2016

@author: Danai
"""
import urllib
from time import time

computername2="F:/Dropbox/Dani"
computername1="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
ND =open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables.csv')
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/loading_times.csv','w')
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/loading_times.csv','a') as the_file:
    the_file.write('Range'+';'+'Company'+';'+'site'+';'+'loading time'+';')
browser=urllib.request.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
alist =[]
sitelist = []
k=0
n=0
ndlist=[]
show=0
showlist=[]
for notd in ND:
                 page_B = notd.rstrip()
                 partsB = page_B.split(';')
                 print (partsB[2])
                 sitesB=partsB[2] 
                 ndlist.insert(n,sitesB)
                 n=n+1  
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
             show=0
             for a in range (1,21):
                 if ndlist[a] == sites:
                     print("Nothing: "+str(k))
                     show=1
                     showlist.insert(k-1,'1')
             if show == 0:
                   print("Run it normally: "+str(k))
                   url= "http://"+ sites
                   try:
                       response=browser.open(url)# this might throw an exception if something goes wrong.
                   except Exception:
                       continue
                   start_time = time()
                   myHTML=response.read()   
                   end_time = time()    
                   response.close()
                   print(round(end_time-start_time, 3))
                   l_t = round(end_time-start_time, 3)   
                   with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/loading_times.csv','a') as the_file2:
                       the_file2.write('\n'+str(k)+';'+str(companyname)+';'+str(url)+';'+str(l_t)+';')
                         


            

                