import os
import boto3
import mxnet as mx

def loadModelByGroupNumber(k, model_file, job_names, bucket_name):
    '''Load the model trained to group data into k groups
    
    Args:
       k (int): number of groups
       model_name (string): model_name
       job_names (list): list with a model trained for each group in range
       bucket_name (string): name of the s3 bucket
       
    Returns:
       object with the loaded model
    
    '''
    model_key = os.path.join('kmeans/output/',job_names[k], 'output/'+model_file)
    
    # download and unzip model
    boto3.resource('s3').Bucket(bucket_name).download_file(model_key, model_file)
    
    
    #print("Model for k={} ({})".format(k, key))
    os.system('tar -zxvf '+model_file)
    return mx.ndarray.load('model_algo-1')