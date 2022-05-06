#!/usr/bin/env python
# coding: utf-8

# In[12]:


#testing nested creation of dictionaries 

import csv #to open csv file
import json #to output data clearly 
import time #time library
data_dict2 = {}

array = [0,1,2,5] #array for selecting variables from file
#0 is book id - thinking about removing after finished
#1 is title 
#2 is author - note that multiple authors are seperated with a / 
#5 is isbn-13 
#any of the below variables can be selected to add into the database for more work 
#not included 3-average ratings, 4-isbn-10, 6-lang, 7-pages, 8-ratings count, 9-text reviews, 10-publication date, 11-publisher 

index = 0
with open("books.csv", 'r', encoding="utf-8") as fin:
    csvreader = csv.reader(fin, delimiter=",")
    header = []

    for row in csvreader:
        if index == 0:
            header = row
            index += 1
            continue
        #Create dict of book with info of headers        
        data_dict2[row[0]] = {'title':row[1] ,'author':row[2],'isbn-13':row[5]}
            
            
#Data
print(json.dumps(data_dict2,indent = 4))

#print(data_dict2)
#data_dict.items()

#print(data_dict2)


# In[ ]:





# In[ ]:




