import pandas as pd
import numpy as np 



def get_program(row):
    if row['program_id'] == 2:
        return 'wd'
    elif row['program_id'] == 3:
        return 'ds'
    else:
        return None
    
    
    
def clean_logs(df):
    
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date')

    df['program'] = df.apply(lambda df: get_program(df), axis=1)
    
    df.drop(columns=['time', 'id', 'slack', 'created_at',
                     'updated_at', 'deleted_at', 'program_id'], inplace = True)
    
    df.dropna(inplace= True)
    
    return df    