# `read_json(file_path)`

Read data from a JSON file.

## Arguments
- `file_path` (str): The path to the JSON file.

## Returns
- `dict`: The JSON data as a dictionary.

## Raises
- `FileNotFoundError`: If the specified file does not exist.
- `json.JSONDecodeError`: If the JSON data is invalid.

## Usage
```python
from read_json import read_json

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

---