import pandas as pd
import numpy as np

def dropMissingColumns(df, threshold = 20):
    '''Make a dict with the names of the columns and then drop this columns from dataframe 
    
    Args:
        df (pandas dataframe): dataframe with columns to be dropped
        threshold (int): Percentage of missing values
        
    Returns:
        None
    
    '''
    rows = df.shape[0]
    missing_percentages = df.isnull().sum().sort_values(ascending = False).divide(other = (rows/100))
    drop_columns = missing_percentages[missing_percentages > threshold]
    df.drop(columns = list(drop_columns.index), axis = 1, inplace = True)
    
def getVariances(df):
    '''Get a list with the variance of each dataframe column
    
    Args:
        df (pandas dataframe): dataframe with columns to have variance calculated
        
    Returns:
        pd.Series: Series object with the columns variances
    
    '''
    df_description = df.describe()
    std_df = df_description.loc[['std']].values.reshape(df_description.shape[1],)
    return pd.Series(std_df, index =df_description.columns) 

def dropLowVarianceCols(df, threshold = 0.5):
    '''Drop the columns with a variance lower than a threshold
    
    Args:
        df (pandas dataframe): dataframe with columns to be dropped
        threshold (float): minimum variance to keep columns
        
    Returns:
        index (pandas Index): index values of columns dropped
    '''
    std_serie = getVariances(df)

    drop_lowdispersion_cols = std_serie[std_serie < threshold]
    print("Dropping columns: ",drop_lowdispersion_cols)
    df.drop(columns = list(drop_lowdispersion_cols.index), axis = 1, inplace = True)
    
    return drop_lowdispersion_cols.index

def dropColumnsWithUniqueValues(df):
    '''Drop the columns that have all different values
    
    Args:
       df (pandas dataframe): dataframe 
       
    Returns:
       df (pandas dataframe): dataframe with unique value columns dropped
    
    '''
    rows = df.shape[0]
    df = df.loc[:, ( (df.nunique()/rows) < 1.0)]
            
    return df

def replaceForNan(df):
    '''Replace values of dataframe for NaN
       Warning: This is a very specific function that only applies to
                Arvato Datasets.
       
    Args:
       df (pandas dataframe): dataframe   
    
    Returns:
       None
    
    '''
    df['CAMEO_INTL_2015'].replace('XX',np.nan,inplace = True)
    df['CAMEO_DEUG_2015'].replace('X',np.nan, inplace = True)
    df['EINGEFUEGT_AM'].replace('NaT',np.nan, inplace = True)

def timestampToFloat(df, column):
    '''Replace NaT for NaN values and convert to float a column
    
    Args:
       df (pandas dataframe): dataframe 
       column (string): column name
       
    Returns:
       Colum converted from timestamp to float
    
    '''
    timestamp =  pd.to_datetime(df[column]) ## pandas recognizes your format

    df[column] = timestamp.dt.strftime('%Y%m%d')
    df[column] = df[column].replace('NaT', 'NaN')
    return df[column].astype('float')