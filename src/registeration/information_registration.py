"Information regitration module"
from pathlib import Path
from typing import Union
import pandas as pd
from csv import writer


def read_from_DB(file: Union[str, Path]):
    """Reads information from database asserted that the user has access.
    """
    dataset = pd.read_csv(file, encoding='utf-8')
    for index, row in dataset.iterrows():
        first_nam = row[0]
        last_name = row[1]
        personal_id = row[2]
        date_of_birth = pd.to_datetime(row[3]).strftime('%m/%d/%Y')
        return first_nam, last_name, personal_id, date_of_birth
    pass


def write_to_DB(db_file, first_name, last_name, personal_id, date_of_birth):
    """

    Args:
        db_file:
        first_name:
        last_name:
        personal_id:
        date_of_birth:

    Returns: Writes information to database (Only admin can use this method)

    """
    row = [first_name, last_name, personal_id, date_of_birth]
    with open(db_file, 'a') as file:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(file)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(row)

        # Close the file object
        file.close()


def get_info():
    """Submits the formatted output information that is requested.
    """
    pass


def import_info():
    """Writes the formatted input information that is provided by user (Admin should provide access)."""
    pass


# write_to_DB("idcard.csv", "alireza", "ahmadi", 4, '03-06-1997')
