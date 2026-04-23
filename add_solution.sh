#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./add_solution.sh <file_path> \"<commit_message>\""
    echo "Example: ./add_solution.sh problems/algoexpert/medium/cycle_in_graph.py \"Added Cycle in Graph problem\""
    exit 1
fi

FILE_PATH=$1
COMMIT_MESSAGE=$2

# Create directory structure if it doesn't already exist
mkdir -p "$(dirname "$FILE_PATH")"

# Create the file if it doesn't exist
if [ ! -f "$FILE_PATH" ]; then
    touch "$FILE_PATH"
    echo "Created file: $FILE_PATH"
else
    echo "File already exists: $FILE_PATH"
fi

# Stage and commit checking if there are actually changes to commit
git add "$FILE_PATH"

if git diff --staged --quiet; then
    echo "No changes to commit for $FILE_PATH"
else
    git commit -m "$COMMIT_MESSAGE"
    echo "Successfully committed: $COMMIT_MESSAGE"
fi
