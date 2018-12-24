# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:11:28 2018

@author: Giulio
"""
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import random
import urllib2
from bs4 import BeautifulSoup


stupidi = "usvacmleUSVACMLE"
#stupidi = "Xpemonye"
stupidi_age = [23,24,24,25,25,26,26,27]


# specify the url
quote_page ='http://en.comuni-italiani.it/regioni.html'
# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value

data = []

dataset = {}


        
        
for tr in soup.find_all('tr')[3:23]:
    tds = tr.find_all('td')
    dataset[tds[1].text]=tds[2].text,tds[3].text,tds[4].text,tds[5].text
         
 
        
cicla = True;
choosen_region ="";
while(cicla):
#for i in range(1,2):
    data = []
    for region in dataset.keys():
        data.append((region,fuzz.ratio(stupidi,region)))
        data = sorted(data, key=lambda x:x[1])
        
        best_five = data[16:]
        best_five.reverse()
        
    for region in best_five:
      
        index_age = random.randint(0,7)
        index_letter = stupidi_age[index_age] / int(dataset[region[0]][3]) ## age / provinces
        #print best_five
        
        if(region[1]< 63 and cicla):
            print region
            
            if(index_letter < len(region[0])):  
             char =  region[0][index_letter] 
             
             if(index_letter < len(stupidi)):
              stupidi = stupidi.replace(stupidi[index_letter],char,1)
              print stupidi, char , index_letter,"=====BEST SUB========="
             else : 
              stupidi_index = random.randint(0,len(stupidi)-1)
              stupidi = stupidi.replace(stupidi[stupidi_index],char,1)
              print stupidi, char , stupidi_index ,"=====MEDIUM SUB===="
             
            else: 
              index_letter = random.randint(0,len(region[0])-1)
              char =  region[0][index_letter] 
              stupidi_index = random.randint(0,len(stupidi)-1)
              stupidi = stupidi.replace(stupidi[stupidi_index],char,1)
              print stupidi, char , stupidi_index ,"=====WORST SUB=="
              
        else :
            if(cicla== True):   
                print region
                cicla = False
              
    
   
 



         
           
    
