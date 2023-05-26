import json

def read_json(file_path):
    """
    Read data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The JSON data as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the JSON data is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error decoding JSON in '{file_path}': {e.msg}", e.doc, e.pos)

def write_json(data, file_path):
    """
    Write data to a JSON file.

    Args:
        data (dict): The data to be written as a dictionary.
        file_path (str): The path to the JSON file.

    Raises:
        TypeError: If the data is not of type 'dict'.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, sort_keys=True, indent=4)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
