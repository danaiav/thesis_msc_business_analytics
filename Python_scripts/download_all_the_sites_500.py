# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:14:22 2016

@author: Danai
"""

import urllib
import time

computername2="F:/Dropbox/Dani"
computername1="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
alist =[]
k=0
browser=urllib.request.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
    #dowload the 50 firsts sites
for page in LIST500:
    page_A = page.rstrip()
    parts = page_A.split(';')
    print (parts[2])
    i = parts[0]
    companyname = parts[1]
    alist.insert(k,companyname)
    k=k+1
   
    url= "http://"+ parts[2]

    #an exception might be thrown, so the code should be in a try-except block
    try:
        #use the browser to get the url.
        response=browser.open(url)# this might throw an exception if something goes wrong.

    except Exception: # this describes what to do if an exception is thrown
       # print 'Error while fetching page', page
      #  print sys.exc_info()
        continue#ignore this page.
  
    #read the response in html format. This is essentially a long piece of text
    myHTML=response.read()
    fwriter=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+str(k)+'_'+companyname+'.html','w')
    fwriter.write(str(myHTML))
    fwriter.close()
    fwriter=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+str(k)+'_'+companyname+'.txt','w')
    fwriter.write(str(myHTML))
    fwriter.close()

    #wait for 2 seconds
    time.sleep(2)
