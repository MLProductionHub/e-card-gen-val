from pathlib import Path
from typing import Dict, List, Union
import os
import csv

def init_database(database_path: Union[str, Path], headers: List[str]) -> str:
    """Creates a new csv file as the database with the given headers.

    Args:
        database_path (Union[str, Path]): path of the database
        headers (List[str]): a list of the headers for csv file

    Returns:
        str: the absolute address of the database file
    """
    database_path = os.path.expanduser(database_path) # Creating the absolute path
    if os.path.exists(database_path): # checking for existing databases
        print("The database file already exists.")
    else:
        with open(database_path, mode='w') as f:
            writer = csv.writer(f) # initialize the csv writer

            writer.writerow(headers) # write the header line
    
    return str(database_path) # print the file address

def write_to_database(database: Union[str, Path], info: Dict[str, object]):
    """Writes a row in the dataset given the values as a dictionary.

    Args:
        database (Union[str, Path]): The path to the database we want to use or initiate
        info (Dict[str, object]): The dictionary contatining the key and values. (Values should be iterables)
    """
    database = os.path.expanduser(database) # create the absolut path to database
    args = list(info.values()) # values to be stored

    try: 
        for values in args:
            assert len(values) == len(args[0]) # checking that all lists have the same length
        args_size = len(args[0])
    
    except AssertionError:
        print("The values are not the same size. The inputs will be deprecated to the minimum compatible size.")
        args_size = min([len(values) for values in args]) # in case of different length the minimum length is considered


    if os.path.exists(database): # the case that database already exists
        with open(database, "a") as file: # writing in database
            writer = csv.writer(file) 
            for i in range(args_size):
                row  = []
                for values in args:
                    row.append(values[i])
                writer.writerow(row)
    else: # case of database not existing
        headers = list(info.keys()) # headers of database
        database_path = init_database(database, headers) # initializing the database
        with open(database_path, "a") as file: # writing in the database
            writer = csv.writer(file)
            for i in range(args_size):
                row  = []
                for values in args:
                    row.append(values[i])
                writer.writerow(row)
