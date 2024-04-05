#!/bin/bash

set -e # exit on error

find . -not -path "./\.hatch/*" -type f -exec dos2unix {} \;

for file in .devcontainer/starting_scripts/*.sh; do
  bash "$file"
done

