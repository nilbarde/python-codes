# python-codes
simple python codes for small tasks for file handling 

---

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

## `write_json(data, file_path)`

Write data to a JSON file.

### Arguments
- `data` (dict): The data to be written as a dictionary.
- `file_path` (str): The path to the JSON file.

### Raises
- `TypeError`: If the data is not of type 'dict'.

---