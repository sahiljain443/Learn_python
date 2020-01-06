
"""
This scripts takes JSON script as input and exports a list of app_domains and corresponding app_ccl
Sample JSON file attached with valid JSON format

Created on Mon Jan  6 2020

@author: Sahil Jain
"""
import json

# Load JSON file in 'data' object
with open('C:/Users/ca33443/Desktop/CASB/Netskope/app_domains_raw.json') as json_file:
    data = json.load(json_file)

#'data' is a list of dictionaries
# open a new .xls file to write the values that will be extracted from 'data' object
f = open('C:/Users/ca33443/Desktop/CASB/Netskope/list_of_steered_domains.xls', 'w+')

# iterate on all list entries and write them to file seperated by : and followed by newline
for i in range (len(data)):
    f.write (str(data[i]['app_domains']) + ':' +str(data[i]['app_ccl']) + '\n') 

# Close xls file    
f.close()

