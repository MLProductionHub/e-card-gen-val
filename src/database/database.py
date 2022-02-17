from genericpath import exists
from pathlib import Path
from typing import List, Union
import os
import csv

def init_DB(database_path: Union[str, Path], headers: List[str]) -> str:
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
     
    


