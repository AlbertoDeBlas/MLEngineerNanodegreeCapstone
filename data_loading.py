import re
import io
import pandas as pd
import ast

def read_config(file_name):
    '''Returns config values to run the notebook
    
    Args:
       file_name (string): name of the config file
       
    Returns:
       dict with the configuration items 
    '''
    with open(file_name, "r") as data:
        dictionary = ast.literal_eval(data.read())
    
    return dictionary

def filter_csv(string):
    return re.search(r'.csv', string)

def list_csv_files(obj_list):
    '''Returns a list of csv files from the object list of a dict
	
	Args:
		obj_list (dict): list of objects
		
	Returns:
		filtered_list (list): list of csv files
	'''
    files=[]
    for contents in obj_list['Contents']:
        files.append(contents['Key'])

    filtered_list = list(filter(filter_csv, files))

    return filtered_list

def load_dataframe_from_s3(s3_client, bucket, name):
    '''Returns a csv file from s3
    
    Args:
        s3_client(): s3 client object
        bucket: s3 bucket where the file is located
        name: name of the csv file
        
    Returns:
        pandas dataframe
    
    '''
    data_object = s3_client.get_object(Bucket=bucket, Key=name)
    data_body = data_object["Body"].read()
    data_stream = io.BytesIO(data_body)
    
    return pd.read_csv(data_stream, header=0, delimiter=",") 
