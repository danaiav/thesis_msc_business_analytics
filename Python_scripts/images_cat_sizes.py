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
fw=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images.csv','w')
fw1=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables.csv','w')
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images.csv','a') as the_file:
    the_file.write('range'+';'+'companyname'+';'+'png'+';'+'dib'+';'+'jpg'+';'+'jpeg'+';'+'bmp'+';'+'jpe'+';'+'gif'+';'+'tif'+';'+'tiff'+';'+'total'+';')

with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables.csv','a') as the_file_na:
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
            with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images.csv','a') as the_file2:
                the_file2.write('\n'+i+';'+alist[num]+';')
            for index in range(len(images)):
                x = images[index]
                photo = re.findall(x,line) 
                print ('The site of the company ', alist[num],' has ',len(photo),' ',x,' photos')
                with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images.csv','a') as the_file3:
                    the_file3.write(str(len(photo))+';') # write them to the file
                number = len(photo) + number
            print ('The total number of photos in the site of the company ', alist[num],' are ',number)
            with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images.csv','a') as the_file4:        
                the_file4.write(str(number)+';')  
    if not os.path.exists(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.txt'):
        print('The site: '+ alist[num]+' has not been downloaded!')#something is wrong with these sites i have to check them again
        with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/not_downloadables.csv','a') as the_filena:
            the_filena.write('\n'+i+';'+alist[num]+';'+sitelist[num]+';')
print (alist)
#Now we will found the height and the weight of the fucking 50 first sites
fwim=open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images_sizes.csv','w')    
with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images_sizes.csv','a') as the_file1_sizes:
            the_file1_sizes.write('company'+';'+'dimensions'+';'+'occurencies'+';')
lines = [] 
for num in range(0,50):
    i=str(num+1)
    if os.path.exists(computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.html'):
        with open (computername2+'/Spinellis - Diplwmatiki/Python Scripts/sites/'+ i +'_'+alist[num]+'.html', 'rt') as in_file: 
            for line in in_file:
                lines.append(line)
           # print(lines[0].find("height"))
            infoMatch_h= re.findall('height\S+"([0-9]+)"',line)
            print(len(infoMatch_h))
            print(infoMatch_h)
            infoMatch_w= re.findall('width\S+"([0-9]+)"',line)
            print(len(infoMatch_w))
            print(infoMatch_w)
            h_w=[]
            hw=0
            if len(infoMatch_h)>= len(infoMatch_w):
                height = infoMatch_w           
                print(height)
            if len(infoMatch_h)< len(infoMatch_w):
                height = infoMatch_h           
                print(height)    
            for l in range(len(height)):
                h_w_c=infoMatch_h[l]+'x'+infoMatch_w[l]    
                h_w.insert(hw,h_w_c)
                hw=hw+1
            if h_w == []:#we check if there are not any dimensions available
                print("No photos for "+ alist[num]+" so we go to the next site")
            if h_w != []:#now we continue with the cases where the dimensions are indeed available
                print(h_w)
                from collections import Counter
                hw_unique = Counter(h_w)
                hw_unique2 = str(hw_unique)#unique different prices
                print(hw_unique2)
                split1 = hw_unique2.split('{')
                a=split1[1]
                split2 =a.split('}')
                b=split2[0]
                split3 = b.split(',')
                print(split3)
                finalsplit=[]
                z=0
                m=1
                for numb in range(len(split3)):
                    oldstring = split3[numb]
                    newstring = oldstring.replace('"', "")
                    new = newstring.replace("'","")
                    string = new.replace(" ","")
                    finalstring = string.split(':')
                    finalsplit.insert(z,finalstring[0])
                    finalsplit.insert(m,finalstring[1])
                    z=z+2
                    m=m+2
                print(finalsplit)
                print('Different dimensions in the site:'+alist[num]+' : '+str(len(hw_unique)))
                z1=0
                m1=1
                for h in range(len(hw_unique)):
                    with open(computername2+'/Spinellis - Diplwmatiki/Python Scripts/infos/info_images_sizes.csv','a') as the_file2_sizes:
                            the_file2_sizes.write('\n'+alist[num]+';'+finalsplit[z1]+';'+finalsplit[m1]+';')
                    z1=z1+2
                    m1=m1+2