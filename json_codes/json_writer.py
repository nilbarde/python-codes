import json


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


if __name__ == "__main__":
    data = {"key1": "value1", "key2": "value2"}
    file_path = "path/to/file.json"
    try:
        write_json(data, file_path)
        # JSON data successfully written to the file
    except FileNotFoundError as e:
        print(e)
        # Handle file not found error
    except TypeError as e:
        print(e)
        # Handle invalid data type error (data is not a dictionary)
