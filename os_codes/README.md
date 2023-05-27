# File Utility Functions

This module provides utility functions for working with files and directories.

## `get_file_size(filepath)`

Gets the size of a file in bytes.

### Arguments
- `filepath` (str): The path to the file.

### Returns
- `int`: The size of the file in bytes.

### Usage
```python
from file_size import get_file_size

filepath = "path/to/file.txt"
size = get_file_size(filepath)
print(f"Size of '{filepath}': {size} bytes")
```

---

## `get_files_in_directory(directory_path, suffix=None, recursive=False, return_full_path=False)`

Retrieve files inside a directory, including sub-folders (if `recursive` is `True`).

### Arguments
- `directory_path` (str): The path to the directory.
- `suffix` (str, optional): A suffix to filter the file names. Defaults to `None`.
- `recursive` (bool, optional): Whether to search for files recursively inside sub-folders. If set to `True`, then `return_full_path` is also set to `True`. Defaults to `False`.
- `return_full_path` (bool, optional): Whether to return the full file path or just the file name. Defaults to `False`.

### Returns
- `list`: A list of file paths (or file names) matching the specified suffix (if provided) or all files in the directory.

### Raises
- `FileNotFoundError`: If the specified directory does not exist.

### Usage
```python
from directory_listing import get_files_in_directory

directory_path = "path/to/directory"
files = get_files_in_directory(directory_path, suffix=".txt", recursive=True, return_full_path=True)
print("Files in the directory:")
for file_path in files:
    print(file_path)

```

---

## `get_last_modified_time(filepath)`

Gets the last modified time of a file.

### Arguments
- `filepath` (str): The path to the file.

### Returns
- `datetime.datetime`: The last modified time of the file as a `datetime` object.

### Usage
```python
filepath = "path/to/file.txt"
last_modified_time = get_last_modified_time(filepath)
print(f"Last modified time of '{filepath}': {last_modified_time}")
```

---

## `create_folder(folder_path)`

Checks if the given folder exists or not, and if it does not exist, creates it.

### Arguments
- `folder_path` (str): The path to the folder to check or create.

### Returns
- `bool`: `True` if the folder exists or was created, `False` otherwise.

### Usage
```python
folder_path = "path/to/new_folder"
success = create_folder(folder_path)
if success:
    print(f"Folder '{folder_path}' created or already exists.")
else:
    print(f"Failed to create folder '{folder_path}'.")
```

---
