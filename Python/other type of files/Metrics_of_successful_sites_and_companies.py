
# coding: utf-8

# In[1]:

#First we import the libraries we will need
import urllib
import urllib2
import time
import os
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd


# In[2]:

#First of all we need to find all the name of the sites that belong to fortune 500. This can happen if we seperate
#The information needed from the below link
url = "http://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites"
list_company_number =[]
list_company_name = []
list_company_website = []


# In[3]:

#In order to extract the needed informations we will create 3 lists. The first one will contain the rank of each site, the
#second one will contain the name of the company and the 3rd one will contain the actual link of the company's site.
#For achieving this purpose we will create a funstion that will in its turn create those three list.
#In order to know if the function worked we will ask it to return the first element of each list along with a sentence.
def websites (url): 
    from time import time # I used it to see how much time it does to run the function
    start = time ()
    browser = urllib2.build_opener() 
    browser.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = browser.open(url)# this might throw an exception if something goes wrong.
    myHTML = response.read()
    soup = BeautifulSoup(myHTML,"lxml")    
    o = 0
    td_list =[]
    for row2 in soup.html.body.findAll('td'):
        td_list.insert(o, row2)
        o = o + 1
    a = 0
    b = 1
    c = 2
    list_numbering = 0
    for i in range (0,500):        
        num = str(td_list[a])
        company = str(td_list[b])
        site = str(td_list[c])
        c_num = re.findall('>(.+?)</td>',num)  
        c_num = str(c_num[0])
        c_name = re.findall('>(.+?)</td>',company)
        c_name = str(c_name[0])
        c_site = re.findall('">(.+?)</a>',site)
        c_site = str(c_site[0])        
        list_company_number.insert(list_numbering,c_num)
        list_company_name.insert(list_numbering,c_name)
        list_company_website.insert(list_numbering,c_site)
        a = a + 3
        b = b + 3
        c = c + 3
        list_numbering =  list_numbering + 1 
    end = time ()
    duration = round (end - start, 1)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', duration, ' seconds'
    print 'The lists are ready in ', minutes, ' minutes'


# In[4]:

# After creating the function we should now test that it actually works correctly
websites (url)


# In[5]:

#Try to validate each page url #pip install validators
import validators
nv = 0
for num in range(len(list_company_website)):
    line = 'http://' + str(list_company_website[num])
    x = validators.url(line)    
    if x != True:
        nv = nv +1
print "The validation is complete! There were" , nv, "not valid pages"


# In[6]:

list500_sites = []
list500_names = []
list500_num = []
list500_url = []


# In[7]:

#def list_company_HTML (list_company_website,list_company_name,start,end):
import time
browser2 = urllib2.build_opener()
browser2.addheaders = [('User-agent', 'Mozilla/5.0')]
for i in range (0,500):
    k = str(i + 1)
    lc = str(list_company_website[i])
    lc = lc.replace("'","")
    lc = lc.replace("[","")
    lc = lc.replace("]","")
    lcn = str(list_company_name[i])
    lcn = lcn.replace("'","")
    lcn = lcn.replace("[","")
    lcn = lcn.replace("]","")
    url2= 'http://' + lc
    list500_names.insert(i,lcn)
    list500_url.insert(i,lc)
    list500_num.insert(i,k)
    if i == 118 or i == 464 or i == 268 or i == 70:
        #These sites have a problem and the whole code is stacking 
        #when I run it so we will thing of this site as a not downloadable
        list500_sites.insert(i,0)  
        print ("The site " + str(i) + " has NOT been downloaded!")
    else:
        #an exception might be thrown, so the code should be in a try-except block
        try:
            response2=browser2.open(url2)
            print ("The site " + str(i) + " has been downloaded!")
        except Exception: # this describes what to do if an exception is thrown
            list500_sites.insert(i,0)
            print ("The site " + str(i) + " has NOT been downloaded from exception!")           
            continue     
            #if it goes into to exception it does not continue below
        myHTML2=response2.read()
        list500_sites.insert(i,myHTML2) 
        #wait for 2 seconds
        time.sleep(2)       


