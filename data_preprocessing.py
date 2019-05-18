# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:39:42 2019

@author: jzhao124
"""

# data-preprocessing
import pandas as pd

total_data = pd.read_csv('F:\\Jupyter\\personalized_incentive_data\\total.csv')

total_data['trip_mode'] = pd.factorize(total_data['trip_mode'])[0] + 1

total_data['trip_purpose'] = pd.factorize(total_data['trip_purpose'])[0] + 1

total_data['is_selected'] = pd.factorize(total_data['is_selected'])[0] + 1

total_data.to_csv('F:\\Jupyter\\personalized_incentive_data\\total_processed.csv')