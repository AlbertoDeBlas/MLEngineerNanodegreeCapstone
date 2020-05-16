# MLEngineerNanodegreeCapstone

This is the Capstone Project for the Machine Learning Engineer Nanodegree of Udacity.

The aim of the project is to analize data to get insights about the kind of population that describes the customer base of the Arvato company and predict from a dataset which people are more likely to become customers.


It is composed by:

  1. Notebooks:
       - Customer Segmentation Report
       - Supervised Learning Model
    
  2. Python custom libraries
       - data_loading:
              Contains functions to load the data into the **notebook
       - data_cleaning :
              Contains functions to clean the data
       - data_visualization:
              Contains functions to plot graphs 
       - feature_selection:
              Contains functions to find feature importance and to fit the model
       - csv_transformation:
              Contains functions to convert data from files to dataframes or viceversa
       - memory_dataframe:
              Contains functions to get information about memory usage of the objects used
       - model_selection:
              Contains functions to know which is the most convenient model or hyperparameters to use
       - import_management:
              Utility function to reload custom libraries without the need to restart the kernel
        
   3. Bash script
       - my_env.sh:
             Script with the lines necessary to put into Sagemaker's notebook configuration--> Lifecycle management to                  upgrade libraries from the base image distribution.