# In[8]:

#As we can see there is one site that hasn't been downloaded in order
#to keep track of the sites that we could not download
#we will create a new list that we will keep them all together there
not_d = []
not_d_n = []
num = []
def not_downloadables (list500_names,list500_sites):
    met = 0       
    for i in range(len(list500_names)):       
        if list500_sites[i] == 0:
            ct = list500_names[i]
            not_d.insert(met,ct)
            not_d_n.insert(met,str(i))
            num.insert(met,met)
            met = met + 1
   


# In[9]:

#Now we will run the function to see which sites havent been downloaded
not_downloadables (list500_names,list500_sites)
d = {'company' : pd.Series(not_d, index=[num]),
     'number' : pd.Series(not_d_n, index=[num])}
nd = pd.DataFrame(d)    
nd


# In[10]:

empty=[]
keyf = []
flesch = []
sentence =[] 
word = []
unique_w = []


# In[11]:

import time # I used it to see how much time it does to run the function
for num in range(0,500):
    site = list500_sites[num]
    line = list500_url[num] 
    url_check = "http://www.webpagefx.com/tools/read-able/check.php?tab=Test+By+Url&uri=http://" + line
    browser = urllib2.build_opener()
    browser.addheaders = [('User-agent', 'Mozilla/5.0')]
    if site == 0 or num == 107:
        print("Site", str(num), "is not validated from sites")
        flesch.insert(num,"n/a")
        sentence.insert(num,"n/a")
        word.insert(num,"n/a")
        unique_w.insert(num,"n/a")  
    else:
        try:
            response = browser.open(url_check)
        except Exception: 
            flesch.insert(num,"n/a")
            sentence.insert(num,"n/a")
            word.insert(num,"n/a")
            unique_w.insert(num,"n/a")
            print("Site", str(num), "is not validated from check")
            continue        
        html_r = response.read()
        check = str(html_r)       
        if check != empty:                
                soup = BeautifulSoup(check,"lxml")
                o = 0
                keyf = []
                for row in soup.html.body.findAll('tr'):
                    keyf.insert(o,row)
                    o = o + 1
                if keyf != empty:                        
                        #print("Site", str(num), "is validated")
                        #Flesh measurement
                        if keyf[0] != empty:
                            readability = str(keyf[0])
                            split1 = readability.split('>')
                            readability2 = str(split1[4])
                            split2 = readability2.split('<')
                            readability3 = str(split2[0])
                            flesch.insert(num,readability3)
                        else:
                            flesch.insert(num,"n/a")
                            sentence.insert(num,"n/a")
                            word.insert(num,"n/a")
                            unique_w.insert(num,"n/a")   
                        #Number of sentences   
                        if keyf[6] != empty:
                            sentences = str(keyf[6])
                            spli1 = sentences.split('>')
                            sentences2 = str(spli1[4])
                            spli2 = sentences2.split('<')
                            sentences3 = str(spli2[0])
                            sentence.insert(num,sentences3)
                        else:
                            flesch.insert(num,"n/a")
                            sentence.insert(num,"n/a")
                            word.insert(num,"n/a")
                            unique_w.insert(num,"n/a")  
                        #Number of words
                        if keyf[7] != empty:
                            words = str(keyf[7])
                            spl1 = words.split('>')
                            words2 = str(spl1[4])
                            spl2 = words2.split('<')
                            words3 = str(spl2[0])
                            word.insert(num,words3)
                        else:
                            flesch.insert(num,"n/a")
                            sentence.insert(num,"n/a")
                            word.insert(num,"n/a")
                            unique_w.insert(num,"n/a")  
                        #No. of complex words
                        if keyf[7] != empty:
                            unique_ws = str(keyf[8])
                            sp1 = unique_ws.split('>')
                            unique_ws2 = str(sp1[4])
                            sp2 = unique_ws2.split('<')
                            unique_ws3 = str(sp2[0])
                            unique_w.insert(num,unique_ws3)
                        else:
                            flesch.insert(num,"n/a")
                            sentence.insert(num,"n/a")
                            word.insert(num,"n/a")
                            unique_w.insert(num,"n/a")  
                else:
                        print("Site", str(num), "is not validated from check 2")
                        flesch.insert(num,"n/a")
                        sentence.insert(num,"n/a")
                        word.insert(num,"n/a")
                        unique_w.insert(num,"n/a")            
    time.sleep(2)


