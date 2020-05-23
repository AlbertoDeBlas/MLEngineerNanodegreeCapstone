import pandas as pd
import ast

def csvToDataFrame(filename):
    '''Read a csv into a dataframe
    Args:
       filename (string): name of the csv file
       
    Returns:
       dataframe with the csv data
    '''
    df = pd.read_csv(filename, nrows = 1, header = None)
    
    col_types = []
    for column in range(1, df.shape[1]-1):
        df[column] = pd.to_numeric(df[column], downcast='float')
        
    # create the dict of index names and optimized datatypes
    dtypes = df.dtypes
    colnames = dtypes.index
    types = [i.name for i in dtypes.values]
    column_types = dict(zip(colnames, types))

    df = pd.read_csv(filename,dtype=column_types, header = None)

    last_col_index = df.shape[1]-1

    df[0] = df[0].apply(lambda x: str(x)[15:])
    df[0] = pd.to_numeric(df[0], downcast='float')
    df[last_col_index] = df[last_col_index].apply(lambda x: str(x)[:-2])
    df[last_col_index] = pd.to_numeric(df[last_col_index], downcast='float')
    
    return df


def csvToDataFrameLinear(filename):
    '''Read a csv into a dataframe, specific for the LinearLearner transformation output
    Args:
       filename (string): name of the csv file
       
    Returns:
       dataframe with the csv data
    '''
    df = pd.read_csv(filename, nrows = 1, header = None)
    
    col_types = []
    for column in range(1, df.shape[1]-1):
        df[column] = pd.to_numeric(df[column], downcast='float')
        
    # create the dict of index names and optimized datatypes
    dtypes = df.dtypes
    colnames = dtypes.index
    types = [i.name for i in dtypes.values]
    column_types = dict(zip(colnames, types))

    df = pd.read_csv(filename,dtype=column_types, header = None,names = ['zero', 'Response'])

    last_col_index = df.shape[1]-1

    df['zero'] = df['zero'].apply(lambda x: str(x)[38:-1])
    df['zero'] = pd.to_numeric(df['zero'], downcast='float')
    df['Response'] = df['Response'].apply(lambda x: str(x)[6:-2])
    df['Response'] = pd.to_numeric(df['Response'], downcast='float')
    df = df.drop('zero', axis = 1)
    
    return df



def readKmeanResultToDF(filename):
    '''Read kmean transformation results to a dataframe
    
    Args: 
       filename (string): name of the file with the kmean results
       
    Returns:
       dataframe with the results
    
    '''
    file = open(filename, "r")

    Lines = file.readlines() 

    count = 0
    
    content_list = []

    for line in Lines: 
        # Strips the newline character 
        contents = line.strip()
        
        content_dict = ast.literal_eval(contents)
        content_list.append(content_dict)
    
    return pd.DataFrame(content_list)