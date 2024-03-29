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


if __name__ == "__main__":
    file_path = "path/to/file.json"
    try:
        json_data = read_json(file_path)
        # Process the JSON data
    except FileNotFoundError as e:
        print(e)
        # Handle file not found error
    except json.JSONDecodeError as e:
        print(e)
        # Handle invalid JSON data error