# In[12]:

readability = []


# In[13]:

def readable (flesch):
    for i in range (len(flesch)):
            f_n = flesch[i]
            if f_n == "n/a":
                readability.insert(i,"n/a")                
            else:
                a = int(float(f_n))
                if a > 90:    
                    readability.insert(i,"Very easy")                    
                elif a > 80:
                    readability.insert(i,"Easy")
                elif a > 70:
                    readability.insert(i,"Fairly easy")
                elif a > 60:
                    readability.insert(i,"Standard")
                elif a > 50:
                    readability.insert(i,"Fairly difficult")
                elif a > 30:
                    readability.insert(i,"Difficult")
                else:
                    readability.insert(i,"Very Confusing")                    
    print "The function is completed!"


# In[14]:

readable (flesch)


# In[15]:

d1 = {'company' : pd.Series(list500_names, index=[list500_num]),
      'url' : pd.Series(list500_url, index=[list500_num]),
      'Readability' : pd.Series(readability, index=[list500_num]),
      'Flesh_Mesaure' : pd.Series(flesch,index=[list500_num]),
'Sentences' : pd.Series(sentence, index=[list500_num]),
'Words' : pd.Series(word, index=[list500_num]),
'Unique words' : pd.Series(unique_w, index=[list500_num])}
fre = pd.DataFrame(d1)    
fre.head(3) #we see the first 3 in the data frame
fre.to_csv('total_500_words.csv', sep=';')


# In[16]:

#Retreiving the social media from each site
#First create empty lists for the ones that 
#we will need to calculate
sm_f = []
sm_t = []
sm_i = []
sm_p = []
sm_y = []
sm_l = []   
sm_nm = [] 
nm = []
sm_url = []


# In[17]:

#Then create a function that will feel in those 
#lists so as to make the data frame later on
def socialmedia (list500_sites,list500_names,list500_url):
    from time import time 
    # I used it to see how much time it does to run the function
    start = time ()
    for i in range(len(list500_names)):        
            myHTML = list500_sites[i]
            sm = ['facebook.com','twitter.com',
                  'instagram.com','pinterest.com',
                  'youtube.com','linkedin.com'] 
            if myHTML == 0:                
                sm_nm.insert(i,list500_names[i]) 
                nm.insert(i,i)
                sm_url.insert(i,list500_url[i])
                sm_f.insert(i,'n/a')
                sm_t.insert(i,'n/a')
                sm_i.insert(i,'n/a')
                sm_p.insert(i,'n/a')
                sm_y.insert(i,'n/a')
                sm_l.insert(i,'n/a')
            else:
                for index in range(len(sm)):
                    x = sm[index]
                    social = re.findall(x,myHTML)                                
                    if (len(social) > 0):
                        if x == 'facebook.com':
                            answerf = 'TRUE'
                        if x == 'twitter.com':
                            answert = 'TRUE'
                        if x == 'instagram.com':
                            answeri = 'TRUE'
                        if x == 'pinterest.com':
                            answerp = 'TRUE'
                        if x == 'youtube.com':
                            answery = 'TRUE'
                        if x =='linkedin.com':
                            answerl = 'TRUE'                   
                    else:
                         if x == 'facebook.com':
                            answerf = 'FALSE'
                         if x == 'twitter.com':
                            answert = 'FALSE'
                         if x == 'instagram.com':
                            answeri = 'FALSE'
                         if x == 'pinterest.com':
                            answerp = 'FALSE'
                         if x == 'youtube.com':
                            answery = 'FALSE'
                         if x =='linkedin.com':
                            answerl = 'FALSE'                
                sm_nm.insert(i,list500_names[i]) 
                nm.insert(i,i)
                sm_url.insert(i,list500_url[i])
                sm_f.insert(i,answerf)
                sm_t.insert(i,answert)
                sm_i.insert(i,answeri)
                sm_p.insert(i,answerp)
                sm_y.insert(i,answery)
                sm_l.insert(i,answerl)
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are completed in ', minutes, ' minutes' 
    print 'The lists are ready in ', duration, ' seconds'


