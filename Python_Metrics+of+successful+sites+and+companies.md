

```python
#First we import the libraries we will need
import urllib
import urllib2
import time
import os
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```


```python
#First of all we need to find all the name of the sites that belong to fortune 500. This can happen if we seperate
#The information needed from the below link
url = "http://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites"
list_company_number =[]
list_company_name = []
list_company_website = []
list500_sites = []
list500_names = []
list500_num = []
list500_url = []
```


```python
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
```


```python
# After creating the function we should now test that it actually works correctly
websites (url)
```

    The lists are ready in  1.2  seconds
    The lists are ready in  0.0  minutes
    


```python
#Try to validate each page url #pip install validators
import validators
nv = 0
for num in range(len(list_company_website)):
    line = 'http://' + str(list_company_website[num])
    x = validators.url(line)    
    if x != True:
        nv = nv +1
print "The validation is complete! There were" , nv, "not valid pages"
```

    The validation is complete! There were 0 not valid pages
    


```python
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
    #print (url2)
    list500_names.insert(i,lcn)
    list500_url.insert(i,lc)
    list500_num.insert(i,k)
    if i == 118 or i == 464:#The site 118(119) has a problem and the whole code is stacking 
        #when I run it so we will thing of this site as a not downloadable
        list500_sites.insert(i,0)
        #print ("The site " + k + " has NOT been downloaded!")
    else:
        #an exception might be thrown, so the code should be in a try-except block
        try:
            response2=browser2.open(url2)
        except Exception: # this describes what to do if an exception is thrown
            list500_sites.insert(i,0)
            print ("The site " + str(i) + " has NOT been downloaded!") 
            continue     
            #read the response in html format. This is essentially a long piece of text
        myHTML2=response2.read()
        list500_sites.insert(i,myHTML2)
        #wait for 2 seconds
        time.sleep(2)
        #print ("The site " + k + " has been downloaded!")    
    #print "We saved: ",str(i + 1)," sites!"
    #print (len(list500_names),list500_names)
```

    The site 14 has NOT been downloaded!
    The site 15 has NOT been downloaded!
    The site 37 has NOT been downloaded!
    The site 62 has NOT been downloaded!
    The site 90 has NOT been downloaded!
    The site 97 has NOT been downloaded!
    The site 127 has NOT been downloaded!
    The site 135 has NOT been downloaded!
    The site 141 has NOT been downloaded!
    The site 161 has NOT been downloaded!
    The site 164 has NOT been downloaded!
    The site 209 has NOT been downloaded!
    The site 216 has NOT been downloaded!
    The site 239 has NOT been downloaded!
    The site 242 has NOT been downloaded!
    The site 275 has NOT been downloaded!
    The site 306 has NOT been downloaded!
    The site 326 has NOT been downloaded!
    The site 363 has NOT been downloaded!
    The site 414 has NOT been downloaded!
    The site 424 has NOT been downloaded!
    The site 441 has NOT been downloaded!
    The site 481 has NOT been downloaded!
    


```python
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
   
```


```python
#Now we will run the function to see which sites havent been downloaded
not_downloadables (list500_names,list500_sites)
d = {'company' : pd.Series(not_d, index=[num]),
     'number' : pd.Series(not_d_n, index=[num])}
nd = pd.DataFrame(d)    
nd
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Costco</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fannie Mae</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Target</td>
      <td>37</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HCA Holdings</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nike</td>
      <td>90</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tesoro</td>
      <td>97</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Arrow Electronics</td>
      <td>118</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Emerson Electric</td>
      <td>127</td>
    </tr>
    <tr>
      <th>8</th>
      <td>AutoNation</td>
      <td>135</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Southwest Airlines</td>
      <td>141</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Southern</td>
      <td>161</td>
    </tr>
    <tr>
      <th>11</th>
      <td>American Electric Power</td>
      <td>164</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Loews</td>
      <td>209</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PBF Energy</td>
      <td>216</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Toys “R” Us</td>
      <td>239</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Dominion Resources</td>
      <td>242</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Global Partners</td>
      <td>275</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PayPal Holdings</td>
      <td>306</td>
    </tr>
    <tr>
      <th>18</th>
      <td>News Corp.</td>
      <td>326</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Williams</td>
      <td>363</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Tractor Supply</td>
      <td>414</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Ameren</td>
      <td>424</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Old Republic International</td>
      <td>441</td>
    </tr>
    <tr>
      <th>23</th>
      <td>St. Jude Medical</td>
      <td>464</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Raymond James Financial</td>
      <td>481</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Now we will perfom a reliability test for the text that is 
#included in the html code of the company's page
from pattern import metrics
readability = []
rdb = []
```


```python
def readable (list500_names,list500_sites):
    for i in range (len(list500_names)):
            myHTML = list500_sites[i]
            if myHTML == 0:
                readability.insert(i,"n/a")
                rdb.insert(i,"n/a")
            else:
                a = metrics.flesch_reading_ease(myHTML) * 100
                a = round (a, 1)
                if a > 90:    
                    readability.insert(i,"Very easy")
                    rdb.insert(i,6)
                elif a > 80:
                    readability.insert(i,"Easy")
                    rdb.insert(i,5)
                elif a > 70:
                    readability.insert(i,"Fairly easy")
                    rdb.insert(i,4)
                elif a > 60:
                    readability.insert(i,"Standard")
                    rdb.insert(i,3)
                elif a > 50:
                    readability.insert(i,"Fairly difficult")
                    rdb.insert(i,2)
                elif a > 30:
                    readability.insert(i,"Difficult")
                    rdb.insert(i,1)
                else:
                    readability.insert(i,"Very Confusing")
                    rdb.insert(i,0)                    
    print "The function is completed!"
```


