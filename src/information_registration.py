"Information regitration module"
import pandas as pd

def read_from_DB(file):
    """Reads information from database asserted that the user has access.
    """
    dataset = pd.read_csv(file, encoding='utf-8')
    for index, row in dataset.iterrows():
        first_name = row[0]
        last_name = row[1]
        personal_id = row[2]
        date_of_birth = pd.to_datetime(row[3]).strftime('%m/%d/%Y')
        return first_name, last_name, personal_id, date_of_birth

def write_to_DB():
    """Writes information to database (Only admin can use this method).
    """
    pass

def get_info():
    """Submits the formatted output information that is requested.
    """
    pass

def import_info():
    """Writes the formatted input information that is provided by user (Admin should provide access)."""
    pass