# In[18]:

#Now we will run the function for the 25 first sites for starters
socialmedia (list500_sites,list500_names,list500_url)


# In[19]:

#Finally we create the data frame with the elements we found            
d2 = {'company' : pd.Series(sm_nm, index=[nm]),
     'facebook' : pd.Series(sm_f, index=[nm]),
      'twitter' : pd.Series(sm_t, index=[nm]),
     'instagram' : pd.Series(sm_i, index=[nm]),
      'pinterest' : pd.Series(sm_p, index=[nm]),
     'youtube' : pd.Series(sm_y, index=[nm]),
      'linkedin' : pd.Series(sm_l, index=[nm]),}
social_media = pd.DataFrame(d2)    
social_media.tail(3) #we see the first 3 in the data frame
social_media.to_csv('total_500_sm.csv', sep=';')


# In[20]:

#Create the lists we will need for the data frame
l_nm = []
l_ex = []
l_in = []
l_t = []
nm = []
l_url = []


# In[21]:

#create the function that will calculate the different type of links
def links (list500_sites,list500_names,list500_url):
    from time import time 
    # I used it to see how much time it does to run the function
    start = time ()
    for num in range(len(list500_names)):        
            myHTML = list500_sites[num]
            if myHTML == 0:
                l_nm.insert(num,list500_names[num])            
                l_ex.insert(num,'n/a')
                l_t.insert(num,'n/a')
                l_in.insert(num,'n/a')
                nm.insert(num,num)                
            else: 
                href = re.findall('href',myHTML)
                external = re.findall('href="https:',myHTML)
                ex = (len(external))
                alllinks = (len(href))
                internal =  (len(href) - len(external))
                l_nm.insert(num,list500_names[num])            
                l_ex.insert(num,ex)
                l_t.insert(num,alllinks)
                l_in.insert(num,internal)
                nm.insert(num,num)                
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'
    print 'The lists are ready in ', duration, ' seconds'


# In[22]:

#Run the function in order to find the external, 
#internal and total links of each site
#For now we are running for the first 25 sites only
links (list500_sites,list500_names,list500_url)


# In[23]:

#Create a dataframe so as to be able to see 
#the results of the function we run
d3 = {'company' : pd.Series(l_nm, index=[nm]),
      'external' : pd.Series(l_ex, index=[nm]),
      'internal' : pd.Series(l_in, index=[nm]),
     'total links' : pd.Series(l_t, index=[nm])}
sites_links = pd.DataFrame(d3)    
sites_links.tail(3) #we see the first 3 in the data frame
sites_links.to_csv('total_500_sites_links.csv', sep=';')


# In[24]:

#The initial lists we will need in order 
#to calculate the loading time
lt_nm = [] 
lt_time = []
nm = []
lt_url = []


# In[ ]:

#the function that will calculate the loading time
def loadtime (list_company_website,list500_names,list500_url):
    from time import time
    browser2 = urllib2.build_opener()
    browser2.addheaders = [('User-agent', 'Mozilla/5.0')]
    for num in range(len(list500_names)):
        lc = str(list_company_website[num])        
        lc = lc.replace("'","")   
        lc = lc.replace("[","")
        lc = lc.replace("]","")
        url2 = 'http://' + lc
        if num == 118 or num == 464 or num == 70:
            #The site 118(119) has a problem and the whole code 
            #is stacking when I run it so we will thing of this 
            #site as a not downloadable
            lt_nm.insert(num,list500_names[num])            
            lt_time.insert(num,'n/a')
            nm.insert(num,num)
            lt_url.insert(num,list500_url[num])            
        else:
            try:
                response2 = browser2.open(url2)
            except Exception:
                lt_time.insert(num,'n/a')
                lt_nm.insert(num,list500_names[num])  
                nm.insert(num,num)
                print ("The site " + str(num)+ " has NOT been loaded!")
                continue     
            start_time = time()
            myHTML2 = response2.read()
            end_time = time()
            response2.close()
            l_t = round(end_time-start_time, 3) 
            #in order to be more readable we rounded the time
            loadt = str(l_t)
            lt_nm.insert(num,list500_names[num])            
            lt_time.insert(num,loadt)
            nm.insert(num,num)
            lt_url.insert(num,list500_url[num])
            #print ("The site " + str(num) + " has been loaded!")
    print "The function is completed!"


