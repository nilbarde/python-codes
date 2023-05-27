# JSON File Operations

This module provides functions for reading and writing data from/to JSON files.

## `read_json(file_path)`

Read data from a JSON file.

### Arguments
- `file_path` (str): The path to the JSON file.

### Returns
- `dict`: The JSON data as a dictionary.

### Raises
- `FileNotFoundError`: If the specified file does not exist.
- `json.JSONDecodeError`: If the JSON data is invalid.

### Usage
```python
from json_reader import read_json

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
```
- Handling error will help code from crashing (Optional)

## `write_json(data, file_path)`

Write data to a JSON file.

### Arguments
- `data` (dict): The data to be written as a dictionary.
- `file_path` (str): The path to the JSON file.

### Raises
- `TypeError`: If the data is not of type 'dict'.

### Usage
```python
from json_writer import write_json

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
```
---