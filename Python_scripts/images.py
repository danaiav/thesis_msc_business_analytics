# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 14:31:16 2016

@author: Danonito
"""
import re   
import os
computername2="F:/Dropbox/Dani"
computername1="C:/Users/Danonito/Dropbox/Dani"
LIST500 =open(computername2+'/Spinellis - Diplwmatiki/fortune500.csv')
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images1.csv','w')
fw1=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables1.csv','w')
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images1.csv','a') as the_file:
    the_file.write('range'+';'+'companyname'+';'+'png'+';'+'dib'+';'+'jpg'+';'+'jpeg'+';'+'bmp'+';'+'jpe'+';'+'gif'+';'+'tif'+';'+'tiff'+';'+'total'+';')

with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables1.csv','a') as the_file_na:
    the_file_na.write('range'+';'+'companyname'+';'+'site'+';')

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
#find how many pictures has each one of the 50 first sites
for num in range(0,500):
    i=str(num+1)  
    if os.path.exists(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt'):
        hand = open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt')
        for line in hand:
            line = line.rstrip()
           #How many pictures
            images = ['.png','.dib','.jpg','.jpeg','.bmp','.jpe','.gif','.tif','.tiff'] 
            number = 0 
            with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images1.csv','a') as the_file2:
                the_file2.write('\n'+i+';'+alist[num]+';')
            for index in range(len(images)):
                x = images[index]
                photo = re.findall(x,line) 
                print ('The site of the company ', alist[num],' has ',len(photo),' ',x,' photos')
                with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images1.csv','a') as the_file3:
                    the_file3.write(str(len(photo))+';') # write them to the file
                number = len(photo) + number
            print ('The total number of photos in the site of the company ', alist[num],' are ',number)
            with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images1.csv','a') as the_file4:        
                the_file4.write(str(number)+';')  
    if not os.path.exists(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt'):
        print('The site: '+ alist[num]+' has not been downloaded!')#something is wrong with these sites i have to check them again
        with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables1.csv','a') as the_filena:
            the_filena.write('\n'+i+';'+alist[num]+';'+sitelist[num]+';')
print (alist)
#Now we will found the height and the weight of the fucking 50 first sites
fwim=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images_sizes1.csv','w')    
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images_sizes1.csv','a') as the_file1_sizes:
            the_file1_sizes.write('range'+';'+'company'+';'+'dimensions'+';'+'occurencies'+';')
