"""initializes a new database for storing the users informations."""

from genericpath import exists
from pathlib import Path
from typing import List, Union
import os
import csv

def init_DB(DB_name: str, headers: List[str]) -> str:
    """Creates a new csv file as the database with the given headers.

    Args:
        DB_name (str): name of the database
        headers (List[str]): a list of the headers for csv file

    Returns:
        str: the absolute address of the database file
    """
    root_path = os.getcwd() # getting the current working directory as the root directory
    data_path = os.path.join(root_path, "data") # create the data folder path

    if os.path.exists(data_path): # checking if the data directory exists
        database_path = os.path.join(data_path, DB_name+".csv") # database path
    else:
        os.mkdir(data_path) # creating the path if it doesn't exist
        database_path = os.path.join(data_path, DB_name+".csv") # database path

    if os.path.exists(database_path): # checking for existing databases
        print("The database file already exists.")
    else:
        with open(database_path, mode='w') as f:
            writer = csv.writer(f) # initialize the csv writer

            writer.writerow(headers) # write the header line
    
    return str(database_path) # print the file address

if __name__ == "__main__":
    headers = ['a', 'b', 'c']
    db_name = "testdb"
    init_DB(db_name, headers)


