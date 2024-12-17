""" This script is primarily for debugging the find_student_email function used in the notebooks. """

## Imports
import re
import pandas as pd
import numpy as np
import os
#print(os.getcwd())



## Function to find student emails
def find_student_email(email):

    pattern = re.compile(r'[a-zA-Z0-9]+@siswa.um.edu.my$') 
    if type(email)==str:
        if(re.search(pattern,email)):
            return email
        else:
            #print('Not a student\'s email')
            pass
    else:
        #print('no email')
        pass
        



users = pd.read_csv('./data/raw/users.csv') ## Importing the data
student_emails = [] # Creating empty list to store student emails



for e in users.email:
    if find_student_email(e)==e:
        if e not in student_emails:
            student_emails.append(e)

print('for loop results')
print(student_emails[0:5])   
print(len(student_emails)) 

student_emails_iterator = filter(find_student_email,users.email)
print('filter() results')
student_emails = list(student_emails_iterator)
print(len(student_emails))