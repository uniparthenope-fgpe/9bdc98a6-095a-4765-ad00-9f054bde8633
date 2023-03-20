#!/bin/bash

# Set the file name and library name variables
file_name=$1
library_name="pandas"

# Use grep to search for the library import statement in the file
if grep -q "import $library_name" "$file_name"; then
    echo "The file $file_name imports the $library_name library."
    exit 0
else
    echo "The file $file_name does not import the $library_name library."
    exit 2
fi