# In[ ]:

#running the function for the first 25 sites
loadtime (list_company_website,list500_names,list500_url)


# In[ ]:

#creating the data frame with the loading times
d4 = {'company' : pd.Series(lt_nm, index=[nm]),
      'loading time' : pd.Series(lt_time, index=[nm])}
loading_time = pd.DataFrame(d4)    
loading_time.head(3) #we see the first 3 in the data frame
loading_time.to_csv('loading_time.csv', sep=';')


# In[ ]:

#Find out how many and what type of images each site has
#first we create the initially empty lists
p_p = []
p_d = []
p_jpg = []
p_jpeg = []
p_gif = []
p_tif = []
p_tiff = []
p_bmp = []
p_jpe = []
p_nm = []
p_tt =[]
nm = []
p_url = []


# In[ ]:

#Then we create the function that will explore 
#the html pages and search for the images
def images (list500_sites,list500_names,list500_url):
    from time import time # I used it to see 
    #how much time it does to run the function
    start = time ()
    for num in range(len(list500_names)):
            myHTML = list500_sites[num] 
            image = ['.png','.dib','.jpg','.jpeg',
                     '.bmp','.jpe','.gif','.tif','.tiff'] 
            totalnumber = 0 
            if myHTML == 0:
                p_nm.insert(num,list500_names[num])            
                p_p.insert(num,'n/a')  
                p_d.insert(num,'n/a')  
                p_jpg.insert(num,'n/a')  
                p_jpeg.insert(num,'n/a')  
                p_gif.insert(num,'n/a')  
                p_tif.insert(num,'n/a')  
                p_tiff.insert(num,'n/a')  
                p_bmp.insert(num,'n/a')  
                p_jpe.insert(num,'n/a')  
                p_tt.insert(num,'n/a')
                nm.insert(num,num)
                p_url.insert(num,list500_url[num])          
            else: 
                for index in range(len(image)):
                    x = image[index]
                    photo = re.findall(x,myHTML)
                    if x == '.png':
                        p = str (len(photo))
                    if x == '.dib':
                        d = str (len(photo))
                    if x == '.jpg':
                        jpg = str (len(photo))
                    if x == '.jpeg':
                        jpeg = str (len(photo))
                    if x == '.gif':
                        gif = str (len(photo))
                    if x == '.tif':
                        tif = str (len(photo))
                    if x == '.tiff':
                        tiff = str (len(photo))
                    if x == '.bmp':
                        bmp = str (len(photo))
                    if x == '.jpe':
                        jpe = str (len(photo))
                    totalnumber = len(photo) + totalnumber
                total = str (totalnumber)
                p_nm.insert(num,list500_names[num])            
                p_p.insert(num,p)  
                p_d.insert(num,d)  
                p_jpg.insert(num,jpg)  
                p_jpeg.insert(num,jpeg)  
                p_gif.insert(num,gif)  
                p_tif.insert(num,tif)  
                p_tiff.insert(num,tiff)  
                p_bmp.insert(num,bmp)  
                p_jpe.insert(num,jpe)  
                p_tt.insert(num,total)
                nm.insert(num,num)
                p_url.insert(num,list500_url[num])
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'
    print 'The lists are ready in ', duration, ' seconds'


# In[ ]:

#Then we run the function for the first 20 sites for now
images (list500_sites,list500_names,list500_url)


# In[ ]:

