import pandas as pd

def memory_usage(df):
    '''Function to calculate memory usage of a dataframe in megabytes
    
    Args:
       df (pandas dataframe): dataframe
       
    Returns:
       Memory used
    '''
    return(round(df.memory_usage(deep=True).sum() / 1024 ** 2, 2))

