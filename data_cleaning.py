import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

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
       column converted from timestamp to float
    
    '''
    timestamp =  pd.to_datetime(df[column]) ## pandas recognizes your format

    df[column] = timestamp.dt.strftime('%Y%m%d')
    df[column] = df[column].replace('NaT', 'NaN')
    return df[column].astype('float')

def timestampToInt(df, column):
    '''Convert to int a datetime column
    
    Args:
       df (pandas dataframe): dataframe 
       column (string): column name
       
    Returns:
       column converted from timestamp to int
    
    '''
    timestamp =  pd.to_datetime(df[column]) ## pandas recognizes your format

    df[column] = timestamp.dt.strftime('%Y%m%d')
    return df[column].astype('int32')


def to_category(df, categorical_columns):
    '''Convert to categorical a list of columns
    
    Args:
       df (pandas dataframe): dataframe 
       categorical_columns (list): list of columns to convert to category
       
    Returns:
       dataframe with converted columns
    
    '''
    for column in categorical_columns:
        df[column] = df[column].astype('category', inplace = True)
    
    return df

def to_int(df, categorical_columns):
    '''Convert to int a list of columns
    
    Args:
       df (pandas dataframe): dataframe 
       categorical_columns (list): list of columns to convert to int
       
    Returns:
       dataframe with converted columns
    
    '''
    for column in categorical_columns:
        df[column] = df[column].astype('uint8', inplace = True)
    
    return df

#Inspired in https://towardsdatascience.com/make-working-with-large-dataframes-easier-at-least-for-your-memory-6f52b5f4b5c4
def impute_mode_categorical(df):
    '''Impute mode into categorical columns of the dataframe 
    (objects and category types)
    
    Args:
       df (pandas dataframe): dataframe 
       
    Returns:
      dataframe with imputed NaNs
    
    '''
    categorical_columns= df.select_dtypes(include=['O','category'])
    cols = list(df)
    
    for column in categorical_columns: 
        col_data = df[column]
        col_data.replace(-1,np.nan, inplace = True)
        null_data = sum(col_data.isna())
        mode = col_data.mode()[0]
        if null_data > 0:
            col_data.fillna(mode, inplace=True)
            
    return df

def impute_median_numerical(df):
    '''Impute median into numerical columns of the dataframe 
    (objects and category types)
    
    Args:
       df (pandas dataframe): dataframe 
       
    Returns:
      dataframe with imputed NaNs
    
    '''
    numeric_cols = df.select_dtypes(include=['int','float'])
    cols = list(df)
    
    for column in numeric_cols: 
        col_data = df[column]
        
        col_data.replace(-1,np.nan, inplace = True)
        null_data = sum(col_data.isna())
        median = col_data.median()
        if null_data > 0:
            col_data.fillna(median, inplace=True)
            
    return df


def encodeColumnByLabel(df, label):
    label_encoder = LabelEncoder()
    label_encoder.fit(df[label])
    return label_encoder.transform(df[label])