#Finally we create a dataframe in order to see the results of the function
d5 = {'company' : pd.Series(p_nm, index=[nm]),
      '.png' : pd.Series(p_p, index=[nm]),
      '.dib' : pd.Series(p_d, index=[nm]),
      '.jpg' : pd.Series(p_jpg, index=[nm]),
      '.jpeg' : pd.Series(p_jpeg, index=[nm]),
      '.bmp' : pd.Series(p_bmp, index=[nm]),
      '.jpe' : pd.Series(p_jpe, index=[nm]),
      '.gif' : pd.Series(p_gif, index=[nm]),
      '.tif' : pd.Series(p_tif, index=[nm]),
      '.tiff' : pd.Series(p_tiff, index=[nm]), 
      'total images' : pd.Series(p_tt, index=[nm])}
images_types = pd.DataFrame(d5)    
images_types.head(3) #we see the first 3 in the data frame
images_types.to_csv('images_types.csv', sep=';')


# In[ ]:

#Now we will gather the total number of pixels that exist
#in each web page under examination
#with this we will have a grasp of the images that each site is using
im_nm = []
im_pix = []    
import time
def url_to_image(list500_names, list500_url):
    import numpy as np
    import urllib
    for num in range(len(list500_names)):
        url= 'http://' + list500_url[num]
        if num == 45 or num == 118 or num == 390:
            print (str(num), "Exception")
            im_pix.insert(num,"n/a")
            im_nm.insert(num,list500_names[num]) 
        else:
            try: # download the image, convert it to a NumPy array 
                resp = urllib.urlopen(url)
            except Exception:
                print (str(num), "Exception")
                im_pix.insert(num,"n/a")
                im_nm.insert(num,list500_names[num]) 
                continue
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            #print(image)
            pixels = 0
            #add up all the pixels of the page
            for n in range (len(image)):
                pixels = pixels + image[n]
            print (str(num), pixels)
            im_nm.insert(num,list500_names[num])            
            im_pix.insert(num,pixels)
        time.sleep(2)


# In[ ]:

#Run the function
url_to_image(list500_names, list500_url) 


# In[ ]:

#Finally we create a dataframe in order to see the results of the function
dpix = {'company' : pd.Series(im_nm, index=[list500_num]),
      'pixels' : pd.Series(im_pix, index=[list500_num])}
images_pixels = pd.DataFrame(dpix)    
images_pixels.head(3) #we see the first 3 in the data frame
images_pixels.to_csv('images_pixels.csv', sep=';')


# In[ ]:

#In order to validate the html code we will use the w3 validator
#We will validate each url and then we will open the url of the validation page
#so as to extract the errors, the info warnings and the non-document-error io informations 
#First we create the empty lists we would use later on
num_errors = []
num_info_warnings = []
num_non_doc = [] 
nm = []
num_open_page = []
empty = ""


# In[ ]:

#Then we create the function that will pull the informations we want
def html_validation (list500_url,list500_names):
    from time import time # I used it to see how much time it does to run the function
    start = time ()
    for num in range(len(list500_names)):
        line = list500_url[num] 
        url_check = "https://validator.w3.org/nu/?doc=https://" + line
        browser = urllib2.build_opener()
        browser.addheaders = [('User-agent', 'Mozilla/5.0')]
        response = browser.open(url_check)
        html_check = response.read()
        html_check
        check = str(html_check)
        er = 0
        err = 0
        errr = 0
        e = False
        if check != empty:
            e = True
            soup = BeautifulSoup(check,"lxml")
            o = 0
            keyf = []
            for row in soup.html.body.findAll('div'):
                keyf.insert(o,row)
                o = o + 1
            #print(len(keyf),list500_url[num], "site number: ", str(num))        
            if len(keyf) != 0:       
                    keyfin = str(keyf[2]) 
                    #the elements we need is in the 2nd div of the code
                    dol= re.findall('class="error"',keyfin)            
                    er = er + len(dol)
                    doll= re.findall('class="info warning"'
                                     ,keyfin)            
                    err = err + len(doll)
                    dolll= re.findall('class="non-document-error io"'
                                      ,keyfin)            
                    errr = errr + len(dolll)
        num_errors.insert(num,er)
        num_info_warnings.insert(num,err)
        num_non_doc.insert(num,errr)  
        nm.insert(num,num) 
        num_open_page.insert(num,e)
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'


# In[ ]:

#Now we will run the function we created
html_validation (list500_url,list500_names)


# In[ ]:

#After the checks we will create the dataframe with the informations we want
d8 = {'company' : pd.Series(list500_names, index=[nm]),
      'The_page_opened' : pd.Series(num_open_page, index=[nm])
      ,'number_of_errors' : pd.Series(num_errors, index=[nm]),
      'number_of_warning' : pd.Series(num_info_warnings, index=[nm])
      ,'non-document-error' : pd.Series(num_non_doc, index=[nm])}
html_val = pd.DataFrame(d8)    
html_val.head(3) 
html_val.to_csv('html_val.csv', sep=';')


# In[ ]:

#The next step is to take some informations from the fortune 500 site for each company
#In order to achieve that we should open the pages for each one of the sites seperately
#Since there is a pattern in the way the pages are named it shouldn't be difficult
#Firstly we should create the pattern with which we will download the pages
#By running the code we can see that the names of each comany are not 
#written exactly as we have saved them
#So we do need to alter the names first in order for the below function to run


# In[ ]:

#creating a new list with alterations in order for the names
#to match the ones that fortune 500 uses so that we can download the html page
list_company_name_new = []
for num in range (0,500):
    cn = list_company_name[num]
    cn = cn.replace(" ", "-")
    cn = cn.replace("&", "")
    cn = cn.replace("’", "")
    cn = cn.replace(".", "-")
    cn = cn.replace("amp;", "")    
    company = cn.lower()
    list_company_name_new.insert(num,cn)


# In[ ]:

fortune_pages = []
def fortune500 (list_company_name_new):
    from time import time # I used it to see how much time it does to run the function
    start = time ()
    for num3 in range (0,500):
        i = str (num3 +1)    
        companyname =  list_company_name_new[num3]
        browser = urllib2.build_opener() 
        #because i work from different computers with different 
        #pyhton version some commands are not recognizable in each version
        browser.addheaders = [('User-agent', 'Mozilla/5.0')]
        site_fortune = "http://beta.fortune.com/fortune500/"+companyname+"-"+ i    
        page_fortune = browser.open(site_fortune)
        html_fortune = page_fortune.read()    
        #print("fortune page for company: ", list_company_name_new[num3],i)
        fortune_pages.insert(num3, html_fortune)
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'
    print 'The lists are ready in ', duration, ' seconds'


# In[ ]:

#Run the function we created
fortune500 (list_company_name_new)


# In[ ]:

#Now that we have opened the url we are going to extract 
#some informations that we need from them
#In order to do that initially we have to create 
#the variables we will need
keyf =[]
keyfaw = []
per =[]
rev_dol = []
prof_dol = []
assets_dol = []
tse_dol = []
tse_per = []
mar_dol = []
market = []
nm = []
ln = []
urln = []
empty = []
pef = []
pe_rat =[]
pr_r = []
peratio = []
empty = []
keyfawin = 0


# In[ ]:

