# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:28:35 2021

@author: Lennart
"""

#%% importing libraries 
import csv
import glob
import os
import pandas as pd
import json

#%% merge Tweet-files to one csv-file

################ get the path of each json-file (incl. file-name) ################
## to get your directory change the varaible path and the folder 'tweet' to yours 
### if you have stored the json-files as another file-type just change the '*.txt'
path = (r'C:\Users\Lennart\Documents\Studium\master_sociology\0_MAThesis\data') 
file_list = glob.glob(os.path.join(path, 'tweet', '*.txt')) 

data = pd.DataFrame()

#load files, transpose the dataframes
for file_path in file_list:
        with open(file_path, 'r', errors = 'ignore') as file:   
            reader = json.load(file)
            reader = pd.DataFrame.from_dict(reader['raw_data'], orient = 'index')
            reader = reader.rename_axis('columns').reset_index().T
            reader = pd.DataFrame(reader.values[1:], columns = reader.iloc[0])
        
            #merge all files to one dataframe        
            for i in range(0,1):
                data = data.append(reader)
                
#stores the dataframe of all Tweets as one csv-file at your cd                
data.to_csv('./tweets_hateSpeech_2015-2020.csv', sep = ',', index = False) 
