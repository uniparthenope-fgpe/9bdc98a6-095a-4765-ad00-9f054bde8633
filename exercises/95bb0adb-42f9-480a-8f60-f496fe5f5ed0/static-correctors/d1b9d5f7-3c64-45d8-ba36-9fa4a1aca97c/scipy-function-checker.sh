#!/bin/bash

# Set the file name and library name variables
file_name=$1
function_name=$2
library_name="scipy"

# Use grep to search for the library import statement in the file
if grep -q "import $library_name" "$file_name" && grep -q "$function_name" "$file_name"; then
    echo "Correct function"
    exit 0
else
    exit 2
fi