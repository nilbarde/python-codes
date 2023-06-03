# `get_last_modified_time(filepath)`

Gets the last modified time of a file.

## Arguments
- `filepath` (str): The path to the file.

## Returns
- `datetime.datetime`: The last modified time of the file as a `datetime` object.

## Usage
```python
from file_timestamp import get_last_modified_time

filepath = "path/to/file.txt"
last_modified_time = get_last_modified_time(filepath)
print(f"Last modified time of '{filepath}': {last_modified_time}")
```
---
