

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
list500_sites = []
list500_names = []
list500_num = []
list500_url = []
```


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
    list500_names.insert(i,lcn)
    list500_url.insert(i,lc)
    list500_num.insert(i,k)
    if i == 118 or i == 464 or i == 70:
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
```

    The site 0 has been downloaded!
    The site 1 has been downloaded!
    The site 2 has been downloaded!
    The site 3 has been downloaded!
    The site 4 has been downloaded!
    The site 5 has been downloaded!
    The site 6 has been downloaded!
    The site 7 has been downloaded!
    The site 8 has been downloaded!
    The site 9 has been downloaded!
    The site 10 has been downloaded!
    The site 11 has been downloaded!
    The site 12 has been downloaded!
    The site 13 has been downloaded!
    The site 14 has been downloaded!
    The site 15 has NOT been downloaded from exception!
    The site 16 has been downloaded!
    The site 17 has been downloaded!
    The site 18 has been downloaded!
    The site 19 has been downloaded!
    The site 20 has been downloaded!
    The site 21 has been downloaded!
    The site 22 has been downloaded!
    The site 23 has been downloaded!
    The site 24 has been downloaded!
    The site 25 has been downloaded!
    The site 26 has been downloaded!
    The site 27 has been downloaded!
    The site 28 has been downloaded!
    The site 29 has been downloaded!
    The site 30 has been downloaded!
    The site 31 has been downloaded!
    The site 32 has been downloaded!
    The site 33 has been downloaded!
    The site 34 has been downloaded!
    The site 35 has been downloaded!
    The site 36 has been downloaded!
    The site 37 has been downloaded!
    The site 38 has been downloaded!
    The site 39 has been downloaded!
    The site 40 has been downloaded!
    The site 41 has been downloaded!
    The site 42 has been downloaded!
    The site 43 has been downloaded!
    The site 44 has been downloaded!
    The site 45 has been downloaded!
    The site 46 has been downloaded!
    The site 47 has been downloaded!
    The site 48 has been downloaded!
    The site 49 has been downloaded!
    The site 50 has been downloaded!
    The site 51 has been downloaded!
    The site 52 has been downloaded!
    The site 53 has been downloaded!
    The site 54 has been downloaded!
    The site 55 has been downloaded!
    The site 56 has been downloaded!
    The site 57 has been downloaded!
    The site 58 has been downloaded!
    The site 59 has been downloaded!
    The site 60 has been downloaded!
    The site 61 has been downloaded!
    The site 62 has NOT been downloaded from exception!
    The site 63 has been downloaded!
    The site 64 has been downloaded!
    The site 65 has been downloaded!
    The site 66 has been downloaded!
    The site 67 has been downloaded!
    The site 68 has been downloaded!
    The site 69 has been downloaded!
    The site 70 has NOT been downloaded!
    The site 71 has been downloaded!
    The site 72 has been downloaded!
    The site 73 has been downloaded!
    The site 74 has been downloaded!
    The site 75 has been downloaded!
    The site 76 has been downloaded!
    The site 77 has been downloaded!
    The site 78 has been downloaded!
    The site 79 has been downloaded!
    The site 80 has been downloaded!
    The site 81 has been downloaded!
    The site 82 has been downloaded!
    The site 83 has been downloaded!
    The site 84 has been downloaded!
    The site 85 has been downloaded!
    The site 86 has been downloaded!
    The site 87 has been downloaded!
    The site 88 has been downloaded!
    The site 89 has been downloaded!
    The site 90 has NOT been downloaded from exception!
    The site 91 has been downloaded!
    The site 92 has been downloaded!
    The site 93 has been downloaded!
    The site 94 has been downloaded!
    The site 95 has been downloaded!
    The site 96 has been downloaded!
    The site 97 has NOT been downloaded from exception!
    The site 98 has been downloaded!
    The site 99 has been downloaded!
    The site 100 has been downloaded!
    The site 101 has been downloaded!
    The site 102 has been downloaded!
    The site 103 has been downloaded!
    The site 104 has been downloaded!
    The site 105 has been downloaded!
    The site 106 has been downloaded!
    The site 107 has been downloaded!
    The site 108 has been downloaded!
    The site 109 has been downloaded!
    The site 110 has been downloaded!
    The site 111 has been downloaded!
    The site 112 has been downloaded!
    The site 113 has been downloaded!
    The site 114 has been downloaded!
    The site 115 has been downloaded!
    The site 116 has been downloaded!
    The site 117 has been downloaded!
    The site 118 has NOT been downloaded!
    The site 119 has been downloaded!
    The site 120 has been downloaded!
    The site 121 has been downloaded!
    The site 122 has been downloaded!
    The site 123 has been downloaded!
    The site 124 has been downloaded!
    The site 125 has been downloaded!
    The site 126 has been downloaded!
    The site 127 has been downloaded!
    The site 128 has been downloaded!
    The site 129 has been downloaded!
    The site 130 has been downloaded!
    The site 131 has been downloaded!
    The site 132 has been downloaded!
    The site 133 has been downloaded!
    The site 134 has been downloaded!
    The site 135 has NOT been downloaded from exception!
    The site 136 has been downloaded!
    The site 137 has been downloaded!
    The site 138 has been downloaded!
    The site 139 has been downloaded!
    The site 140 has been downloaded!
    The site 141 has NOT been downloaded from exception!
    The site 142 has been downloaded!
    The site 143 has been downloaded!
    The site 144 has been downloaded!
    The site 145 has been downloaded!
    The site 146 has been downloaded!
    The site 147 has been downloaded!
    The site 148 has been downloaded!
    The site 149 has been downloaded!
    The site 150 has been downloaded!
    The site 151 has been downloaded!
    The site 152 has been downloaded!
    The site 153 has been downloaded!
    The site 154 has been downloaded!
    The site 155 has been downloaded!
    The site 156 has been downloaded!
    The site 157 has been downloaded!
    The site 158 has been downloaded!
    The site 159 has been downloaded!
    The site 160 has been downloaded!
    The site 161 has NOT been downloaded from exception!
    The site 162 has been downloaded!
    The site 163 has been downloaded!
    The site 164 has NOT been downloaded from exception!
    The site 165 has been downloaded!
    The site 166 has been downloaded!
    The site 167 has been downloaded!
    The site 168 has been downloaded!
    The site 169 has been downloaded!
    The site 170 has been downloaded!
    The site 171 has been downloaded!
    The site 172 has been downloaded!
    The site 173 has been downloaded!
    The site 174 has been downloaded!
    The site 175 has been downloaded!
    The site 176 has been downloaded!
    The site 177 has been downloaded!
    The site 178 has been downloaded!
    The site 179 has been downloaded!
    The site 180 has been downloaded!
    The site 181 has been downloaded!
    The site 182 has been downloaded!
    The site 183 has been downloaded!
    The site 184 has been downloaded!
    The site 185 has been downloaded!
    The site 186 has been downloaded!
    The site 187 has been downloaded!
    The site 188 has been downloaded!
    The site 189 has been downloaded!
    The site 190 has been downloaded!
    The site 191 has been downloaded!
    The site 192 has been downloaded!
    The site 193 has been downloaded!
    The site 194 has been downloaded!
    The site 195 has NOT been downloaded from exception!
    The site 196 has been downloaded!
    The site 197 has been downloaded!
    The site 198 has been downloaded!
    The site 199 has been downloaded!
    The site 200 has been downloaded!
    The site 201 has been downloaded!
    The site 202 has been downloaded!
    The site 203 has been downloaded!
    The site 204 has been downloaded!
    The site 205 has been downloaded!
    The site 206 has been downloaded!
    The site 207 has been downloaded!
    The site 208 has been downloaded!
    The site 209 has been downloaded!
    The site 210 has been downloaded!
    The site 211 has been downloaded!
    The site 212 has been downloaded!
    The site 213 has been downloaded!
    The site 214 has been downloaded!
    The site 215 has been downloaded!
    The site 216 has NOT been downloaded from exception!
    The site 217 has been downloaded!
    The site 218 has been downloaded!
    The site 219 has been downloaded!
    The site 220 has been downloaded!
    The site 221 has been downloaded!
    The site 222 has been downloaded!
    The site 223 has been downloaded!
    The site 224 has been downloaded!
    The site 225 has been downloaded!
    The site 226 has been downloaded!
    The site 227 has been downloaded!
    The site 228 has NOT been downloaded from exception!
    The site 229 has been downloaded!
    The site 230 has been downloaded!
    The site 231 has been downloaded!
    The site 232 has been downloaded!
    The site 233 has been downloaded!
    The site 234 has been downloaded!
    The site 235 has been downloaded!
    The site 236 has been downloaded!
    The site 237 has been downloaded!
    The site 238 has been downloaded!
    The site 239 has NOT been downloaded from exception!
    The site 240 has been downloaded!
    The site 241 has been downloaded!
    The site 242 has NOT been downloaded from exception!
    The site 243 has been downloaded!
    The site 244 has been downloaded!
    The site 245 has been downloaded!
    The site 246 has been downloaded!
    The site 247 has been downloaded!
    The site 248 has been downloaded!
    The site 249 has been downloaded!
    The site 250 has been downloaded!
    The site 251 has been downloaded!
    The site 252 has been downloaded!
    The site 253 has been downloaded!
    The site 254 has been downloaded!
    The site 255 has been downloaded!
    The site 256 has been downloaded!
    The site 257 has been downloaded!
    The site 258 has been downloaded!
    The site 259 has been downloaded!
    The site 260 has been downloaded!
    The site 261 has been downloaded!
    The site 262 has been downloaded!
    The site 263 has been downloaded!
    The site 264 has been downloaded!
    The site 265 has been downloaded!
    The site 266 has been downloaded!
    The site 267 has been downloaded!
    The site 268 has been downloaded!
    The site 269 has been downloaded!
    The site 270 has been downloaded!
    The site 271 has been downloaded!
    The site 272 has been downloaded!
    The site 273 has been downloaded!
    The site 274 has been downloaded!
    The site 275 has NOT been downloaded from exception!
    The site 276 has been downloaded!
    The site 277 has been downloaded!
    The site 278 has been downloaded!
    The site 279 has been downloaded!
    The site 280 has been downloaded!
    The site 281 has been downloaded!
    The site 282 has been downloaded!
    The site 283 has been downloaded!
    The site 284 has been downloaded!
    The site 285 has been downloaded!
    The site 286 has been downloaded!
    The site 287 has been downloaded!
    The site 288 has been downloaded!
    The site 289 has been downloaded!
    The site 290 has been downloaded!
    The site 291 has been downloaded!
    The site 292 has been downloaded!
    The site 293 has been downloaded!
    The site 294 has been downloaded!
    The site 295 has been downloaded!
    The site 296 has been downloaded!
    The site 297 has been downloaded!
    The site 298 has been downloaded!
    The site 299 has been downloaded!
    The site 300 has been downloaded!
    The site 301 has been downloaded!
    The site 302 has been downloaded!
    The site 303 has been downloaded!
    The site 304 has been downloaded!
    The site 305 has been downloaded!
    The site 306 has NOT been downloaded from exception!
    The site 307 has been downloaded!
    The site 308 has been downloaded!
    The site 309 has been downloaded!
    The site 310 has been downloaded!
    The site 311 has been downloaded!
    The site 312 has been downloaded!
    The site 313 has been downloaded!
    The site 314 has been downloaded!
    The site 315 has been downloaded!
    The site 316 has been downloaded!
    The site 317 has been downloaded!
    The site 318 has been downloaded!
    The site 319 has been downloaded!
    The site 320 has been downloaded!
    The site 321 has been downloaded!
    The site 322 has been downloaded!
    The site 323 has been downloaded!
    The site 324 has been downloaded!
    The site 325 has been downloaded!
    The site 326 has NOT been downloaded from exception!
    The site 327 has been downloaded!
    The site 328 has been downloaded!
    The site 329 has been downloaded!
    The site 330 has been downloaded!
    The site 331 has been downloaded!
    The site 332 has been downloaded!
    The site 333 has been downloaded!
    The site 334 has been downloaded!
    The site 335 has been downloaded!
    The site 336 has been downloaded!
    The site 337 has been downloaded!
    The site 338 has been downloaded!
    The site 339 has been downloaded!
    The site 340 has been downloaded!
    The site 341 has been downloaded!
    The site 342 has been downloaded!
    The site 343 has been downloaded!
    The site 344 has been downloaded!
    The site 345 has been downloaded!
    The site 346 has been downloaded!
    The site 347 has been downloaded!
    The site 348 has been downloaded!
    The site 349 has been downloaded!
    The site 350 has been downloaded!
    The site 351 has been downloaded!
    The site 352 has been downloaded!
    The site 353 has been downloaded!
    The site 354 has been downloaded!
    The site 355 has been downloaded!
    The site 356 has been downloaded!
    The site 357 has been downloaded!
    The site 358 has been downloaded!
    The site 359 has been downloaded!
    The site 360 has been downloaded!
    The site 361 has been downloaded!
    The site 362 has been downloaded!
    The site 363 has NOT been downloaded from exception!
    The site 364 has been downloaded!
    The site 365 has been downloaded!
    The site 366 has been downloaded!
    The site 367 has been downloaded!
    The site 368 has been downloaded!
    The site 369 has been downloaded!
    The site 370 has been downloaded!
    The site 371 has been downloaded!
    The site 372 has been downloaded!
    The site 373 has been downloaded!
    The site 374 has been downloaded!
    The site 375 has been downloaded!
    The site 376 has been downloaded!
    The site 377 has been downloaded!
    The site 378 has been downloaded!
    The site 379 has been downloaded!
    The site 380 has been downloaded!
    The site 381 has been downloaded!
    The site 382 has been downloaded!
    The site 383 has been downloaded!
    The site 384 has been downloaded!
    The site 385 has been downloaded!
    The site 386 has been downloaded!
    The site 387 has been downloaded!
    The site 388 has been downloaded!
    The site 389 has been downloaded!
    The site 390 has been downloaded!
    The site 391 has been downloaded!
    The site 392 has been downloaded!
    The site 393 has been downloaded!
    The site 394 has been downloaded!
    The site 395 has been downloaded!
    The site 396 has been downloaded!
    The site 397 has NOT been downloaded from exception!
    The site 398 has been downloaded!
    The site 399 has been downloaded!
    The site 400 has been downloaded!
    The site 401 has been downloaded!
    The site 402 has been downloaded!
    The site 403 has been downloaded!
    The site 404 has been downloaded!
    The site 405 has been downloaded!
    The site 406 has been downloaded!
    The site 407 has been downloaded!
    The site 408 has been downloaded!
    The site 409 has been downloaded!
    The site 410 has been downloaded!
    The site 411 has been downloaded!
    The site 412 has been downloaded!
    The site 413 has been downloaded!
    The site 414 has NOT been downloaded from exception!
    The site 415 has been downloaded!
    The site 416 has been downloaded!
    The site 417 has been downloaded!
    The site 418 has been downloaded!
    The site 419 has been downloaded!
    The site 420 has been downloaded!
    The site 421 has been downloaded!
    The site 422 has been downloaded!
    The site 423 has been downloaded!
    The site 424 has been downloaded!
    The site 425 has been downloaded!
    The site 426 has been downloaded!
    The site 427 has been downloaded!
    The site 428 has been downloaded!
    The site 429 has been downloaded!
    The site 430 has been downloaded!
    The site 431 has been downloaded!
    The site 432 has been downloaded!
    The site 433 has been downloaded!
    The site 434 has been downloaded!
    The site 435 has been downloaded!
    The site 436 has been downloaded!
    The site 437 has been downloaded!
    The site 438 has been downloaded!
    The site 439 has been downloaded!
    The site 440 has been downloaded!
    The site 441 has NOT been downloaded from exception!
    The site 442 has been downloaded!
    The site 443 has been downloaded!
    The site 444 has been downloaded!
    The site 445 has been downloaded!
    The site 446 has been downloaded!
    The site 447 has been downloaded!
    The site 448 has been downloaded!
    The site 449 has been downloaded!
    The site 450 has been downloaded!
    The site 451 has been downloaded!
    The site 452 has been downloaded!
    The site 453 has been downloaded!
    The site 454 has been downloaded!
    The site 455 has been downloaded!
    The site 456 has been downloaded!
    The site 457 has been downloaded!
    The site 458 has been downloaded!
    The site 459 has been downloaded!
    The site 460 has been downloaded!
    The site 461 has been downloaded!
    The site 462 has been downloaded!
    The site 463 has been downloaded!
    The site 464 has NOT been downloaded!
    The site 465 has been downloaded!
    The site 466 has been downloaded!
    The site 467 has been downloaded!
    The site 468 has been downloaded!
    The site 469 has been downloaded!
    The site 470 has been downloaded!
    The site 471 has been downloaded!
    The site 472 has been downloaded!
    The site 473 has been downloaded!
    The site 474 has been downloaded!
    The site 475 has been downloaded!
    The site 476 has been downloaded!
    The site 477 has been downloaded!
    The site 478 has been downloaded!
    The site 479 has been downloaded!
    The site 480 has been downloaded!
    The site 481 has been downloaded!
    The site 482 has been downloaded!
    The site 483 has been downloaded!
    The site 484 has been downloaded!
    The site 485 has been downloaded!
    The site 486 has been downloaded!
    The site 487 has been downloaded!
    The site 488 has been downloaded!
    The site 489 has been downloaded!
    The site 490 has been downloaded!
    The site 491 has been downloaded!
    The site 492 has been downloaded!
    The site 493 has been downloaded!
    The site 494 has been downloaded!
    The site 495 has been downloaded!
    The site 496 has been downloaded!
    The site 497 has been downloaded!
    The site 498 has been downloaded!
    The site 499 has been downloaded!
    


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
      <td>Fannie Mae</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HCA Holdings</td>
      <td>62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Best Buy</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nike</td>
      <td>90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tesoro</td>
      <td>97</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Arrow Electronics</td>
      <td>118</td>
    </tr>
    <tr>
      <th>6</th>
      <td>AutoNation</td>
      <td>135</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Southwest Airlines</td>
      <td>141</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Southern</td>
      <td>161</td>
    </tr>
    <tr>
      <th>9</th>
      <td>American Electric Power</td>
      <td>164</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Office Depot</td>
      <td>195</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PBF Energy</td>
      <td>216</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Consolidated Edison</td>
      <td>228</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Toys “R” Us</td>
      <td>239</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Dominion Resources</td>
      <td>242</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Global Partners</td>
      <td>275</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PayPal Holdings</td>
      <td>306</td>
    </tr>
    <tr>
      <th>17</th>
      <td>News Corp.</td>
      <td>326</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Williams</td>
      <td>363</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Auto-Owners Insurance</td>
      <td>397</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Tractor Supply</td>
      <td>414</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Old Republic International</td>
      <td>441</td>
    </tr>
    <tr>
      <th>22</th>
      <td>St. Jude Medical</td>
      <td>464</td>
    </tr>
  </tbody>
