#!/bin/bash

# Project directory
project_dir="/path/to/your/project"

# Create directories for source code, documentation, and data
mkdir -p "$project_dir/src" "$project_dir/docs" "$project_dir/data"

# Initialize README file in the project root
echo "# Project README" > "$project_dir/README.md"

# Copy project template files
template_dir="/path/to/templates"
cp -r "$template_dir/src_templates" "$project_dir/src/"
cp -r "$template_dir/docs_templates" "$project_dir/docs/"

# Generate data files
for i in {1..5}; do
    touch "$project_dir/data/file_$i.txt"
done

echo "Project files and directories created successfully."
