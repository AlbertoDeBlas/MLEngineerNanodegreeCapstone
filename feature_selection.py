import os
import boto3

def unzipModel(training_job, bucket_name, prefix, model_file, result_filename):
    '''Unzip resulting model and move to the notebook
    
    Args:
       training_job(string): training job name
       prefix (string): prefix where the model is stored
       model_file (string): name of the created model
       result_filename (string): name of the unzipped model
       
    Returns:
       None
    '''
    # where the model is saved, by default
    model_key = os.path.join(prefix, training_job, 'output/'+model_file)
    print(model_key)

    # download and unzip model
    boto3.resource('s3').Bucket(bucket_name).download_file(model_key, model_file)

    # unzipping as model_algo-1
    os.system('tar -zxvf '+model_file)
    os.system('unzip model_algo-1')
    os.system('mv model_algo-1 '+result_filename)
    
# Calculate the explained variance for the top n principal components
# you may assume you have access to the global var N_COMPONENTS
def explained_variance(s, n_top_components):
    '''Calculates the approx. data variance that n_top_components captures.
    Args:
       s (pandas dataframe): dataframe of singular values for top components; 
           the top value is in the last row.
       n_top_components (int): number of top components to use.
     
    Returns: 
       The expected data variance covered by the n_top_components.
    '''
    n_components = len(s) - n_top_components
    partial = s[n_components:].pow(2).sum(axis=0)
    total = s.pow(2).sum(axis=0)

    return partial/total