# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:28:35 2021
w/ python 3.7.6
@author: Lennart

!Attention: this isn't the fastest/cleanest solution, tho 
one of the faster solutions are to compute it w/ an array instead of a dataframe 
computional time depends on your kernel, etc.
data is quite big 
    -> 1 million files in total, files are up to 13KB 
therefore, I split the Tweet-files in 4 folders to ensure the memory capacity is sufficient
this results in 4 different code blocks that do the same, just with other files
computional time w/ 8GB RAM, 2.9Ghz 4MB L3 cache:
    each block ~ 12h    
"""

#%% importing libraries 
import glob
import os
import pandas as pd
import json

#cd of the data
path = (r'C:\Users\Lennart\Documents\Studium\master_sociology\0_MAThesis\data')
#%% merge Tweet-files to one csv-file Vol. I

################ get the path of each json-file (incl. file-name) ################
## to get your directory change the varaible path and the folder 'tweet' to yours 
### if you have stored the json-files as another file-type just change the '*.txt'
path = (r'C:\Users\Lennart\Documents\Studium\master_sociology\0_MAThesis\data') 
file_list = glob.glob(os.path.join(path, 'tweet', '*.txt')) 

data = pd.DataFrame()

# load files, transpose the dataframes
for file_path in file_list:
        with open(file_path, 'r', errors = 'ignore') as file:   
            reader = json.load(file)
            reader = pd.DataFrame.from_dict(reader['raw_data'], orient = 'index')
            reader = reader.rename_axis('columns').reset_index().T
            reader = pd.DataFrame(reader.values[1:], columns = reader.iloc[0])
        
            # merge all files to one dataframe
            ## if you use python 2 change range to xrange
            for i in range(0,1):
                data = data.append(reader)
              
# stores the dataframe of all Tweets as one csv-file at your cd                
data.to_csv('C:/Users/Lennart/OneDrive/0_MAThesis/data/tweets_hateSpeech_2015-2020.csv', sep = ',', index = False)

#%% merge Tweet-files to one csv-file Vol. II
path = (r'C:\Users\Lennart\Documents\Studium\master_sociology\0_MAThesis\data') 
file_list1 = glob.glob(os.path.join(path, 'tweet1', '*.txt'))

data1 = pd.DataFrame()

for file_path in file_list1:
    with open(file_path, 'r', errors = 'ignore') as file1:
        reader1 = json.load(file1)
        reader1 = pd.DataFrame.from_dict(reader1['raw_data'], orient = 'index')
        reader1 = reader1.rename_axis('columns').reset_index().T
        reader1 = pd.DataFrame(reader1.values[1:], columns = reader1.iloc[0])
        
        for i in range(0,1):
            data1 = data1.append(reader1)
            
data1.to_csv('C:/Users/Lennart/OneDrive/0_MAThesis/data/tweets_hateSpeech_2015-2020_1.csv', sep = ',', index = False)

#%% merge Tweet-files to one cs-file Vol. III

file_list2 = glob.glob(os.path.join(path, 'tweet2', '*.txt'))

data2 = pd.DataFrame()

for file_path in file_list2:
    with open(file_path, 'r', errors = 'ignore') as file2:
        reader2 = json.load(file2)
        reader2 = pd.DataFrame.from_dict(reader2['raw_data'], orient = 'index')
        reader2 = reader2.rename_axis('columns').reset_index().T
        reader2 = pd.DataFrame(reader2.values[1:], columns = reader2.iloc[0])
        
        for i in range(0,1):
            data2 = data2.append(reader2)
            
data2.to_csv('C:/Users/Lennart/OneDrive/0_MAThesis/data/tweets_hateSpeech_2015-2020_2.csv', sep = ',', index = False)

#%% merge Tweet-files to one csv-file Vol. IV

file_list3 = glob.glob(os.path.join(path, 'tweet3', '*.txt'))

data3 = pd.DataFrame()

for file_path in file_list3:
    with open(file_path, 'r', errors = 'ignore') as file3:
        reader3 = json.load(file3)
        reader3 = pd.DataFrame.from_dict(reader3['raw_data'], orient = 'index')
        reader3 = reader3.rename_axis('columns').reset_index().T
        reader3 = pd.DataFrame(reader3.values[1:], columns = reader3.iloc[0])
        
        for i in range(0,1):
            data3 = data3.append(reader3)
            
data3.to_csv('C:/Users/Lennart/OneDrive/0_MAThesis/data/tweets_hateSpeech_2015-2020_3.csv', sep = ',', index = False)

#%% merge all user-files to one csv-file

file_list_user = glob.glob(os.path.join(path, 'user', '*.txt'))

data_user = pd.DataFrame()

for file_path in file_list_user:
    with open(file_path, 'r', errors = 'ignore') as user:
        j = json.load(user)
        j = pd.DataFrame.from_dict(j['raw_data'], orient = 'index')
        j = j.rename_axis('columns').reset_index().T
        j = pd.DataFrame(j.values[1:], columns = j.iloc[0])
        
        for i in range(0,1):
            data_user = data_user.append(j)
            
data_user.to_csv('C:/Users/Lennart/OneDrive/0_MAThesis/data/user_hateSpeech_2015-2020.csv', sep = ',', index = False)