```python
readable (list500_names,list500_sites)
```

    The function is completed!
    


```python
d1 = {'company' : pd.Series(list500_names, index=[list500_num]),
      'url' : pd.Series(list500_url, index=[list500_num]),
      'Readability' : pd.Series(readability, index=[list500_num]),
      'Readability_index' : pd.Series(rdb, index=[list500_num])}
fre = pd.DataFrame(d1)    
fre.tail(3) #we see the first 3 in the data frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Readability</th>
      <th>Readability_index</th>
      <th>company</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>498</th>
      <td>Very Confusing</td>
      <td>0</td>
      <td>NVR</td>
      <td>www.nvrinc.com</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Very Confusing</td>
      <td>0</td>
      <td>Cincinnati Financial</td>
      <td>www.cinfin.com</td>
    </tr>
    <tr>
      <th>500</th>
      <td>Very Confusing</td>
      <td>0</td>
      <td>Burlington Stores</td>
      <td>www.burlingtonstores.com</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
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
                #print(str(i),"no")
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
```


```python
#Now we will run the function for the 25 first sites for starters
socialmedia (list500_sites,list500_names,list500_url)
```

    The lists are completed in  0.0  minutes
    The lists are ready in  0.259  seconds
    


```python
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
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>facebook</th>
      <th>instagram</th>
      <th>linkedin</th>
      <th>pinterest</th>
      <th>twitter</th>
      <th>youtube</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>497</th>
      <td>NVR</td>
      <td>TRUE</td>
      <td>TRUE</td>
      <td>FALSE</td>
      <td>TRUE</td>
      <td>TRUE</td>
      <td>TRUE</td>
    </tr>
    <tr>
      <th>498</th>
      <td>Cincinnati Financial</td>
      <td>TRUE</td>
      <td>FALSE</td>
      <td>FALSE</td>
      <td>FALSE</td>
      <td>FALSE</td>
      <td>FALSE</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Burlington Stores</td>
      <td>TRUE</td>
      <td>TRUE</td>
      <td>FALSE</td>
      <td>TRUE</td>
      <td>TRUE</td>
      <td>TRUE</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create the lists we will need for the data frame
l_nm = []
l_ex = []
l_in = []
l_t = []
nm = []
l_url = []
```


```python
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
```


```python
#Run the function in order to find the external, 
#internal and total links of each site
#For now we are running for the first 25 sites only
links (list500_sites,list500_names,list500_url)
```

    The lists are ready in  0.0  minutes
    The lists are ready in  0.088  seconds
    


```python
#Create a dataframe so as to be able to see 
#the results of the function we run
d3 = {'company' : pd.Series(l_nm, index=[nm]),
      'external' : pd.Series(l_ex, index=[nm]),
      'internal' : pd.Series(l_in, index=[nm]),
     'total links' : pd.Series(l_t, index=[nm])}
sites_links = pd.DataFrame(d3)    
sites_links.tail(3) #we see the first 3 in the data frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>external</th>
      <th>internal</th>
      <th>total links</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>497</th>
      <td>NVR</td>
      <td>5</td>
      <td>29</td>
      <td>34</td>
    </tr>
    <tr>
      <th>498</th>
      <td>Cincinnati Financial</td>
      <td>3</td>
      <td>73</td>
      <td>76</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Burlington Stores</td>
      <td>16</td>
      <td>168</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>




```python
#The initial lists we will need in order 
#to calculate the loading time
lt_nm = [] 
lt_time = []
nm = []
lt_url = []
```


```python
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
        if num == 118 or num == 464:
            #The site 118(119) has a problem and the whole code 
            #is stacking when I run it so we will thing of this 
            #site as a not downloadable
            lt_nm.insert(num,list500_names[num])            
            lt_time.insert(num,'n/a')
            nm.insert(num,num)
            lt_url.insert(num,list500_url[num])
            #print ("The site " + str(num) + " has NOT been loaded!")
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
```


```python
#running the function for the first 25 sites
loadtime (list_company_website,list500_names,list500_url)
```

    The site 14 has NOT been loaded!
    The site 15 has NOT been loaded!
    The site 37 has NOT been loaded!
    The site 62 has NOT been loaded!
    The site 90 has NOT been loaded!
    The site 97 has NOT been loaded!
    The site 127 has NOT been loaded!
    The site 135 has NOT been loaded!
    The site 141 has NOT been loaded!
    The site 161 has NOT been loaded!
    The site 164 has NOT been loaded!
    The site 204 has NOT been loaded!
    The site 209 has NOT been loaded!
    The site 216 has NOT been loaded!
    The site 242 has NOT been loaded!
    The site 275 has NOT been loaded!
    The site 306 has NOT been loaded!
    The site 326 has NOT been loaded!
    The site 363 has NOT been loaded!
    The site 414 has NOT been loaded!
    The site 424 has NOT been loaded!
    The site 441 has NOT been loaded!
    The site 481 has NOT been loaded!
    The function is completed!
    


```python
#creating the data frame with the loading times
d4 = {'company' : pd.Series(lt_nm, index=[nm]),
      'loading time' : pd.Series(lt_time, index=[nm])}
