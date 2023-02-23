import pandas as pd
import numpy as np 
import os

from env import get_database


def get_log_data():
    '''
    This function is to get the log dataset from a local csv file or from SQL Ace to our working notebook to be able to
    use the data and perform various tasks using the data
    ''' 
    
    if os.path.isfile('curriculum_logs.csv'):
        
        return pd.read_csv('curriculum_logs.csv')
    
    else:
       
        url = get_database('curriculum_logs')
        
        query = '''
        SELECT *
        FROM logs as l
        JOIN cohorts as c
        ON c.id = l.cohort_id;
        '''

        df = pd.read_sql(query, url)
        
        df.to_csv('curriculum_logs.csv', index = False)

        return df   