import os
from datetime import datetime

from file_size import get_file_size


def get_files_in_directory(directory_path, suffix=None, recursive=False, return_full_path=False):
    """
    Retrieve files inside a directory, including sub-folders (if recursive is True).

    Args:
        directory_path (str): The path to the directory.
        suffix (str, optional): A suffix to filter the file names. Defaults to None.
        recursive (bool, optional): Whether to search for files recursively inside sub-folders. 
            If set to True then return_full_path is also set to True. Defaults to False.
        return_full_path (bool, optional): Whether to return the full file path or just the file name. Defaults to False.

    Returns:
        list: A list of file paths (or file names) matching the specified suffix (if provided) or all files in the directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

    return_full_path |= recursive
    files = []
    for root, _, filenames in os.walk(directory_path):
        for file_name in filenames:
            if suffix is None or file_name.endswith(suffix):
                if return_full_path:
                    files.append(os.path.join(root, file_name))
                else:
                    files.append(file_name)
        if not recursive:
            break

    return files


def get_last_modified_time(filepath):
    """Gets the last modified time of a file.

    Args:
        filepath: The path to the file.

    Returns:
        The last modified time of the file as a datetime object.
    """

    return datetime.fromtimestamp(os.path.getmtime(filepath))


def create_folder(folder_path):
    """
    Checks if the given folder exists or not, and if it does not exist, creates it.

    Args:
        folder_path (str): The path to the folder to check or create.

    Returns:
        bool: True if the folder exists or was created, False otherwise.
    """

    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            return True
        except:
            return False
    else:
        return True
