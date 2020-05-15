

def filter_csv(string):
    return re.search(r'.csv', string)

def list_csv_files(obj_list):
    '''Returns a list of csv files from the object list of a dict
	
	Args:
		obj_list (dict): list of objects
		
	Returns:
		filterd_list (list): list of csv files
	'''
    files=[]
    for contents in obj_list['Contents']:
        files.append(contents['Key'])

    filtered_list = list(filter(filter_csv, files))

    return filtered_list
    