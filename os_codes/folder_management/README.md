## `create_folder(folder_path)`

Checks if the given folder exists or not, and if it does not exist, creates it.

### Arguments
- `folder_path` (str): The path to the folder to check or create.

### Returns
- `bool`: `True` if the folder exists or was created, `False` otherwise.

### Usage
```python
from folder_management import create_folder

folder_path = "path/to/new_folder"
success = create_folder(folder_path)
if success:
    print(f"Folder '{folder_path}' created or already exists.")
else:
    print(f"Failed to create folder '{folder_path}'.")
```
---