loading_time = pd.DataFrame(d4)    
loading_time.head(3) #we see the first 3 in the data frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>loading time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Walmart</td>
      <td>0.449</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exxon Mobil</td>
      <td>5.376</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apple</td>
      <td>0.021</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
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
```


```python
#Then we run the function for the first 20 sites for now
images (list500_sites,list500_names,list500_url)
```

    The lists are ready in  0.1  minutes
    The lists are ready in  3.341  seconds
    


```python
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
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>.bmp</th>
      <th>.dib</th>
      <th>.gif</th>
      <th>.jpe</th>
      <th>.jpeg</th>
      <th>.jpg</th>
      <th>.png</th>
      <th>.tif</th>
      <th>.tiff</th>
      <th>company</th>
      <th>total images</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>55</td>
      <td>153</td>
      <td>153</td>
      <td>63</td>
      <td>46</td>
      <td>10</td>
      <td>0</td>
      <td>Walmart</td>
      <td>480</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>Exxon Mobil</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>Apple</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Now we will find the different dimensions that each site uses
#initially we create the empty lists we will need
nm = []
s_comp = []
s_dimensions = []
s_times = []
s_tt_dif_dim = []
ht = [] #list of different heights in each case
wt = [] #list of different widths in each case
h_w = [] # combinations of height and width
dif_size = []  
un_size = [] 
s_url = []
```


```python
#With the below function we will gather 
#in a variable all the different dimensions 
#and in another one all the times that each 
#dimension occures for each html code
def find_dif_sizes (list_company_website,list500_names,list500_url):
    from time import time # I used it to see how much time it does to run the function
    start = time ()
    for num in range(len(list500_names)):
            nm.insert(num,num)                  
            s_comp.insert(num,list500_names[num])
            s_url.insert(num,list500_url[num])
            myHTML = list500_sites[num] 
            if myHTML == 0:
                s_dimensions.insert(num,0)
                s_times.insert(num,0)    
            else: 
                soup = BeautifulSoup(myHTML, "lxml")
                # we create 2 local variables so as to gather the 
                #different dimensions and occurencies  of each page seperately
                s_dimensions_local = []
                s_times_local = []
                hw = 0 
                # we use it for the lists of height and width
                # find all the img in the first site html.Since in some 
                #cases either the height or the width is missing we would 
                #like to keep only the ones that have both dimensions
                for tag in soup.find_all('img'):
                    h = tag.attrs.get('height', None)
                    w = tag.attrs.get('width', None)
                    #we use if to check which ones have both 
                    if h != None:
                        if w != None:
                            ht.insert(hw,h)
                            wt.insert(hw,w)
                            hw = hw + 1                        
                hw2 = 0
                for l in range(len(ht)):
                    h_w_c = ht[l] + 'x' + wt[l]    
                    #we create a str with the form (300x300) 
                    #so as to be more easily to read later on 
                    h_w.insert(hw2,h_w_c)  
                    #we put it in a new list
                    hw2 = hw2 + 1    
                if h_w == []:#we check if there are not any dimensions available
                    nm.insert(num,num)                  
                    s_comp.insert(num,list500_names[num])
                    s_dimensions.insert(num,0)
                    s_times.insert(num,0)    
                if h_w != []:#now we continue with the cases 
                    #where the dimensions are indeed available             
                    from collections import Counter
                    hw_unique = Counter(h_w)
                    hw_unique2 = str(hw_unique) 
                    #the unique different dimensions for the specific site
                    #Due to the fact that we are talking about 
                    #a list we have to split the parts we need 
                    split1 = hw_unique2.split('{')
                    a = split1[1]
                    split2 = a.split('}')
                    b = split2[0]
                    split3 = b.split(',')
                    finalsplit = []
                    fs = []
                    z = 0
                    m = 1
                    j = 0
                    z1 = 0
                    m1 = 1
                    #each of the items in split3 has a form '300x300 : 15'
                    #and in order to create the dataframe we have 
                    #to split this form and keep the informations in different list
                    for numb in split3:                
                        oldstring = numb
                        newstring = oldstring.replace("'", "")
                        new = newstring.replace("'","")
                        string = new.replace(" ","")
                        finalstring = string.split(':')
                        #the finalstring is a list that contains the dimensions
                        #and the occurencies in order toseperate in different
                        #lists we create an additional loop
                        for xx in range(len(finalstring)):
                            ax = finalstring[xx]
                            if 'x' in ax:
                                s_dimensions_local.insert(z1,finalstring[xx])
                                z1 = z1 + 1
                            else:
                                s_times_local.insert(m1,finalstring[xx])
                                m1 = m1 + 1  
                    #Now we can add to the lists the parts we created so as
                    #to have them all gathered together             
                    s_dimensions.insert(num,s_dimensions_local)
                    s_times.insert(num,s_times_local)                
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'
    print 'The lists are ready in ', duration, ' seconds'
```


```python
#Run the function for the first 20 sites
find_dif_sizes (list500_sites,list500_names,list500_url)
```

    The lists are ready in  1.4  minutes
    The lists are ready in  81.813  seconds
    


```python
#Find the unique different image dimensions and put them on a list
def unique_dif_sizes (s_dimensions,list500_names):
    ds = 0
    for num in range(len(list500_names)):
        asw = s_dimensions[num]
        if asw != 0 :
            for s in range(len(asw)):
                ss = asw[s]
                dif_size.insert(ds,ss)
                ds = ds + 1    
    dsu = 0
    for i in dif_size:
        if i not in un_size:
            un_size.insert(dsu,i)
            dsu = dsu + 1
    print(un_size)          
```


```python
#Run the function unique_dif_sizes
unique_dif_sizes (s_dimensions,list500_names)
```

    ['15x75', '44x556', '1x1', '800x1200', '24pxx133px', '21pxx173px', '49x49', '50x45', '29x29', '115x223', '160x233', '41x192', '28x221', '300x993', '15x12', '70x70', '170x300', '83x250', '115x150', '150x150', '11x8', '75x85', 'x', '23x27', '262x100%', '86x226', '280x691', '42x168', '1x700', '27x156', '24x24', '1x10', '10x1', '8x10', '1x660', '19x1', '17x16', '25x125', '2x2', '397x700', '640x1920', '843x1900', '76x209', '53x84', '61x120', '35x35', '10pxx10px', '107x128', '197x875', '403x961', '20x113', '40x90', '0x0', '421x638', '24x83', '160x300', '160x475', '979x833', '430x1000', '210x320', '47x123', '32x116', '576x1024', '681x1024', '175pxx978px', '20x20', '100x100', '80x100', '450x1600', '200x1600', '16x16', '468x990', '42x86', '360x360', '25x61', '51pxx353px', '184x176', '40x148', '165x175', '80x96', '26x76', '16x87', '113x350', '98x113', '280x400', '1080x1295', '533x800', '610x800', '400x600', '148x169', '64x236', '47x236', '25x29', '28x28', '170x252', '199pxx248px', '45x91', '26x151', '16x32', '43x43', '46x223', '399pxx724px', '400x980', '45x45', '45x46', '45x269', '500x500', '484x790', '125x125', '250x480', '418x1300', '396x900', '233x389', '32x32', '18x75', '48x90', '30x113', '281x530', '11x16', '527x922', '7x7', '7x4', '12x7', '70x200', '7x19', '375x753', '460x1180', '195x537', '324x1000', '29x1000', '46x48', '71x234', '24x26', '4x983', '64x144', '20x146', '50x240', '160x225', '310x520', '175x290', '52x166', '420x1600', '169x308', '40x40', '154x268', '300x1600', '27x27', '360x640', '52x123', '52x136', '61x219', '34x115', '34x226', '100x165\\r\\n', '100x165', '4x169', '34x191', '34x78', '49x244', '34x125', '31x31', '10x10', '16x141', '42x63', '44x68', '43x72', '42x43', '37x65', '270x340', '42pxx42px', '396x960', '59x301', '42x55', '35x60', '50x50', '45x73', '27x18', '27x113', '27x718', '27x26', '172x150', '27x25', '277x247', '25x120', '29x140', '61x213', '1x110', '100x340', '13x235', '11x9', '12x235', '38x38', '140x240', '67x200', '30pxx30px', '130x126', '156x308', '14x147', '180x948', '323x948', '450x557', '700x1060', '523x2560', '412x2560', '420x2560', '700x2560', '513x939', '465x557', '106x940', '79x1060', '915x503', '530x2560', '55x55', '90x90', '105x184', '39x158', '230x354', '450x1450', '37x37', '110x140', '140x140', '315x560', '56x281', '754x2409', '399x680', '91x136', '21x134', 'autox100%', 'autox200', '40x350', '12x12', '48x91', '25x5', '2x213', '81x213', '25x15', '15x213', '18x85', '18x136', '18x138', '18x106', '132x762', '18x78', '15x25', '67x213', '18x60', '18x59', '18x52', '18x48', '93x213', '1350x1900', '44x44', '44x47', '48x48', '63x62', '135x240', '94x146', '337x727', '293x229', '8x13', '50x173', '340x229', '35x45', '148x150', '79x150', '96x108', '277x910', '265x35', '17x23', '22x980', '30x130', '24x258', '500x1280', '225x305', '30pxx283px', '200x200', '92x211', '900x2400', '900x900', '901x901', '272x400', '37x118', '210x420', '526x1400', '144x288', '165x141', '110x110', '662x1170', '25x20', '29x28', '642x615', '140x720', '768x615', '404x505', '70x360', '631x505', '46x660', '492x615', '6x4', '112x293', '44x334', '14x18', '260x427', '59x276', '9x30', '26x26', '18x18', '61x194', '327x986', '66x53', '19x155', '16x12', '56x56', '24x163', '57x63', '4x975', '1x975', '121x215', '129x129', '111x111', '42x206', '2x4', '396x208', '215x455', '53x221', '34x825', '34x165', '47x283', '82x301', '138x129', '92x118', '200x250', '30x150', '61x508', '110x258', '64x92', '118x74', '113x945', '37x262', '35x300', '20x200', '20x65', '43x960', '20x120', '8x16', '608x960', '152x263', '336x378', '40x125', '40x120', '2x13', '2x12', '24x1', '2x30', '72x179', '2x17', '6x1', '2x21', '22x22', '34x33', '62x107', '18x21', '17x17', '131x175', '124x195', '384x659', '85x95', '127x151', '8x8', '19x19', '280x660', '39x250', '279x466', '62x250', '513x800', '700x400', '80x43', '60x21', '80x53', '80x37', '23x140', '22x4', '45x4', '12x15', '21x6', '39x974', '169x144', '53x198', '34x129', '34x171', '34x116', '12x14', '27x83', '34x245', '34x104', '34x118', '407x397', '287x280', '104x400', '137x107', '34x192', '39x223', '52x325', '70x205', '52x338', '31x67', '88x194', '24x13', '100x265', '14x20', '269x1280', '14x196', '97x75', '67x92', '10pxx42px', '218x388', '350x800', '25x94', '280x960', '260x800', '260x2800', '40x143', '310x310', '74x70', '84x53', '621x621', '88x63', '100x196', '102x198', '100x175', '145x165', '300x768', '140x165', '496x991', '43x24', '250pxx735px', '480x1250', '218x291', '19x112', '19x201', '188x795', '480x374', '44x179', '378x153', '79x106', '55x110', '19x135', '19x258', '19x87', '319x178', '307x158', '19x192', '23x64', '101x218', '280x410', '134x238', '255x255', '52x52', '255x537', '256x256', '427x1280', '23pxx23px', '52x100', '219x283', '350x975', '1050x990', '33x301', '238x660', '52x233', '288x768', '51x328', '343x1347', '253x423', '345x1362', '14x15', '288x476', '150x300', '300x940', '68x182', '114x200', '691x560', '87x94', '170x417', '331x600', '305x655', '780x1440', '305x665', '70x132', '45x134', '2000x2000', '66x179', '30x30', '786x1487', '786x1490', '785x1490', '144x144', '55x323', '512x512', '328x900', '106x148', '139x289', '120x225', '156x338', '157x343', '157x578', '111x150', '43x141', '130x175', '20x94', '285x640', '335x647', '8x7', '207x314', '20x21', '573x959', '57x45', '57x44', '188x479', '57x96', '57x95', '39x150', '57x104', '57x100', '57x67', '57x136', '57x38', '57x48', '57x43', '57x42', '57x84', '57x114', '57x58', '57x99', '57x97', '57x68', '57x27', '57x105', '57x103', '57x66', '57x65', '57x62', '57x60', '57x69', '31x150', '57x137', '57x131', '57x35', '57x37', '57x32', '57x82', '57x71', '57x73', '57x76', '57x77', '29x150', '57x126', '57x122', '57x36', '57x49', '57x40', '426x712', '57x46', '49x150', '57x87', '57x86', '57x80', '57x83', '57x110', '57x115', '57x50', '57x51', '57x56', '57x57', '11x12', '25x2', '76x85', '11x140', '40x24', '14x121', '38x131', '42x294', '10x18', '76x84', '76x83', '76x2', '16x200', '224x294', '430x1920', '300x300', '25x25', '33x144', '350x712', '38x276', '265x750', '35x97', '72x136', '50x167', '46x176', '100x300', '75x150', '435x1170', '96x217', '460x1170', '500x1170', '566x581', '208x292', '280x290', '39pxx40px', '84x158', '9x9', '10x5', '15x7', '28x71', '1x20', '4x54', '28x80', '22x116', '62x1', '28x149', '28x100', '50x140', '229x722', '0x1', '140x220', '44x70', '240x380', '300x960', '475x1200', '110x350', 'autox400', '53x190', '58x150', '125x296', '159x147', '72x192', '100%x100%', '181x984', '74x347', '284x308', '386x962', '261x649', '14pxx14px', '13pxx46px', '42x186', '12x244', '48x163', '515x1065', '172x254', '321x360', '600x2000', '122x142', '603x2000', '451x1500', '450x1500', '379x1265', '24x129', '24x71', '210x210', '82x206', '450x640', '50x156', '482x557', '300x600', '80x80', '11x72', '181x314', '38x135', '72x202', '546x970', '98x75', '192x342', '14x14', '111x418', '74x400', '30x374', '290x940', '600x1200', '400x400', '225x300', '425x650', '425x640', '348x378', '357x308', '26x243', '620x1280', '21x21', '426x710', '1080x1920', '23x23', '326x580', '734x1280', '1200x1800', '21x22', '21x23', '12pxx12px', '120x120', '46x46', '318x460', '370x630', '75x171', '105x530', '781x1800', '50x100', '79x126', '130x176']
    


```python
#The lists we will need for the next function
t_f_s = []
ttf = []
nm = []
com = []
```


```python
#Function in order to check whether or not each 
#company has these dimensions
def dimensions_per_company (un_size,list500_names):
    from time import time 
    # I used it to see how much time it does to run the function
    start = time ()
    #t_f_s.insert(0,un_size)
    #ttf.insert(0,t_f_s)
    for num in range(len(list500_names)): 
        #print(str(num))
        s1a = s_dimensions[num] 
        #dimensions of site num
        where = [] #empty list
        wh = 0
        haveornot = []
        for er in range (len(un_size)):
            if s1a != 0 :
                for sizea in s1a:
                    if sizea == un_size[er]:
                        where.insert(wh,str(er))
                        wh = wh +1
                        break
            if str(er) in where:
                haveornot.insert(er,True)                    
            else:
                haveornot.insert(er,False)
                    
        t_f_s.insert(num,haveornot)
        ttf.insert(num,t_f_s)
        nm.insert(num,num)
        com.insert(num,list500_names[num])
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'
    print 'The lists are ready in ', duration, ' seconds'
```


```python
#Run the function dimensions_per_company
dimensions_per_company (un_size,list500_names)
```

    The lists are ready in  0.1  minutes
    The lists are ready in  3.699  seconds
    


```python
#Create an initial dataframe where we will add the sizes later on
d6 = {'company' : pd.Series(com, index=[nm])}
sizess = pd.DataFrame(d6)    
sizess.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Walmart</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exxon Mobil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apple</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Now we want to break the variable t_f_s 
#in order to add the columns to the dataframe                  
#Finally we create the data frame with the elements we found 
def final_dimensions_dataframe (un_size,t_f_s,list500_names):
    from time import time 
    # I used it to see how much time it does to run the function
    start = time ()
    for q in range(len(un_size)):
        names = un_size[q]
        var = []
        for num in range(len(list500_names)):
            a = t_f_s[num]
            var.insert(num,a[q])
        sizess[names] = pd.Series(var, index=sizess.index) 
    end = time ()
    duration = round (end - start, 3)
    minutes = round (duration /60, 1)
    print 'The lists are ready in ', minutes, ' minutes'
    print 'The lists are ready in ', duration, ' seconds'
```


```python
#Run the function final_dimensions_dataframe
final_dimensions_dataframe (un_size,t_f_s,list500_names)
```

    The lists are ready in  0.0  minutes
    The lists are ready in  0.414  seconds
    


```python
sizess.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>15x75</th>
      <th>44x556</th>
      <th>1x1</th>
      <th>800x1200</th>
      <th>24pxx133px</th>
      <th>21pxx173px</th>
      <th>49x49</th>
      <th>50x45</th>
      <th>29x29</th>
      <th>...</th>
      <th>120x120</th>
      <th>46x46</th>
      <th>318x460</th>
      <th>370x630</th>
      <th>75x171</th>
      <th>105x530</th>
      <th>781x1800</th>
      <th>50x100</th>
      <th>79x126</th>
      <th>130x176</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>497</th>
      <td>NVR</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>498</th>
      <td>Cincinnati Financial</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>...</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Burlington Stores</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>...</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 706 columns</p>
</div>




```python
#Now we would like to find the words in the text 
#and the unique words of each html page
#First of all we need to have a dictionary with which 
#we would check if the word we found truly exists
#The dictionary is available in the internet from a 
#github acount from where we are going to read it
url_dictionary = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
browser = urllib2.build_opener()
browser.addheaders = [('User-agent', 'Mozilla/5.0')]
response = browser.open(url_dictionary)
html_dictionary = response.read()
html_dictionary
dicti = str(html_dictionary)
#dicti
```


```python
#dict_new = dicti.split("\\n")
dict_new = dicti.split("\n")
dict_new[49] 
#the first 49 parts are not words so we have to remove them from the list
```




    'a1'




```python
dict_final = []
df = 0
for i in range (50,len(dict_new)):
    forfinal = dict_new[i]
    forfinal = forfinal.replace("'","")
    dict_final.insert(df,forfinal)
    df = df + 1
dict_final[0] 
#This is the original dictionary with which we will check each word
```




    'aa'




```python
#And now we will find each html file which words has inside
empty = []
wordsin = []
ocin = []
def html_which_word (list500_names):
    from time import time 
    # I used it to see how much time it does to run the function
    start_t = time()
    for num in range(len(list500_sites)):
            line = list500_sites[num] 
            if line == 0:
                wordsin.insert(num,0)
                ocin.insert(num,0)                 
            else: 
                wordcount={}
                simeiastiksis = ["/",".",",","=",">","<","?","|",":"
                                 ,"_","]","[","$","&","%","(",")","{"
                                 ,"}",'"',";","\\","-","!","+","#","="
                                 ,"@","^","*","'"]
                for ss in range(len(simeiastiksis)):
                    simeio = simeiastiksis[ss]     
                    line = line.replace(simeio, " ")
                for word1 in line.split():
                    word1 = word1.lower()
                    if word1 in dict_final:
                        if word1 not in wordcount:
                            wordcount[word1] = 1
                        else:
                            wordcount[word1] += 1     
                wordsin_local = []
                wl = 0
                ocin_local = []
                for k,v in wordcount.items():
                       #print (k,v)
                       wordsin_local.insert(wl,str(k))
                       ocin_local.insert(wl,str(v))
                       wl = wl + 1
                wordsin.insert(num,wordsin_local) 
                # final list with all the words in each site
                ocin.insert(num,ocin_local)  
                #final list with all the occurencies of the words in each site
            #print('The site', str(num +1), ' has been checked')
    end_t = time()
    total_t = round(end_t - start_t,3)
    total_ = round(total_t / 60,1)
    print('finished ',str(x) ,' sites in: ', str(total_),' minutes')
```


```python
html_which_word (list500_names)
```

    ('finished ', 'True', ' sites in: ', '197.6', ' minutes')
    


```python
#Create the dataframe for the words and unique words
d7 = {'company' : pd.Series(list500_names, index=[nm])}
wordss = pd.DataFrame(d7)    
wordss.head(3) 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Walmart</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exxon Mobil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apple</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create the two lists we will need in order to make the dataframe
l1 = []
l2 = []
for num in range(len(list500_names)):
        line = list500_sites[num] 
        if wordsin[num] == 0 :             
            l1.insert(num,'n/a')
            l2.insert(num,'n/a')
        else:
            total_words = len(wordsin[num])
            occurencies = ocin[num] 
            l1.insert(num,total_words)
            count = 0 
            for a in occurencies :
                if a == '1':
                    count = count + 1
            l2.insert(num,count)
wordss['total_words'] = pd.Series(l1, index=sizess.index)
wordss['unique_words'] = pd.Series(l2, index=sizess.index)          
wordss.head(3)                        
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>total_words</th>
      <th>unique_words</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Walmart</td>
      <td>1646</td>
      <td>443</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exxon Mobil</td>
      <td>801</td>
      <td>154</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apple</td>
      <td>397</td>
      <td>123</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
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
```


```python
#Now we will run the function we created
html_validation (list500_url,list500_names)
```

    The lists are ready in  37.0  minutes
    


```python
#After the checks we will create the dataframe with the informations we want
d8 = {'company' : pd.Series(list500_names, index=[nm]),
      'The_page_opened' : pd.Series(num_open_page, index=[nm])
      ,'number_of_errors' : pd.Series(num_errors, index=[nm]),
      'number_of_warning' : pd.Series(num_info_warnings, index=[nm])
      ,'non-document-error' : pd.Series(num_non_doc, index=[nm])}
html_val = pd.DataFrame(d8)    
html_val.head(3) 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>The_page_opened</th>
      <th>company</th>
      <th>non-document-error</th>
      <th>number_of_errors</th>
      <th>number_of_warning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>Walmart</td>
      <td>0</td>
      <td>879</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>Exxon Mobil</td>
      <td>0</td>
      <td>55</td>
      <td>29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>Apple</td>
      <td>0</td>
      <td>14</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
#The next step is to take some informations from the fortune 500 site for each company
#In order to achieve that we should open the pages for each one of the sites seperately
#Since there is a pattern in the way the pages are named it shouldn't be difficult
#Firstly we should create the pattern with which we will download the pages
#By running the code we can see that the names of each comany are not 
#written exactly as we have saved them
#So we do need to alter the names first in order for the below function to run
```


```python
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
```


```python
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
```


```python
#Run the function we created
fortune500 (list_company_name_new)
```

    The lists are ready in  21.6  minutes
    The lists are ready in  1295.917  seconds
    


```python
#Now that we have opened the url we are going to extract 
#some informations that we need from them
#In order to do that initially we have to create 
#the variables we will need
keyf =[]
per =[]
rev_dol = []
rev_per = []
prof_dol = []
prof_per = []
assets_dol = []
assets_per = []
tse_dol = []
tse_per = []
mar_dol = []
mar_per = []
market = []
nm = []
ln = []
urln = []
empty = []
```


```python
def fortune_metrics (list_company_name,list_company_website):
    x = 0
    for n in range (0,500):   #we put 25 for testing
        nm.insert(x,x)
        ln.insert(x,list_company_name[n])
        urln.insert(x,list_company_website[n])
        files = fortune_pages[x]
        soup = BeautifulSoup(files,"lxml")
        o=0
        for row in soup.html.body.findAll('tbody'):
            keyf.insert(o,row)
            o=o+1
        keyfin = keyf[0] 
        #the elements we need is in the first tbody of the code
        data = keyfin.findAll('td')

        one = str(data[0]) 
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
        tria = str(data[2])
        # revenue in percentage we need to extract this as well
        revper= re.findall('>(.+?)%</td>',tria) 
        #we keep only the numbers
        if revper != empty:    
            w = revper[0]
            a = w.replace("[", "")
            r1 = a.replace("]","")    
            rev_per.insert(x,r1) 
        else:
            rev_per.insert(x,'not available')
        four = str(data[3])   # profit     
        five = str(data[4])   
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
        six = str(data[5])    
        # profit in percentage we need to extract this as well   
        profper = re.findall('>(.+?)%</td>',six) 
        #we keep only the numbers
        if profper != empty:
            w = profper[0]
            a = w.replace("[", "")
            p1 = a.replace("]","")    
            prof_per.insert(x,p1)
        else:
            prof_per.insert(x,'not available')
        seven = str(data[6]) #assets
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
        ten = str(data[9]) #Total Stockholder Equity ($M)    
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
        thirteen = str(data[12]) # market value
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
        x = x + 1
    print "The function is complete!"
```


```python
fortune_metrics (list_company_name,list_company_website)
```

    The function is complete!
    


