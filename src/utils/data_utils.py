import pandas as pd

def load_csv(file_path):    
    '''
    Loads data from a CSV file into a pandas DataFrame
    '''
    return pd.read_csv(file_path)# Loads data from an Excel file
