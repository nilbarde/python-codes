import os

from file_size import get_file_size
from directory_listing import get_files_in_directory
from file_timestamp import get_last_modified_time


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
