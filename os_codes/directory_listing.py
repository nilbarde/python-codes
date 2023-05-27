import os


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


if __name__ == "__main__":
    directory_path = "path/to/directory"
    files = get_files_in_directory(directory_path, suffix=".txt", recursive=True, return_full_path=True)
    print("Files in the directory:")
    for file_path in files:
        print(file_path)