```python
d9 = {'company' : pd.Series(ln, index=[nm]),
      'Revenues $' : pd.Series(rev_dol, index=[nm]),
      'Revenues %' : pd.Series(rev_per, index=[nm]),
      'Assets $' : pd.Series(assets_dol, index=[nm]),
      'Total Stockholder Equity $' : pd.Series(tse_dol, index=[nm]),
      'Market value $' : pd.Series(mar_dol, index=[nm])}
fort500 = pd.DataFrame(d9)    
fort500.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Assets $</th>
      <th>Market value $</th>
      <th>Revenues $</th>
      <th>Revenues %</th>
      <th>Total Stockholder Equity $</th>
      <th>company</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>199,581</td>
      <td>215,356</td>
      <td>482,130</td>
      <td>-0.7</td>
      <td>80,546</td>
      <td>Walmart</td>
    </tr>
    <tr>
      <th>1</th>
      <td>336,758</td>
      <td>347,129</td>
      <td>246,204</td>
      <td>-35.6</td>
      <td>170,811</td>
      <td>Exxon Mobil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>290,479</td>
      <td>604,304</td>
      <td>233,715</td>
      <td>27.9</td>
      <td>119,355</td>
      <td>Apple</td>
    </tr>
  </tbody>
</table>
</div>




```python
fort500.merge(html_val, left_on='company', right_on='company', how='outer')
fort500.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Assets $</th>
      <th>Market value $</th>
      <th>Revenues $</th>
      <th>Revenues %</th>
      <th>Total Stockholder Equity $</th>
      <th>company</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>199,581</td>
      <td>215,356</td>
      <td>482,130</td>
      <td>-0.7</td>
      <td>80,546</td>
      <td>Walmart</td>
    </tr>
    <tr>
      <th>1</th>
      <td>336,758</td>
      <td>347,129</td>
      <td>246,204</td>
      <td>-35.6</td>
      <td>170,811</td>
      <td>Exxon Mobil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>290,479</td>
      <td>604,304</td>
      <td>233,715</td>
      <td>27.9</td>
      <td>119,355</td>
      <td>Apple</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pd.merge(fort500, html_val, how='inner', on=['company', 'company'])
result2 = pd.merge(social_media, fre, how='inner', on=['company', 'company'])
result3 = pd.merge(wordss, sizess, how='inner', on=['company', 'company'])
result4 = pd.merge(images_types, loading_time, how='inner', on=['company', 'company'])
result5 = pd.merge(result, sites_links, how='inner', on=['company', 'company'])
result6 = pd.merge(result5, result2, how='inner', on=['company', 'company'])
result7 = pd.merge(result6, result3, how='inner', on=['company', 'company'])
final3 = pd.merge(result7, result4, how='inner', on=['company', 'company'])
final3.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Assets $</th>
      <th>Market value $</th>
      <th>Revenues $</th>
      <th>Revenues %</th>
      <th>Total Stockholder Equity $</th>
      <th>company</th>
      <th>The_page_opened</th>
      <th>non-document-error</th>
      <th>number_of_errors</th>
      <th>number_of_warning</th>
      <th>...</th>
      <th>.dib</th>
      <th>.gif</th>
      <th>.jpe</th>
      <th>.jpeg</th>
      <th>.jpg</th>
      <th>.png</th>
      <th>.tif</th>
      <th>.tiff</th>
      <th>total images</th>
      <th>loading time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>199,581</td>
      <td>215,356</td>
      <td>482,130</td>
      <td>-0.7</td>
      <td>80,546</td>
      <td>Walmart</td>
      <td>True</td>
      <td>0</td>
      <td>879</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>55</td>
      <td>153</td>
      <td>153</td>
      <td>63</td>
      <td>46</td>
      <td>10</td>
      <td>0</td>
      <td>480</td>
      <td>0.449</td>
    </tr>
    <tr>
      <th>1</th>
      <td>336,758</td>
      <td>347,129</td>
      <td>246,204</td>
      <td>-35.6</td>
      <td>170,811</td>
      <td>Exxon Mobil</td>
      <td>True</td>
      <td>0</td>
      <td>55</td>
      <td>29</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>23</td>
      <td>5.376</td>
    </tr>
    <tr>
      <th>2</th>
      <td>290,479</td>
      <td>604,304</td>
      <td>233,715</td>
      <td>27.9</td>
      <td>119,355</td>
      <td>Apple</td>
      <td>True</td>
      <td>0</td>
      <td>14</td>
      <td>6</td>
      <td>...</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0.021</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 740 columns</p>
</div>




```python
final3.to_csv('total_500.csv', sep=';')
```


```python
data500 = pd.read_csv("total_500.csv", sep=';') 
```


```python
data500.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Assets $</th>
      <th>Market value $</th>
      <th>Revenues $</th>
      <th>Revenues %</th>
      <th>Total Stockholder Equity $</th>
      <th>company</th>
      <th>The_page_opened</th>
      <th>non-document-error</th>
      <th>number_of_errors</th>
      <th>...</th>
      <th>.dib</th>
      <th>.gif</th>
      <th>.jpe</th>
      <th>.jpeg</th>
      <th>.jpg</th>
      <th>.png</th>
      <th>.tif</th>
      <th>.tiff</th>
      <th>total images</th>
      <th>loading time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>199,581</td>
      <td>215,356</td>
      <td>482,130</td>
      <td>-0.7</td>
      <td>80,546</td>
      <td>Walmart</td>
      <td>True</td>
      <td>0</td>
      <td>879</td>
      <td>...</td>
      <td>0</td>
      <td>55</td>
      <td>153</td>
      <td>153</td>
      <td>63</td>
      <td>46</td>
      <td>10</td>
      <td>0</td>
      <td>480</td>
      <td>0.449</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>336,758</td>
      <td>347,129</td>
      <td>246,204</td>
      <td>-35.6</td>
      <td>170,811</td>
      <td>Exxon Mobil</td>
      <td>True</td>
      <td>0</td>
      <td>55</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>23</td>
      <td>5.376</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>290,479</td>
      <td>604,304</td>
      <td>233,715</td>
      <td>27.9</td>
      <td>119,355</td>
      <td>Apple</td>
      <td>True</td>
      <td>0</td>
      <td>14</td>
      <td>...</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0.021</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 741 columns</p>
</div>




```python

```
