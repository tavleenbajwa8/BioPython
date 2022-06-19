#!/usr/bin/env python
# coding: utf-8

#Task: 1. Read given FASTA file
# 2. For each sequence find possible WD repeats i,e region of length 35-45 amino acid bases that  starts with GH or ends with WD (or both GH in start and WD in the end).
# 3. save output in given format.


# example input:
# >sp|P61964|43-82
# GHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKTGHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKTGHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKTGHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKTGHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKTGHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKTGHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKT
# >sp|P61967|43-82
# GHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKT
# >sp|P61968|43-82
# GHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKT
# >sp|P619649|43-82
# GHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKT
# >sp|P61964|43-82
# GHTKAVSSVKFSPNGEWLASSSADKLIKIWGAYDGKFEKT


# example output:
# uniprotId : P61964
# GHkjbkjbkjbkjbjkbjkbjkbkj 40 10-50
# mhvkjbjbkjbkjbkjbkjbkjbkjbwd 40 55-90

# total repeats: 2

# uniprotId : P619649
# GHkjbkjbkjbkjbjkbjkbjkbkj 40 10-50
# mhvkjbjbkjbkjbkjbkjbkjbkjbwd 40 55-90


#Code:

import re
data = {}                                 #Defining empty dictionary
current_id = ''
f = open(r"example.fasta")
#print(f.read())
for i in f.readlines():
    if i.startswith(">"):
        temp_id = i.split('|')[1]           #Splitting the line based on "|" as delimiter and taking 1st index which is the UniProt ID, storing it in var 'temp_id'
        
        #optional
        if current_id != temp_id:           #Updating the value of current id with temp ids as the loop moves across the lines
            current_id = temp_id
    else:
        #print(data)
        if current_id not in data:
            data[current_id] = i.replace('\n', '')            #Appending the first line after replacing "\n" into the respective key as value
            
            #print(data)
        else:
            data[current_id] += i.replace('\n', '')           #Followed by appending next 3 lines
        
pattern = 'GH[A-Z]{0,35}WD'                                   #Defining the regex pattern to be searched

for d in data:
    match = re.findall(pattern, data[d])                               #Finding all the matching sequences using re.findall
    index = [(m.start(0), m.end(0)) for m in re.finditer(pattern, data[d])]            #Finding all the respective indexes using re.finditer
    l = dict(zip(match,index))                                                  #Zipping the two lists into a dictionary

    print("Prot Id:",d, "--- Matched sequences are: ", l)
    
    print("Total no.of repeats:",len(match))                        
    print("---------------------------------")