</table>
</div>




```python
empty=[]
keyf = []
flesch = []
sentence =[] 
word = []
unique_w = []
```
# I used it to see how much time it does to run the function

```python
import time 
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
                        print("Site", str(num), "is validated")
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
```

    ('Site', '0', 'is not validated from check 2')
    ('Site', '1', 'is not validated from check 2')
    ('Site', '2', 'is validated')
    ('Site', '3', 'is validated')
    ('Site', '4', 'is validated')
    ('Site', '5', 'is validated')
    ('Site', '6', 'is validated')
    ('Site', '7', 'is validated')
    ('Site', '8', 'is validated')
    ('Site', '9', 'is validated')
    ('Site', '10', 'is validated')
    ('Site', '11', 'is not validated from check 2')
    ('Site', '12', 'is validated')
    ('Site', '13', 'is validated')
    ('Site', '14', 'is validated')
    ('Site', '15', 'is not validated from sites')
    ('Site', '16', 'is validated')
    ('Site', '17', 'is validated')
    ('Site', '18', 'is validated')
    ('Site', '19', 'is validated')
    ('Site', '20', 'is validated')
    ('Site', '21', 'is validated')
    ('Site', '22', 'is validated')
    ('Site', '23', 'is validated')
    ('Site', '24', 'is validated')
    ('Site', '25', 'is validated')
    ('Site', '26', 'is validated')
    ('Site', '27', 'is validated')
    ('Site', '28', 'is validated')
    ('Site', '29', 'is validated')
    ('Site', '30', 'is validated')
    ('Site', '31', 'is validated')
    ('Site', '32', 'is validated')
    ('Site', '33', 'is not validated from check 2')
    ('Site', '34', 'is validated')
    ('Site', '35', 'is validated')
    ('Site', '36', 'is validated')
    ('Site', '37', 'is not validated from check 2')
    ('Site', '38', 'is validated')
    ('Site', '39', 'is validated')
    ('Site', '40', 'is validated')
    ('Site', '41', 'is validated')
    ('Site', '42', 'is validated')
    ('Site', '43', 'is validated')
    ('Site', '44', 'is validated')
    ('Site', '45', 'is validated')
    ('Site', '46', 'is validated')
    ('Site', '47', 'is validated')
    ('Site', '48', 'is validated')
    ('Site', '49', 'is validated')
    ('Site', '50', 'is validated')
    ('Site', '51', 'is validated')
    ('Site', '52', 'is validated')
    ('Site', '53', 'is validated')
    ('Site', '54', 'is validated')
    ('Site', '55', 'is validated')
    ('Site', '56', 'is validated')
    ('Site', '57', 'is validated')
    ('Site', '58', 'is not validated from check 2')
    ('Site', '59', 'is validated')
    ('Site', '60', 'is validated')
    ('Site', '61', 'is validated')
    ('Site', '62', 'is not validated from sites')
    ('Site', '63', 'is validated')
    ('Site', '64', 'is validated')
    ('Site', '65', 'is validated')
    ('Site', '66', 'is validated')
    ('Site', '67', 'is not validated from check 2')
    ('Site', '68', 'is validated')
    ('Site', '69', 'is validated')
    ('Site', '70', 'is not validated from sites')
    ('Site', '71', 'is validated')
    ('Site', '72', 'is validated')
    ('Site', '73', 'is validated')
    ('Site', '74', 'is validated')
    ('Site', '75', 'is validated')
    ('Site', '76', 'is validated')
    ('Site', '77', 'is validated')
    ('Site', '78', 'is validated')
    ('Site', '79', 'is validated')
    ('Site', '80', 'is validated')
    ('Site', '81', 'is validated')
    ('Site', '82', 'is not validated from check 2')
    ('Site', '83', 'is validated')
    ('Site', '84', 'is validated')
    ('Site', '85', 'is validated')
    ('Site', '86', 'is validated')
    ('Site', '87', 'is validated')
    ('Site', '88', 'is validated')
    ('Site', '89', 'is validated')
    ('Site', '90', 'is not validated from sites')
    ('Site', '91', 'is validated')
    ('Site', '92', 'is validated')
    ('Site', '93', 'is validated')
    ('Site', '94', 'is validated')
    ('Site', '95', 'is validated')
    ('Site', '96', 'is validated')
    ('Site', '97', 'is not validated from sites')
    ('Site', '98', 'is validated')
    ('Site', '99', 'is validated')
    ('Site', '100', 'is validated')
    ('Site', '101', 'is validated')
    ('Site', '102', 'is validated')
    ('Site', '103', 'is validated')
    ('Site', '104', 'is validated')
    ('Site', '105', 'is validated')
    ('Site', '106', 'is not validated from check')
    ('Site', '107', 'is not validated from sites')
    ('Site', '108', 'is validated')
    ('Site', '109', 'is validated')
    ('Site', '110', 'is validated')
    ('Site', '111', 'is validated')
    ('Site', '112', 'is validated')
    ('Site', '113', 'is validated')
    ('Site', '114', 'is validated')
    ('Site', '115', 'is validated')
    ('Site', '116', 'is validated')
    ('Site', '117', 'is validated')
    ('Site', '118', 'is not validated from sites')
    ('Site', '119', 'is validated')
    ('Site', '120', 'is validated')
    ('Site', '121', 'is validated')
    ('Site', '122', 'is validated')
    ('Site', '123', 'is validated')
    ('Site', '124', 'is validated')
    ('Site', '125', 'is not validated from check 2')
    ('Site', '126', 'is validated')
    ('Site', '127', 'is validated')
    ('Site', '128', 'is validated')
    ('Site', '129', 'is validated')
    ('Site', '130', 'is validated')
    ('Site', '131', 'is validated')
    ('Site', '132', 'is validated')
    ('Site', '133', 'is validated')
    ('Site', '134', 'is validated')
    ('Site', '135', 'is not validated from sites')
    ('Site', '136', 'is validated')
    ('Site', '137', 'is validated')
    ('Site', '138', 'is validated')
    ('Site', '139', 'is validated')
    ('Site', '140', 'is validated')
    ('Site', '141', 'is not validated from sites')
    ('Site', '142', 'is validated')
    ('Site', '143', 'is validated')
    ('Site', '144', 'is validated')
    ('Site', '145', 'is validated')
    ('Site', '146', 'is validated')
    ('Site', '147', 'is not validated from check 2')
    ('Site', '148', 'is validated')
    ('Site', '149', 'is validated')
    ('Site', '150', 'is validated')
    ('Site', '151', 'is validated')
    ('Site', '152', 'is validated')
    ('Site', '153', 'is validated')
    ('Site', '154', 'is validated')
    ('Site', '155', 'is not validated from check 2')
    ('Site', '156', 'is validated')
    ('Site', '157', 'is validated')
    ('Site', '158', 'is validated')
    ('Site', '159', 'is validated')
    ('Site', '160', 'is validated')
    ('Site', '161', 'is not validated from sites')
    ('Site', '162', 'is validated')
    ('Site', '163', 'is validated')
    ('Site', '164', 'is not validated from sites')
    ('Site', '165', 'is validated')
    ('Site', '166', 'is not validated from check 2')
    ('Site', '167', 'is validated')
    ('Site', '168', 'is validated')
    ('Site', '169', 'is validated')
    ('Site', '170', 'is validated')
    ('Site', '171', 'is not validated from check 2')
    ('Site', '172', 'is validated')
    ('Site', '173', 'is validated')
    ('Site', '174', 'is validated')
    ('Site', '175', 'is validated')
    ('Site', '176', 'is validated')
    ('Site', '177', 'is validated')
    ('Site', '178', 'is validated')
    ('Site', '179', 'is not validated from check 2')
    ('Site', '180', 'is validated')
    ('Site', '181', 'is validated')
    ('Site', '182', 'is validated')
    ('Site', '183', 'is validated')
    ('Site', '184', 'is validated')
    ('Site', '185', 'is validated')
    ('Site', '186', 'is validated')
    ('Site', '187', 'is validated')
    ('Site', '188', 'is validated')
    ('Site', '189', 'is validated')
    ('Site', '190', 'is validated')
    ('Site', '191', 'is validated')
    ('Site', '192', 'is validated')
    ('Site', '193', 'is validated')
    ('Site', '194', 'is validated')
    ('Site', '195', 'is not validated from sites')
    ('Site', '196', 'is validated')
    ('Site', '197', 'is validated')
    ('Site', '198', 'is validated')
    ('Site', '199', 'is validated')
    ('Site', '200', 'is validated')
    ('Site', '201', 'is validated')
    ('Site', '202', 'is validated')
    ('Site', '203', 'is validated')
    ('Site', '204', 'is validated')
    ('Site', '205', 'is validated')
    ('Site', '206', 'is validated')
    ('Site', '207', 'is validated')
    ('Site', '208', 'is validated')
    ('Site', '209', 'is not validated from check 2')
    ('Site', '210', 'is validated')
    ('Site', '211', 'is not validated from check 2')
    ('Site', '212', 'is validated')
    ('Site', '213', 'is validated')
    ('Site', '214', 'is validated')
    ('Site', '215', 'is validated')
    ('Site', '216', 'is not validated from sites')
    ('Site', '217', 'is validated')
    ('Site', '218', 'is validated')
    ('Site', '219', 'is validated')
    ('Site', '220', 'is validated')
    ('Site', '221', 'is validated')
    ('Site', '222', 'is validated')
    ('Site', '223', 'is validated')
    ('Site', '224', 'is validated')
    ('Site', '225', 'is not validated from check 2')
    ('Site', '226', 'is validated')
    ('Site', '227', 'is validated')
    ('Site', '228', 'is not validated from sites')
    ('Site', '229', 'is validated')
    ('Site', '230', 'is validated')
    ('Site', '231', 'is validated')
    ('Site', '232', 'is validated')
    ('Site', '233', 'is validated')
    ('Site', '234', 'is validated')
    ('Site', '235', 'is validated')
    ('Site', '236', 'is validated')
    ('Site', '237', 'is validated')
    ('Site', '238', 'is validated')
    ('Site', '239', 'is not validated from sites')
    ('Site', '240', 'is validated')
    ('Site', '241', 'is validated')
    ('Site', '242', 'is not validated from sites')
    ('Site', '243', 'is validated')
    ('Site', '244', 'is validated')
    ('Site', '245', 'is validated')
    ('Site', '246', 'is validated')
    ('Site', '247', 'is validated')
    ('Site', '248', 'is validated')
    ('Site', '249', 'is validated')
    ('Site', '250', 'is validated')
    ('Site', '251', 'is validated')
    ('Site', '252', 'is validated')
    ('Site', '253', 'is validated')
    ('Site', '254', 'is validated')
    ('Site', '255', 'is validated')
    ('Site', '256', 'is validated')
    ('Site', '257', 'is validated')
    ('Site', '258', 'is validated')
    ('Site', '259', 'is validated')
    ('Site', '260', 'is validated')
    ('Site', '261', 'is validated')
    ('Site', '262', 'is validated')
    ('Site', '263', 'is validated')
    ('Site', '264', 'is validated')
    ('Site', '265', 'is validated')
    ('Site', '266', 'is validated')
    ('Site', '267', 'is validated')
    ('Site', '268', 'is validated')
    ('Site', '269', 'is validated')
    ('Site', '270', 'is validated')
    ('Site', '271', 'is validated')
    ('Site', '272', 'is not validated from check 2')
    ('Site', '273', 'is validated')
    ('Site', '274', 'is validated')
    ('Site', '275', 'is not validated from sites')
    ('Site', '276', 'is validated')
    ('Site', '277', 'is validated')
    ('Site', '278', 'is validated')
    ('Site', '279', 'is validated')
    ('Site', '280', 'is validated')
    ('Site', '281', 'is validated')
    ('Site', '282', 'is not validated from check 2')
    ('Site', '283', 'is validated')
    ('Site', '284', 'is validated')
    ('Site', '285', 'is validated')
    ('Site', '286', 'is validated')
    ('Site', '287', 'is validated')
    ('Site', '288', 'is validated')
    ('Site', '289', 'is validated')
    ('Site', '290', 'is validated')
    ('Site', '291', 'is validated')
    ('Site', '292', 'is validated')
    ('Site', '293', 'is validated')
    ('Site', '294', 'is validated')
    ('Site', '295', 'is validated')
    ('Site', '296', 'is validated')
    ('Site', '297', 'is not validated from check 2')
    ('Site', '298', 'is validated')
    ('Site', '299', 'is validated')
    ('Site', '300', 'is validated')
    ('Site', '301', 'is validated')
    ('Site', '302', 'is validated')
    ('Site', '303', 'is validated')
    ('Site', '304', 'is validated')
    ('Site', '305', 'is validated')
    ('Site', '306', 'is not validated from sites')
    ('Site', '307', 'is validated')
    ('Site', '308', 'is validated')
    ('Site', '309', 'is validated')
    ('Site', '310', 'is validated')
    ('Site', '311', 'is validated')
    ('Site', '312', 'is validated')
    ('Site', '313', 'is validated')
    ('Site', '314', 'is validated')
    ('Site', '315', 'is validated')
    ('Site', '316', 'is validated')
    ('Site', '317', 'is validated')
    ('Site', '318', 'is validated')
    ('Site', '319', 'is validated')
    ('Site', '320', 'is validated')
    ('Site', '321', 'is validated')
    ('Site', '322', 'is validated')
    ('Site', '323', 'is validated')
    ('Site', '324', 'is validated')
    ('Site', '325', 'is validated')
    ('Site', '326', 'is not validated from sites')
    ('Site', '327', 'is validated')
    ('Site', '328', 'is validated')
    ('Site', '329', 'is validated')
    ('Site', '330', 'is validated')
    ('Site', '331', 'is validated')
    ('Site', '332', 'is validated')
    ('Site', '333', 'is validated')
    ('Site', '334', 'is validated')
    ('Site', '335', 'is validated')
    ('Site', '336', 'is validated')
    ('Site', '337', 'is validated')
    ('Site', '338', 'is validated')
    ('Site', '339', 'is validated')
    ('Site', '340', 'is validated')
    ('Site', '341', 'is validated')
    ('Site', '342', 'is validated')
    ('Site', '343', 'is validated')
    ('Site', '344', 'is validated')
    ('Site', '345', 'is validated')
    ('Site', '346', 'is validated')
    ('Site', '347', 'is validated')
    ('Site', '348', 'is not validated from check 2')
    ('Site', '349', 'is validated')
    ('Site', '350', 'is validated')
    ('Site', '351', 'is validated')
    ('Site', '352', 'is validated')
    ('Site', '353', 'is validated')
    ('Site', '354', 'is validated')
    ('Site', '355', 'is validated')
    ('Site', '356', 'is validated')
    ('Site', '357', 'is validated')
    ('Site', '358', 'is validated')
    ('Site', '359', 'is validated')
    ('Site', '360', 'is validated')
    ('Site', '361', 'is validated')
    ('Site', '362', 'is validated')
    ('Site', '363', 'is not validated from sites')
    ('Site', '364', 'is validated')
    ('Site', '365', 'is validated')
    ('Site', '366', 'is not validated from check 2')
    ('Site', '367', 'is validated')
    ('Site', '368', 'is validated')
    ('Site', '369', 'is not validated from check 2')
    ('Site', '370', 'is validated')
    ('Site', '371', 'is validated')
    ('Site', '372', 'is validated')
    ('Site', '373', 'is validated')
    ('Site', '374', 'is validated')
    ('Site', '375', 'is not validated from check 2')
    ('Site', '376', 'is validated')
    ('Site', '377', 'is validated')
    ('Site', '378', 'is validated')
    ('Site', '379', 'is validated')
    ('Site', '380', 'is validated')
    ('Site', '381', 'is validated')
    ('Site', '382', 'is validated')
    ('Site', '383', 'is not validated from check 2')
    ('Site', '384', 'is not validated from check 2')
    ('Site', '385', 'is validated')
    ('Site', '386', 'is validated')
    ('Site', '387', 'is validated')
    ('Site', '388', 'is validated')
    ('Site', '389', 'is not validated from check 2')
    ('Site', '390', 'is validated')
    ('Site', '391', 'is validated')
    ('Site', '392', 'is validated')
    ('Site', '393', 'is validated')
    ('Site', '394', 'is validated')
    ('Site', '395', 'is validated')
    ('Site', '396', 'is validated')
    ('Site', '397', 'is not validated from sites')
    ('Site', '398', 'is validated')
    ('Site', '399', 'is validated')
    ('Site', '400', 'is validated')
    ('Site', '401', 'is validated')
    ('Site', '402', 'is not validated from check 2')
    ('Site', '403', 'is validated')
    ('Site', '404', 'is not validated from check 2')
    ('Site', '405', 'is validated')
    ('Site', '406', 'is validated')
    ('Site', '407', 'is not validated from check 2')
    ('Site', '408', 'is validated')
    ('Site', '409', 'is validated')
    ('Site', '410', 'is validated')
    ('Site', '411', 'is validated')
    ('Site', '412', 'is validated')
    ('Site', '413', 'is validated')
    ('Site', '414', 'is not validated from sites')
    ('Site', '415', 'is validated')
    ('Site', '416', 'is validated')
    ('Site', '417', 'is validated')
    ('Site', '418', 'is validated')
    ('Site', '419', 'is validated')
    ('Site', '420', 'is validated')
    ('Site', '421', 'is validated')
    ('Site', '422', 'is validated')
    ('Site', '423', 'is validated')
    ('Site', '424', 'is validated')
    ('Site', '425', 'is validated')
    ('Site', '426', 'is validated')
    ('Site', '427', 'is validated')
    ('Site', '428', 'is validated')
    ('Site', '429', 'is validated')
    ('Site', '430', 'is validated')
    ('Site', '431', 'is validated')
    ('Site', '432', 'is not validated from check 2')
    ('Site', '433', 'is validated')
    ('Site', '434', 'is validated')
    ('Site', '435', 'is validated')
    ('Site', '436', 'is validated')
    ('Site', '437', 'is validated')
    ('Site', '438', 'is not validated from check 2')
    ('Site', '439', 'is validated')
    ('Site', '440', 'is validated')
    ('Site', '441', 'is not validated from sites')
    ('Site', '442', 'is validated')
    ('Site', '443', 'is not validated from check 2')
    ('Site', '444', 'is validated')
    ('Site', '445', 'is validated')
    ('Site', '446', 'is validated')
    ('Site', '447', 'is not validated from check 2')
    ('Site', '448', 'is validated')
    ('Site', '449', 'is validated')
    ('Site', '450', 'is validated')
    ('Site', '451', 'is validated')
    ('Site', '452', 'is validated')
    ('Site', '453', 'is validated')
    ('Site', '454', 'is validated')
    ('Site', '455', 'is validated')
    ('Site', '456', 'is validated')
    ('Site', '457', 'is validated')
    ('Site', '458', 'is validated')
    ('Site', '459', 'is validated')
    ('Site', '460', 'is validated')
    ('Site', '461', 'is validated')
    ('Site', '462', 'is validated')
    ('Site', '463', 'is validated')
    ('Site', '464', 'is not validated from sites')
    ('Site', '465', 'is validated')
    ('Site', '466', 'is not validated from check 2')
    ('Site', '467', 'is validated')
    ('Site', '468', 'is not validated from check 2')
    ('Site', '469', 'is validated')
    ('Site', '470', 'is validated')
    ('Site', '471', 'is validated')
    ('Site', '472', 'is validated')
    ('Site', '473', 'is validated')
    ('Site', '474', 'is validated')
    ('Site', '475', 'is validated')
    ('Site', '476', 'is validated')
    ('Site', '477', 'is validated')
    ('Site', '478', 'is validated')
    ('Site', '479', 'is validated')
    ('Site', '480', 'is validated')
    ('Site', '481', 'is validated')
    ('Site', '482', 'is validated')
    ('Site', '483', 'is validated')
    ('Site', '484', 'is validated')
    ('Site', '485', 'is validated')
    ('Site', '486', 'is validated')
    ('Site', '487', 'is validated')
    ('Site', '488', 'is validated')
    ('Site', '489', 'is validated')
    ('Site', '490', 'is validated')
    ('Site', '491', 'is validated')
    ('Site', '492', 'is validated')
    ('Site', '493', 'is validated')
    ('Site', '494', 'is validated')
    ('Site', '495', 'is validated')
    ('Site', '496', 'is validated')
    ('Site', '497', 'is validated')
    ('Site', '498', 'is validated')
    ('Site', '499', 'is validated')
    


```python
readability = []
```


```python
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
```


```python
readable (flesch)
```

    The function is completed!
    


```python
d1 = {'company' : pd.Series(list500_names, index=[list500_num]),
      'url' : pd.Series(list500_url, index=[list500_num]),
      'Readability' : pd.Series(readability, index=[list500_num]),
      'Flesh_Mesaure' : pd.Series(flesch,index=[list500_num]),
'Sentences' : pd.Series(sentence, index=[list500_num]),
'Words' : pd.Series(word, index=[list500_num]),
'Unique words' : pd.Series(unique_w, index=[list500_num])}
fre = pd.DataFrame(d1)    
fre #we see the first 3 in the data frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Flesh_Mesaure</th>
      <th>Readability</th>
      <th>Sentences</th>
      <th>Unique words</th>
      <th>Words</th>
      <th>company</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>Walmart</td>
      <td>www.walmart.com</td>
    </tr>
    <tr>
      <th>2</th>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>Exxon Mobil</td>
      <td>www.exxonmobil.com</td>
    </tr>
    <tr>
      <th>3</th>
      <td>59.7</td>
      <td>Fairly difficult</td>
      <td>119</td>
      <td>25</td>
      <td>279</td>
      <td>Apple</td>
      <td>www.apple.com</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.6</td>
      <td>Fairly difficult</td>
      <td>27</td>
      <td>39</td>
      <td>197</td>
      <td>Berkshire Hathaway</td>
      <td>www.berkshirehathaway.com</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25</td>
      <td>Very Confusing</td>
      <td>229</td>
      <td>295</td>
      <td>799</td>
      <td>McKesson</td>
      <td>www.mckesson.com</td>
    </tr>
    <tr>
      <th>6</th>
      <td>53.4</td>
      <td>Fairly difficult</td>
      <td>37</td>
      <td>59</td>
      <td>326</td>
      <td>UnitedHealth Group</td>
      <td>www.unitedhealthgroup.com</td>
    </tr>
    <tr>
      <th>7</th>
      <td>35</td>
      <td>Difficult</td>
      <td>183</td>
      <td>249</td>
      <td>818</td>
      <td>CVS Health</td>
      <td>www.cvshealth.com</td>
    </tr>
    <tr>
      <th>8</th>
      <td>32.8</td>
      <td>Difficult</td>
      <td>231</td>
      <td>74</td>
      <td>600</td>
      <td>General Motors</td>
      <td>www.gm.com</td>
    </tr>
    <tr>
      <th>9</th>
      <td>82.1</td>
      <td>Easy</td>
      <td>258</td>
      <td>80</td>
      <td>760</td>
      <td>Ford Motor</td>
      <td>www.ford.com</td>
    </tr>
    <tr>
      <th>10</th>
      <td>71.5</td>
      <td>Fairly easy</td>
      <td>374</td>
      <td>176</td>
      <td>1267</td>
      <td>AT&amp;amp;T</td>
      <td>www.att.com</td>
    </tr>
    <tr>
      <th>11</th>
      <td>51.2</td>
      <td>Fairly difficult</td>
      <td>80</td>
      <td>43</td>
      <td>192</td>
      <td>General Electric</td>
      <td>www.ge.com</td>
    </tr>
    <tr>
      <th>12</th>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>AmerisourceBergen</td>
      <td>www.amerisourcebergen.com</td>
    </tr>
    <tr>
      <th>13</th>
      <td>46.1</td>
      <td>Difficult</td>
      <td>55</td>
      <td>13</td>
      <td>89</td>
      <td>Verizon</td>
      <td>www.verizon.com</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20.4</td>
      <td>Very Confusing</td>
      <td>348</td>
      <td>311</td>
      <td>926</td>
      <td>Chevron</td>
      <td>www.chevron.com</td>
    </tr>
    <tr>
      <th>15</th>
      <td>70.3</td>
      <td>Standard</td>
      <td>20</td>
      <td>4</td>
      <td>43</td>
      <td>Costco</td>
      <td>www.costco.com</td>
    </tr>
    <tr>
      <th>16</th>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>Fannie Mae</td>
      <td>www.fanniemae.com</td>
    </tr>
    <tr>
      <th>17</th>
      <td>43.5</td>
      <td>Difficult</td>
      <td>74</td>
      <td>118</td>
      <td>500</td>
      <td>Kroger</td>
      <td>www.thekrogerco.com</td>
    </tr>
    <tr>
      <th>18</th>
      <td>73.3</td>
      <td>Fairly easy</td>
      <td>11</td>
      <td>10</td>
      <td>56</td>
      <td>Amazon.com</td>
      <td>www.amazon.com</td>
    </tr>
    <tr>
      <th>19</th>
      <td>37</td>
      <td>Difficult</td>
      <td>223</td>
      <td>121</td>
      <td>584</td>
      <td>Walgreens Boots Alliance</td>
      <td>www.walgreensbootsalliance.com</td>
    </tr>
    <tr>
      <th>20</th>
      <td>57.9</td>
      <td>Fairly difficult</td>
      <td>273</td>
      <td>149</td>
      <td>763</td>
      <td>HP</td>
      <td>www.hp.com</td>
    </tr>
    <tr>
      <th>21</th>
      <td>39.5</td>
      <td>Difficult</td>
      <td>482</td>
      <td>289</td>
      <td>1316</td>
      <td>Cardinal Health</td>
      <td>www.cardinal.com</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.5</td>
      <td>Difficult</td>
      <td>76</td>
      <td>86</td>
      <td>322</td>
      <td>Express Scripts Holding</td>
      <td>www.express-scripts.com</td>
    </tr>
    <tr>
      <th>23</th>
      <td>45.4</td>
      <td>Difficult</td>
      <td>291</td>
      <td>244</td>
      <td>1343</td>
      <td>J.P. Morgan Chase</td>
      <td>www.jpmorganchase.com</td>
    </tr>
    <tr>
      <th>24</th>
      <td>53.7</td>
      <td>Fairly difficult</td>
      <td>183</td>
      <td>116</td>
      <td>545</td>
      <td>Boeing</td>
      <td>www.boeing.com</td>
    </tr>
    <tr>
      <th>25</th>
      <td>42.7</td>
      <td>Difficult</td>
      <td>1</td>
      <td>4</td>
      <td>25</td>
      <td>Microsoft</td>
      <td>www.microsoft.com</td>
    </tr>
    <tr>
      <th>26</th>
      <td>50.4</td>
      <td>Difficult</td>
      <td>290</td>
      <td>227</td>
      <td>1534</td>
      <td>Bank of America Corp.</td>
      <td>www.bankofamerica.com</td>
    </tr>
    <tr>
      <th>27</th>
      <td>59</td>
      <td>Fairly difficult</td>
      <td>346</td>
      <td>237</td>
      <td>1515</td>
      <td>Wells Fargo</td>
      <td>www.wellsfargo.com</td>
    </tr>
    <tr>
      <th>28</th>
      <td>65.3</td>
      <td>Standard</td>
      <td>254</td>
      <td>56</td>
      <td>723</td>
      <td>Home Depot</td>
      <td>www.homedepot.com</td>
    </tr>
    <tr>
      <th>29</th>
      <td>66.7</td>
      <td>Standard</td>
      <td>5</td>
      <td>4</td>
      <td>29</td>
      <td>Citigroup</td>
      <td>www.citigroup.com</td>
    </tr>
    <tr>
      <th>30</th>
      <td>47.8</td>
      <td>Difficult</td>
      <td>99</td>
      <td>81</td>
      <td>383</td>
      <td>Phillips 66</td>
      <td>www.phillips66.com</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>471</th>
      <td>5.2</td>
      <td>Very Confusing</td>
      <td>170</td>
      <td>175</td>
      <td>417</td>
      <td>Arthur J. Gallagher</td>
      <td>www.ajg.com</td>
    </tr>
    <tr>
      <th>472</th>
      <td>-3422.4</td>
      <td>Very Confusing</td>
      <td>2</td>
      <td>2</td>
      <td>7</td>
      <td>Host Hotels &amp;amp; Resorts</td>
      <td>www.hosthotels.com</td>
    </tr>
    <tr>
      <th>473</th>
      <td>36.5</td>
      <td>Difficult</td>
      <td>477</td>
      <td>206</td>
      <td>1347</td>
      <td>Ashland</td>
      <td>www.ashland.com</td>
    </tr>
    <tr>
      <th>474</th>
      <td>39.9</td>
      <td>Difficult</td>
      <td>32</td>
      <td>28</td>
      <td>105</td>
      <td>Insight Enterprises</td>
      <td>www.insight.com</td>
    </tr>
    <tr>
      <th>475</th>
      <td>42.8</td>
      <td>Difficult</td>
      <td>92</td>
      <td>88</td>
      <td>363</td>
      <td>Energy Future Holdings</td>
      <td>www.energyfutureholdings.com</td>
    </tr>
    <tr>
      <th>476</th>
      <td>47.4</td>
      <td>Difficult</td>
      <td>126</td>
      <td>126</td>
      <td>529</td>
      <td>Markel</td>
      <td>www.markelcorp.com</td>
    </tr>
    <tr>
      <th>477</th>
      <td>57.6</td>
      <td>Fairly difficult</td>
      <td>66</td>
      <td>28</td>
      <td>189</td>
      <td>Essendant</td>
      <td>www.essendant.com</td>
    </tr>
    <tr>
      <th>478</th>
      <td>46.8</td>
      <td>Difficult</td>
      <td>79</td>
      <td>108</td>
      <td>447</td>
      <td>CH2M Hill</td>
      <td>www.ch2m.com</td>
    </tr>
    <tr>
      <th>479</th>
      <td>54.6</td>
      <td>Fairly difficult</td>
      <td>89</td>
      <td>87</td>
      <td>465</td>
      <td>Western &amp;amp; Southern Financial Group</td>
      <td>www.westernsouthern.com</td>
    </tr>
    <tr>
      <th>480</th>
      <td>32.9</td>
      <td>Difficult</td>
      <td>172</td>
      <td>125</td>
      <td>578</td>
      <td>Owens Corning</td>
      <td>www.owenscorning.com</td>
    </tr>
    <tr>
      <th>481</th>
      <td>41.9</td>
      <td>Difficult</td>
      <td>281</td>
      <td>107</td>
      <td>725</td>
      <td>S&amp;amp;P Global</td>
      <td>www.spglobal.com</td>
    </tr>
    <tr>
      <th>482</th>
      <td>36.2</td>
      <td>Difficult</td>
      <td>654</td>
      <td>818</td>
      <td>2929</td>
      <td>Raymond James Financial</td>
      <td>www.raymondjames.com</td>
    </tr>
    <tr>
      <th>483</th>
      <td>36.7</td>
      <td>Difficult</td>
      <td>122</td>
      <td>132</td>
      <td>437</td>
      <td>NiSource</td>
      <td>www.nisource.com</td>
    </tr>
    <tr>
      <th>484</th>
      <td>65</td>
      <td>Standard</td>
      <td>140</td>
      <td>27</td>
      <td>359</td>
      <td>Airgas</td>
      <td>www.airgas.com</td>
    </tr>
    <tr>
      <th>485</th>
      <td>5.5</td>
      <td>Very Confusing</td>
      <td>641</td>
      <td>580</td>
      <td>1534</td>
      <td>ABM Industries</td>
      <td>www.abm.com</td>
    </tr>
    <tr>
      <th>486</th>
      <td>58.8</td>
      <td>Fairly difficult</td>
      <td>199</td>
      <td>208</td>
      <td>1059</td>
      <td>Citizens Financial Group</td>
      <td>www.citizensbank.com</td>
    </tr>
    <tr>
      <th>487</th>
      <td>52</td>
      <td>Fairly difficult</td>
      <td>232</td>
      <td>132</td>
      <td>673</td>
      <td>Booz Allen Hamilton Holding</td>
      <td>www.boozallen.com</td>
    </tr>
    <tr>
      <th>488</th>
      <td>58</td>
      <td>Fairly difficult</td>
      <td>106</td>
      <td>70</td>
      <td>359</td>
      <td>Simon Property Group</td>
      <td>www.simon.com</td>
    </tr>
    <tr>
      <th>489</th>
      <td>40.3</td>
      <td>Difficult</td>
      <td>89</td>
      <td>73</td>
      <td>321</td>
      <td>Domtar</td>
      <td>www.domtar.com</td>
    </tr>
    <tr>
      <th>490</th>
      <td>38.8</td>
      <td>Difficult</td>
      <td>216</td>
      <td>302</td>
      <td>1232</td>
      <td>Rockwell Collins</td>
      <td>www.rockwellcollins.com</td>
    </tr>
    <tr>
      <th>491</th>
      <td>33.1</td>
      <td>Difficult</td>
      <td>337</td>
      <td>143</td>
      <td>651</td>
      <td>Lam Research</td>
      <td>www.lamresearch.com</td>
    </tr>
    <tr>
      <th>492</th>
      <td>36.5</td>
      <td>Difficult</td>
      <td>131</td>
      <td>124</td>
      <td>414</td>
      <td>Fiserv</td>
      <td>www.fiserv.com</td>
    </tr>
    <tr>
      <th>493</th>
      <td>21</td>
      <td>Very Confusing</td>
      <td>366</td>
      <td>452</td>
      <td>1312</td>
      <td>Spectra Energy</td>
      <td>www.spectraenergy.com</td>
    </tr>
    <tr>
      <th>494</th>
      <td>42.9</td>
      <td>Difficult</td>
      <td>54</td>
      <td>109</td>
      <td>435</td>
      <td>Navient</td>
      <td>www.navient.com</td>
    </tr>
    <tr>
      <th>495</th>
      <td>65.1</td>
      <td>Standard</td>
      <td>459</td>
      <td>70</td>
      <td>1059</td>
      <td>Big Lots</td>
      <td>www.biglots.com</td>
    </tr>
    <tr>
      <th>496</th>
      <td>47.1</td>
      <td>Difficult</td>
      <td>129</td>
      <td>84</td>
      <td>380</td>
      <td>Telephone &amp;amp; Data Systems</td>
      <td>www.tdsinc.com</td>
    </tr>
    <tr>
      <th>497</th>
      <td>45.5</td>
      <td>Difficult</td>
      <td>325</td>
      <td>333</td>
      <td>1529</td>
      <td>First American Financial</td>
      <td>www.firstam.com</td>
    </tr>
    <tr>
      <th>498</th>
      <td>64.5</td>
      <td>Standard</td>
      <td>47</td>
      <td>39</td>
      <td>252</td>
      <td>NVR</td>
      <td>www.nvrinc.com</td>
    </tr>
    <tr>
      <th>499</th>
      <td>53.1</td>
      <td>Fairly difficult</td>
      <td>115</td>
      <td>151</td>
      <td>669</td>
      <td>Cincinnati Financial</td>
      <td>www.cinfin.com</td>
    </tr>
    <tr>
      <th>500</th>
      <td>81</td>
      <td>Easy</td>
      <td>33</td>
      <td>10</td>
      <td>113</td>
      <td>Burlington Stores</td>
      <td>www.burlingtonstores.com</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 7 columns</p>
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
    The lists are ready in  0.26  seconds
    


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
    The lists are ready in  0.085  seconds
    


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
      <td>74</td>
      <td>77</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Burlington Stores</td>
      <td>16</td>
      <td>149</td>
      <td>165</td>
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
```


