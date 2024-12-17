# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 06:56:02 2022

@author: kople

Usage manual: Read readme.md
    
"""

#%% Imports

import psycopg2
import pandas as pd
import seaborn as sn
import numpy as np

import os

#%% Set working directory

print(os.getcwd())
os.chdir(r'C:\Users\kople\Documents\Work\RA\Student-Engagement_Prediction')
print(os.getcwd())

#%% Connect to database

# from sqlalchemy import create_engine
# engine1 = create_engine('postgresql+psycopg2://postgres:zarif311998@localhost/C:/Users/kople/Documents/Work/RA/spectrumdbbackup/sess1819sem2')

conn = psycopg2.connect(database='sess1819sem2',host='localhost',user='postgres',password='zarif311998')
cur = conn.cursor()
#%% Query
query = 'SELECT * FROM mdl_grade_grades'
# EXECUTE1 = cur.execute(query)
# RESULT = cur.fetchall()

grades = pd.read_sql_query(query,conn)

save = r'C:\Users\kople\Documents\Work\RA\data'
#grades.to_csv(f'{save}/raw/sess1819sem2/grades.csv', index=False)


# %%
