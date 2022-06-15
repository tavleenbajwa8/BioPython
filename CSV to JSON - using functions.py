#!/usr/bin/env python
# coding: utf-8

# def read_file(path) -> file || [],{}
# 
# def transform(file) -> []
# 
# def write_file(path,[]) -> None || '' || true
# 
# Use functions stated above (or more) to reorganize csv_to_dict script
# 
# use json module to convert data structure (dictionary) to write to a file
# 
# json validator: https://jsonlint.com/
# 
# Note: if facing issue with input file you can take any csv file from the following URL for more simpler, cleaner CSV input
# 
# https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html

# In[1]:


import json
import csv

def csv_to_json(csv_path, json_path):

    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = {"addresses": []}
        for row in reader:
             data["addresses"].append({"firstname":
             row[0], "lastname": row[1], "Building": row[2], "Town": row[3], "City": row[4], "Pin": row[5]})

    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)


csv_path = r'C:\Users\Lakshya\Downloads\addresses.csv'
json_path = 'addresses3.json'
csv_to_json(csv_path,json_path)

