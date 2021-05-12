#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Specify the name of the input file csv in quotes "". Be sure that have you column named 'Course_id' and 'Username" in the CSV. 
#Put the name of the folder and "\" before the name of file like "Folder\input.csv"
#This assumes they are in the same working directory. you can use another working directory in the same way. "otherwd\Folder\input.csv"

#Example: csv_to_load = "Input_Files\Test1.csv"

csv_to_load = "Input_Files\Input01.csv"


#2 Specify the name of the output file, this is a log of results. 
#Example output_csv = "Output_Files\Output1.csv"

output_csv = "Output_Files\Output1.csv"


# In[2]:


import requests
import json
import csv
import pandas as pd



# 1. Create a CSV with the course ID# and email address of user who completed the course. Important: Add the name of CSV on the first line of code
import_csv = pd.read_csv(csv_to_load)
#2 Create a list of the Course_Id column
CourseID_list = import_csv['Course_id'].tolist()
#3 Create a list of the Username Column
Username_list = import_csv['Username'].tolist()


#4 Create the Empty Lists, these are the columns in output file. Each list will be populated with the for loop below as it iterates through the csv
index_list = []
completion_list = []
username_list = []
post_list = []
index = 0

#5 Loop through the Course_ID_list. The loop creates JSON from the lists above and the posts it through the API. 
for row in CourseID_list:
    endpoint = "https://advantagelearning.ivanti.com/incoming/v2/courseExternalActivity"
    headers = {"Authorization": "Bearer ENTER YOUR API KEY HERE", "Content-Type": "application/json"}
    data = json.dumps({"courseId": CourseID_list[index], "userEmail": Username_list[index]})
    post1 = requests.post(endpoint, headers=headers, data=data)
    index_list.append(str(index))
    completion_list.append(str(CourseID_list[index]))
    username_list.append(Username_list[index])
    post_list.append(str(post1))
    index +=1

#6 Write the output to csv
dict = {"Index":index_list, 'Username':username_list, "Course_ID": completion_list, "HTTP Response": post_list}
Output_df = pd.DataFrame(dict)        
Output_df.to_csv(output_csv)                          
print(Output_df)                          
    


# In[ ]:




