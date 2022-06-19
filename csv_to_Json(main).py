#!/usr/bin/env python
# coding: utf-8

# #Task 
# Create CSV file from Json
# 
# https://jsonplaceholder.typicode.com/posts
# or download atttached file
# 
# Save the content of above URL as JSON. With your python script read the  JSON (save as dictionary in python)
# Write the contents as CSV file.
# 
# 
# The JSON have 100 posts and so the result CSV file should have 101 line (1 Header, 100 records).

# In[ ]:


import json
import csv

#Loading the data from main1.json file
with open(r"main1.json") as f:
    data = json.load(f)

    
#Opening a new csv file to write the data in
    csv_file1 = open("csv_file1.csv", 'w')

    
#Creating a csv writer object
    csv_writer = csv.writer(csv_file1)


    count = 0

#Adding the keys as header in 1 row & Values as corresponding rows below the header
    for i in data:                                   
        if count == 0:
            headers = i.keys()
            csv_writer.writerow(headers)
            count += 1

        csv_writer.writerow(i.values())


# In[74]:


#Raw code: Incomplete

import json
import csv
with open(r"main1.json") as f:
    data = json.load(f)
    #print(data)

#userdata = data['user']
#print(userdata)

csv_file = open("csv_file1.csv", 'w')

csv_writer = csv.writer(csv_file1)


count = 0

for i in data:
    if count == 0:
    
        headers = i.keys()
        print(headers)
        print(i.values())
        csv_writer.writerow(headers)
        count += 1
        
    csv_writer.writerow(i.values())
    
csv_file.close()

    
    


# In[ ]:




