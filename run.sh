#!/bin/bash

PYTHON="python3"
PATH_PB="/src/problems"
PATH_LIB="/src/lib"

if [ ! $# -eq 1 ]; then 
    echo "Usage:  $0 n"
    echo "Compute the n th problem of Project Euler"
    echo "For n = 0, tests of the lib are launch"
    exit 1
fi

# Verify that the parameter is a number
[ -n "$1" ] && [ "$1" -eq "$1" ] 2>/dev/null
if [ $? -ne 0 ]; then
   echo $1 is not number
   exit 1
fi

# Find the correct directory
if [ $1 -eq 0 ]; then 
    echo "Launch tests..."
    DIR=$PATH_LIB
elif [ $1 -ge 1 ] && [ $1 -lt 50 ]; then
    DIR="${PATH_PB}/1-49/$1"
elif [ $1 -ge 50 ] && [ $1 -lt 100 ]; then
    DIR="${PATH_PB}/50-99/$1"
else
    echo "The problem $1 is not resolved yet..."
    exit 1
fi

PATH_EXE=$(pwd)${DIR}

# Test if the folder exist
if [ -d $PATH_EXE ]; then 
    cd $PATH_EXE
    for SCRIPT in $(ls *.py); do
        $PYTHON $SCRIPT
    done
else
    echo "The problem $1 is not resolved yet..."
    exit 1
fi

if [ $1 -eq 0 ]; then 
    echo "Done."
fi