def fortune_metrics (list_company_name,list_company_website):
    for n in range (0,500):          
        print("site",str(n), list_company_website[n])
        x = 0        
        nm.insert(x,n)
        ln.insert(x,list_company_name[n])
        urln.insert(x,list_company_website[n])
        files = fortune_pages[n]
        soup = BeautifulSoup(files, 'lxml')     
        ###############################################
        o=0
        for row in soup.html.body.findAll('tbody'):
            keyf.insert(o,row)
            o = o + 1
        keyfin = keyf[0]  #the elements we need is in the first tbody of the code  
        keyfon = keyf[1]
        data = keyfin.findAll('td')
        ##################################
        # revenue
        two = str(data[1]) 
        # revenue in dollars we need to extract this
        revdol= re.findall('>\$(.+?)</td>',two) 
        #we keep only the numbers
        if revdol[0] != empty:
            w = revdol[0]
            a = w.replace("[", "")
            r = a.replace("]","")
            rev_dol.insert(x,r)
        else:
            rev_dol.insert(x,'not available')
        five = str(data[5])
        #################################
        # profit in dollars we need to extract this   
        profdol= re.findall('>\$(.+?)</td>',five) 
        #we keep only the numbers
        if profdol != empty:
            w = profdol[0]
            a = w.replace("[", "")
            p = a.replace("]","")
            prof_dol.insert(x,p)
        else:
            prof_dol.insert(x,'not available')
        ###############################
        #assets in dollard
        eight = str(data[7]) #assets in dollars we need to extract this
        assetsdol= re.findall('>\$(.+?)</td>',eight) 
        #we keep only the numbers
        if assetsdol != empty:
            w = assetsdol[0]
            a = w.replace("[", "")
            ass = a.replace("]","")
            assets_dol.insert(x,ass)
        else:
            assets_dol.insert(x,'not available')
        ###################################
       #Total Stockholder Equity ($M)    
        eleven = str(data[10]) 
        #Total Stockholder Equity ($M) in dollars we need to extract this
        tsedol= re.findall('>\$(.+?)</td>',eleven) 
        #we keep only the numbers
        if tsedol != empty:
            w = tsedol[0]
            a = w.replace("[", "")
            ts = a.replace("]","")
            tse_dol.insert(x,ts)
        else:
            tse_dol.insert(x,'not available')
        ########################################
        # market value
        fourteen = str(data[13]) 
        # market value in dollars we need to extract this
        mardol= re.findall('>\$(.+?)</td>',fourteen) 
        #we keep only the numbers
        if mardol != empty:
            w = mardol[0]
            a = w.replace("[", "")
            mar = a.replace("]","")
            mar_dol.insert(x,mar)
        else:
            mar_dol.insert(x,'not available')
        ##############################################################    
        datao = keyfon.findAll('td')        
        # Profit as % of Revenues
        twoo = str(datao[2]) 
        prof_rev= re.findall('>(.+?)%</td>',twoo) 
        #we keep only the numbers
        if  prof_rev[0] != empty:
            w = prof_rev[0]
            a = w.replace("[", "")
            r = a.replace("]","")
            pr_r.insert(x,r)
        else:
            pr_r.insert(x,'not available')
        x = x + 1
    print "The function is complete!"


# In[ ]:

fortune_metrics (list_company_name,list_company_website)


# In[ ]:

d9 = {'company' : pd.Series(ln, index=[nm]),
      'Revenues $' : pd.Series(rev_dol, index=[nm]),
      'Profits $' : pd.Series(prof_dol, index=[nm]),
      'Assets $' : pd.Series(assets_dol, index=[nm]),
      'Total Stockholder Equity $' : pd.Series(tse_dol, index=[nm]),      
'Proft_%_Revenues' : pd.Series(pr_r, index=[nm]),
      'Market value $' : pd.Series(mar_dol, index=[nm])}
fort500 = pd.DataFrame(d9)    
fort500.head(3)
fort500.to_csv('fort500.csv', sep=';')


# In[ ]:

result = pd.merge(fort500, html_val, how='inner', on=['company', 'company'])
result2 = pd.merge(social_media, fre, how='inner', on=['company', 'company'])
result3 = pd.merge(sites_links, images_pixels, how='inner', on=['company', 'company'])
result4 = pd.merge(images_types, loading_time, how='inner', on=['company', 'company'])
result5 = pd.merge(result,result2 , how='inner', on=['company', 'company'])
result6 = pd.merge(result3, result4, how='inner', on=['company', 'company'])
final = pd.merge(result5, result6, how='inner', on=['company', 'company'])
final.head(3)


# In[ ]:

final.to_csv('total_500_final.csv', sep=';')


# In[ ]:

data500 = pd.read_csv("total_500_final.csv", sep=';') 


# In[ ]:

data500.head(3)


# In[ ]:



