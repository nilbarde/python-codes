import os


def get_file_size(filepath):
    """Gets the size of a file in bytes.

    Args:
        filepath: The path to the file.

    Returns:
        The size of the file in bytes.
    """
    stat = os.stat(filepath)
    return stat.st_size


if __name__ == "__main__":
    filepath = "path/to/file.txt"
    size = get_file_size(filepath)
    print(f"Size of '{filepath}': {size} bytes")
