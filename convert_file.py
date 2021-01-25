import csv
import sys
import pprint



# Function to convert a csv file to a list of dictionaries.
def csv_dict_list(name_file):
     
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
 
    reader = csv.DictReader(open(name_file, 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

