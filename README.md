# MLEngineerNanodegreeCapstone


## Introduction
This is the Capstone Project for the Machine Learning Engineer Nanodegree of Udacity.

The aim of the project is to analize data to get insights about the kind of population that describes the customer base of the Arvato company and predict from a dataset which people are more likely to become customers.

## Configuration

This project is prepared to run in a Sagemaker's Notebook Instance.

1. Create a Lifecycle configuration
       - Put the lines of my_env.sh in the configuration

2. Create a notebook instance
	- Instance type: ml.m4.xlarge or higher.
	- Add the Lifecycle configuration created
	- Clone from this repository

3. Copy to an S3 bucket the data files

4. Change the AWS Bucket name in `config_data` file

## Data

The datasets used are from Arvato:


  -  `Udacity_AZDIAS_052018.csv`: Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns).
 -   `Udacity_CUSTOMERS_052018.csv`: Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns).
  -  `Udacity_MAILOUT_052018_TRAIN.csv`: Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns).
  -  `Udacity_MAILOUT_052018_TEST.csv`: Demographics data for individuals who were targets of a marketing campaign; 42 833 persons (rows) x 366 (columns).


## Code
It is composed by:

  1. Notebooks:
       - Customer Segmentation Report
       - Supervised Learning Model
    
  2. Python custom libraries
       - `data_loading.py`:
              Contains functions to load the data into the **notebook
    - `data_cleaning.py` :
              Contains functions to clean the data
    - `data_visualization.py`:
              Contains functions to plot graphs 
    - `feature_selection.py`:
              Contains functions to find feature importance and to fit the model
    - `csv_transformation.py`:
              Contains functions to convert data from files to dataframes or viceversa
    - `memory_dataframe.py`:
              Contains functions to get information about memory usage of the objects used
    - `model_selection.py`:
              Contains functions to know which is the most convenient model or hyperparameters to use
    - `import_management.py`:
              Utility function to reload custom libraries without the need to restart the kernel
        
   3. Bash script
    - `my_env.sh`:
             Script with the lines necessary to put into Sagemaker's notebook configuration--> Lifecycle management to                  upgrade libraries from the base image distribution.


## License
 This repository is licensed under GNU General Public License v3.0 . Please read the [LICENSE](https://github.com/AlbertoDeBlas/MLEngineerNanodegreeCapstone/blob/master/LICENSE) before using this repository.
