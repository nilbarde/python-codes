# Explore a simple Bash script showcasing fundamental file operations. 
# This script can serve as a starting point for creating your own file-centric scripts.

#!/bin/bash

# Define variables
source_file="example.txt"
destination_folder="backup"

# Check if the source file exists
if [ -e "$source_file" ]; then
    echo "Source file '$source_file' found."

    # Check if the destination folder exists; if not, create it
    if [ ! -d "$destination_folder" ]; then
        mkdir "$destination_folder"
        echo "Created destination folder '$destination_folder'."
    fi

    # Copy the source file to the destination folder
    cp "$source_file" "$destination_folder/"
    echo "File copied to '$destination_folder/'."

else
    echo "Source file '$source_file' not found. Exiting..."
    exit 1
fi

# Display the contents of the destination folder
echo -e "\nContents of '$destination_folder/':"
ls "$destination_folder/"