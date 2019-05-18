# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:48:26 2019

@author: jzhao124
"""

import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

pt = pd.read_csv("F:\Jupyter\personalized_incentive_data\predict_target.csv")


results = confusion_matrix(pt['t'], pt['p']) 
print ('Confusion Matrix :')
print(results) 
print ('Accuracy Score :', accuracy_score(pt['t'], pt['p']) )
print ('Report : ')
print (classification_report(pt['t'], pt['p']) )

loca1 = pd.read_csv("C:\Users\jzhao124\Desktop\Generated_Diary.csv")
loca2 = pd.read_csv("C:\Users\jzhao124\Desktop\Generated_Diary_2.csv")






# calculate purposes of background logging trips
def cal_trip_purpose_bgl(trips, turple_purpose, locations):    
    # the locations = (home_lat, home_long, work_lat, work_long)    
    # the turple_purpose is (hw_purpose, hw_purpose)
    len_trips = len(trips)
    result_list = []
    
    # if the location data is missing from the location table
    if len(locations) == 0:
        return ['NONCOMMUTE'] * len_trips
    
    if turple_purpose[0] == True and turple_purpose[1] == True:
        result_list = ['NONCOMMUTE'] * len_trips
    else:
        (hw_origin_index, hw_destination_index) = find_hw_origin_des_index(trips, locations)
        (wh_origin_index, wh_destination_index) = find_wh_origin_des_index(trips, locations)
        for i in range(len_trips):
            if i >= hw_origin_index and i <= hw_destination_index:
                result_list.append('HW')
            else:
                if i >= wh_origin_index and i <= wh_destination_index:
                    result_list.append('WH')
                else:
                    result_list.append('NONCOMMUTE')
    return result_list
    