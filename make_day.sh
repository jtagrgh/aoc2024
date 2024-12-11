#!/bin/bash

if [ -d "$1" ]; then
    echo "Directory $1 already exists."
    exit 1
fi
mkdir $1
cd $1
touch part1.py
touch part2.py
touch input.txt
touch sample_input.txt