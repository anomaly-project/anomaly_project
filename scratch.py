import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import env


def count_logs():
    ''' function gives a dataframe with the number of visits each path has
    '''
    url = env.get_database('curriculum_logs')
    query = 'select count(logs.date) as visits, path from logs group by path order by visits Desc;'
    df = pd.read_sql(query, url)
    return df


def count_lessons():
    url = env.get_database('curriculum_logs')
    query = 'select count(logs.date) as visits, path, cohort_id from logs group by cohort_id, path order by cohort_id, visits DESC;'
    df = pd.read_sql(query, url)
    df = df.dropna()
    df = df[df['path'] != '/']
    top = df.groupby('cohort_id').head(3).reset_index(drop=True)
    bottom = df.groupby('cohort_id').tail(3).reset_index(drop=True)
    top['in_bottom'] = top['path'].isin(bottom['path'])
    in_both = top[top['in_bottom'] == True]
    in_both['path'] = in_both['path'].drop_duplicates()
    in_both.dropna()
    return in_both