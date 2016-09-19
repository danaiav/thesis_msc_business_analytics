# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:09:03 2016

@author: Danai
"""

import re   
import os
computername1="F:/Dropbox/Dani"
computername2="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
diction =open(computername2+'/Spinellis - Diplwmatiki/dictionary.txt')
dictionary = []
da = 0
for d in diction:
    lined = d.rstrip()
    #print(lined)
    dictionary.insert(da,lined)
    da=da+1
    
#print(dictionary)
#create a csv file that we will put the results in
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/words.csv','w')
#import the first line with the titles
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/words.csv','a') as the_file:
    the_file.write('range'+';'+'company'+';'+'word'+';'+'occurencies'+';'+'total'+';')
alist =[]
sitelist = []
k=0
empty=[]
empty2=' '


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
    if os.path.exists(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt'):
        file = open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt','r+')
        wordcount={}
        corwordcount={}
        simeiastiksis = ["/",'1',"2","0","3","4","5","6","7","8","9",".",",","=",">","<","?","|",":","_","]","[","$","&","%","(",")","{","}",'"',";","\\","-","!","+","#","=","@","^","*","'"]
        for line in file:
            for ss in range(len(simeiastiksis)):
                simeio = simeiastiksis[ss]     
                line = line.replace(simeio, " ")
        for word1 in line.split():
            if word1 not in wordcount:
                wordcount[word1] = 1
            else:
                wordcount[word1] += 1  
        a=0
        ak=[]
        for k,v in wordcount.items():
           # print (k,v)
            ak.insert(a,k)
            a=a+1
        ak=sorted(ak)
        alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        start_end =[0,23847,41594,72207,90469,104087,115757,126064,139055,152031,154600,158151,167454,196007,199026,211303,244643,246394,262832,300271,318063,340711,345865,352307,352737,353779,354980]
        for q in range(len(ak)):
            word2 = ak[q]  
            word = word2.lower()
            letters= list(word)
            if letters is not empty: 
                let = letters[0]
                #print(let)
                for ww in range(len(alphabet)):
                    ldw =alphabet[ww]
                    #print(ldw)
                    if let is ldw:
                        #print('same letter')
                        start = start_end[ww]
                        end = start_end[ww+1]
                        ax = 0
                        for ass in range (start,end):
                           # print (dictionary[i])
                           # print (word)
                          #  print(ass)
                          #  print(end -1)
                            check = end -1
                            w = (ass == check)
                            word_dic = dictionary[ass]
                            if word == word_dic:
                                print('TRUE ',q)
                                ass = end
                                ax = 1
                            if w == True:
                                if ax == 0:                                    
                                    print('reach end',q)
                                    if word is not dictionary[ass]:
                                        del wordcount[word2]
                                
    for k,v in wordcount.items():
           print (k,v)
           with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/words.csv','a') as the_fileq: 
                the_fileq.write('\n'+str(i)+';'+alist[num]+';'+str(k)+';'+str(v)+';'+str(len(wordcount))+';')

#fw1=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/uwords.csv','w')
#with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/uwords.csv','a') as the_filequ1: 
 #               the_filequ1.write('range'+';'+'company'+';'+'unique_words'+';')        
#unique_words=0                           
#un_w =open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/words_sintitle.csv')
#for numw in range(0,10):
 #       i=numw+1
  #      k=str(i)
   #     unique_words = 0 
    #    for un in un_w:
     #       page_w = un.rstrip()
      #      parts_w = page_w.split(';')
       #     range_c = parts_w[0]
        #    oc_c = parts_w[3]            
         #   if k == range_c:
          #      print ("in")
           #     if oc_c == '1':
            #        print('also in')
             #       unique_words = unique_words + 1                    
    #    with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/uwords.csv','a') as the_filequ: 
     #           the_filequ.write('\n'+str(i)+';'+alist[numw]+';'+str(unique_words)+';')
            



            
            