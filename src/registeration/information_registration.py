"Information regitration module"
from pathlib import Path
from typing import Union
from csv import writer
import csv

def read_from_DB(file: Union[str, Path]):
    """Reads information from database asserted that the user has access.
    """
    with open(file) as file_obj:
        # Create reader object by passing the file
        # object to DictReader method
        reader_obj = csv.DictReader(file_obj)

        # Iterate over each row in the csv file
        # using reader object
        for row in reader_obj:
            print(row)


def write_to_DB(db_file, first_name, last_name, personal_id, date_of_birth):
    """

    Args:
        db_file: the database file
        first_name: the first name of a person
        last_name: the last name of a person
        personal_id: the personal id of a person
        date_of_birth: the date of birth of a person

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

# print(read_from_DB("idcard.csv"))
# write_to_DB("idcard.csv", "alireza", "ahmadi", 4, '03-06-1997')
