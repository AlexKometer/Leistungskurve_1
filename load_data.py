import os
import numpy as np

def load_data(file_name):
    # Determine the path of the current directory
    current_dir = os.path.dirname(__file__)
    # Build the full path to the file
    file_path = os.path.join(current_dir, file_name)

    # Use numpy.genfromtxt to read the CSV data from the file into a NumPy array
    data_array = np.genfromtxt(file_path, delimiter=',', dtype=None, names=True, encoding='utf-8')

    # Transpose the array to have each column in a separate NumPy array
    column_names = data_array.dtype.names
    column_arrays = {column: data_array[column] for column in column_names}

    return column_arrays