import os
from datetime import datetime


def get_last_modified_time(filepath):
    """Gets the last modified time of a file.

    Args:
        filepath: The path to the file.

    Returns:
        The last modified time of the file as a datetime object.
    """

    return datetime.fromtimestamp(os.path.getmtime(filepath))


if __name__ == "__main__":
    filepath = "path/to/file.txt"
    last_modified_time = get_last_modified_time(filepath)
    print(f"Last modified time of '{filepath}': {last_modified_time}")