```python
#running the function for the first 25 sites
loadtime (list_company_website,list500_names,list500_url)
```

    The site 15 has NOT been loaded!
    The site 62 has NOT been loaded!
    The site 90 has NOT been loaded!
    The site 97 has NOT been loaded!
    The site 135 has NOT been loaded!
    The site 141 has NOT been loaded!
    The site 161 has NOT been loaded!
    The site 164 has NOT been loaded!
    The site 195 has NOT been loaded!
    The site 216 has NOT been loaded!
    The site 228 has NOT been loaded!
    The site 239 has NOT been loaded!
    The site 242 has NOT been loaded!
    The site 275 has NOT been loaded!
    The site 306 has NOT been loaded!
    The site 326 has NOT been loaded!
    The site 363 has NOT been loaded!
    The site 397 has NOT been loaded!
    The site 414 has NOT been loaded!
    The site 441 has NOT been loaded!
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
      <td>0.212</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exxon Mobil</td>
      <td>3.447</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apple</td>
      <td>0.023</td>
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
    The lists are ready in  3.627  seconds
    


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
      <td>29</td>
      <td>134</td>
      <td>134</td>
      <td>94</td>
      <td>42</td>
      <td>7</td>
      <td>0</td>
      <td>Walmart</td>
      <td>440</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>17</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>Exxon Mobil</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>Apple</td>
      <td>3</td>
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
    The lists are ready in  81.676  seconds
    


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
```


```python
#Run the function unique_dif_sizes
unique_dif_sizes (s_dimensions,list500_names)
```


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
    The lists are ready in  3.429  seconds
    


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
    The lists are ready in  0.301  seconds
    


```python
sizess.tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>company</th>
      <th>144x144</th>
      <th>15x75</th>
      <th>8x15</th>
      <th>44x556</th>
      <th>1x1</th>
      <th>800x1200</th>
      <th>autox100%</th>
      <th>24pxx133px</th>
      <th>21pxx173px</th>
      <th>...</th>
      <th>318x460</th>
      <th>370x630</th>
      <th>75x171</th>
      <th>105x530</th>
      <th>781x1800</th>
      <th>50x100</th>
      <th>360x1306</th>
      <th>306x1306</th>
      <th>338x1306</th>
      <th>82x136</th>
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
      <td>False</td>
      <td>False</td>
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
      <td>False</td>
      <td>False</td>
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
<p>3 rows × 694 columns</p>
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

    The lists are ready in  36.8  minutes
    


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
      <td>814</td>
      <td>1</td>
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
      <td>16</td>
      <td>7</td>
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

    The lists are ready in  20.1  minutes
    The lists are ready in  1208.919  seconds
    


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
result = pd.merge(fort500, html_val, how='inner', on=['company', 'company'])
result2 = pd.merge(social_media, fre, how='inner', on=['company', 'company'])
result3 = pd.merge(sites_links, sizess, how='inner', on=['company', 'company'])
result4 = pd.merge(images_types, loading_time, how='inner', on=['company', 'company'])
result5 = pd.merge(result,result2 , how='inner', on=['company', 'company'])
result6 = pd.merge(result3, result4, how='inner', on=['company', 'company'])
final = pd.merge(result5, result6, how='inner', on=['company', 'company'])
final.head(3)
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
      <td>814</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>29</td>
      <td>134</td>
      <td>134</td>
      <td>94</td>
      <td>42</td>
      <td>7</td>
      <td>0</td>
      <td>440</td>
      <td>0.212</td>
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
      <td>17</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>24</td>
      <td>3.447</td>
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
      <td>16</td>
      <td>7</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0.023</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 729 columns</p>
</div>




```python
final.to_csv('total_500_new.csv', sep=';')
```


```python
data500 = pd.read_csv("total_500_new.csv", sep=';') 
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
      <td>814</td>
      <td>...</td>
      <td>0</td>
      <td>29</td>
      <td>134</td>
      <td>134</td>
      <td>94</td>
      <td>42</td>
      <td>7</td>
      <td>0</td>
      <td>440</td>
      <td>0.212</td>
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
      <td>17</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>24</td>
      <td>3.447</td>
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
      <td>16</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0.023</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 730 columns</p>
</div>




```python

```
