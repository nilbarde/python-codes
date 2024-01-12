# Python `os` Library Functions Guide

The `os` module in Python provides a way to interact with the operating system. This guide introduces and explains some of the basic and important functions available in the `os` library.

## Table of Contents

- [Current Working Directory](#current-working-directory)
- [List Files and Directories](#list-files-and-directories)
- [Create a Directory](#create-a-directory)
- [Remove/Delete a File or Directory](#remove-delete-a-file-or-directory)
- [Rename a File or Directory](#rename-a-file-or-directory)
- [Check if a Path Exists](#check-if-a-path-exists)
- [Get Information about a File](#get-information-about-a-file)
- [Joining Paths](#joining-paths)

## Current Working Directory

To get the current working directory, you can use the `os.getcwd()` function:

```python
import os

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)
```

## List Files and Directories
To list all files and directories in a given path, you can use `os.listdir()`:

```python
import os

path = '/path/to/directory'
contents = os.listdir(path)
print("Contents of", path, ":", contents)

```

## Create a Directory
To create a new directory, you can use `os.mkdir()`:

```python
import os

new_directory = '/path/to/new_directory'
os.mkdir(new_directory)
print("Directory", new_directory, "created.")
```

## Remove/Delete a File or Directory
To remove or delete a file, you can use `os.remove()`. To remove a directory, use `os.rmdir()`:

```python
import os

file_to_delete = '/path/to/file.txt'
os.remove(file_to_delete)
print("File", file_to_delete, "deleted.")

directory_to_delete = '/path/to/directory'
os.rmdir(directory_to_delete)
print("Directory", directory_to_delete, "deleted.")
```

## Rename a File or Directory
To rename a file or directory, you can use `os.rename()`:

```python
import os

old_name = '/path/to/old_name.txt'
new_name = '/path/to/new_name.txt'
os.rename(old_name, new_name)
print("File/Direcory renamed from", old_name, "to", new_name)
```

## Check if a Path Exists
To check if a path (file or directory) exists, you can use `os.path.exists()`:

```python
import os

path_to_check = '/path/to/file_or_directory'
if os.path.exists(path_to_check):
    print(path_to_check, "exists.")
else:
    print(path_to_check, "does not exist.")
```

## Get Information about a File
To get information about a file, such as size and modification time, you can use `os.stat()`:

```python
import os
import datetime

file_path = '/path/to/file.txt'
file_info = os.stat(file_path)

print("Size:", file_info.st_size, "bytes")
print("Last Modified:", datetime.datetime.fromtimestamp(file_info.st_mtime))
```

## Joining Paths
To join paths together, you can use `os.path.join()`:

```python
import os

base_path = '/path/to/base'
sub_path = 'subdirectory'
full_path = os.path.join(base_path, sub_path)

print("Full Path:", full_path)
```

