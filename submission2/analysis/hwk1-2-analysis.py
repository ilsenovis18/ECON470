## Title:           ECON 470 Homework 1 Answers
## Author:          Ilse Novis
## Date Created:    1/29/2025
## Date Edited:     1/29/2025
## Description:     This file renders/runs Python code for the assignment

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Markdown, display
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.DtypeWarning)

# Check current directory
#import os
#print(os.getcwd())

# Read output databases
full_ma_data = pd.read_csv('data/output/full_ma_data.csv')
contract_service_area = pd.read_csv('data/output/contract_service_area.csv')

# Pivot table to get the number of plans per type and year
plans_per_type = full_ma_data.pivot_table(index='plan_type', columns='year', values='planid', aggfunc='count')

# Exluce SNP and EGHP plans, and plans between 800 and 899
final_ma_data = full_ma_data[(full_ma_data['snp'] == "No") & (full_ma_data['eghp'] == "No") & ((full_ma_data['planid'] < 800) | (full_ma_data['planid'] >= 900))]
plans_per_type = final_ma_data.pivot_table(index='plan_type', columns='year', values='planid', aggfunc='count')

# Pivot table to get the average enrollment per plan type and year
enrollment_per_type = final_ma_data.pivot_table(index='plan_type', columns='year', values='avg_enrollment', aggfunc='mean')