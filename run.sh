#!/bin/bash

PYTHON="python3"
PATH_PB="/src/problems"
PATH_LIB="/src/lib"
PATH_RUST="/rust"
PATH_SOL="/src/bench/sol.txt"

NB=""
RUN_RUST=""

RES_BENCH=res_bench.txt

# Read Argument
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    # Diplay help manual
    -h|--help)
    echo "Usage:  $0 [options] n"
    echo "Compute the n th problem of Project Euler"
    echo ""
    echo "Options:"
    echo "-p --python         Run the python version to compute the result"
    echo "-r --rust           Run the rust version to compute the result"
    echo ""
    echo "Bench & Test"
    echo "-t --test           Launch test for the tools used to resolve the problems"
    echo "-b --bench          Run and display the results"
    echo "-d --bench-display  Display the result. If the results are not computed"
    echo "                    the bench is run."
    echo "-c --bench-clean    Remove the result of the bench"
    exit 0
    ;;

    # Run tests of the lib
    -t|--test-lib)
    DIR=$PATH_LIB
    NB=0
    shift
    ;;

    # Run python version
    -p|--python)
    RUN_RUST=""
    shift
    ;;

    # Run rust version
    -r|--rust)
    RUN_RUST="True"
    shift
    ;;

    # Launch bench
    -b|--bench)
    ./src/bench/bench.sh $(pwd)/src/problems $(pwd)/$RES_BENCH
    python3 src/bench/bench_analysis.py $(pwd)$PATH_SOL $(pwd)/$RES_BENCH
    exit 0
    ;;

    # Display bench result
    -d|--bench-display)
    if [ ! -f $RES_BENCH ]; then
        ./src/bench/bench.sh $(pwd)/src/problems $(pwd)/$RES_BENCH
    fi
    python3 src/bench/bench_analysis.py $(pwd)$PATH_SOL $(pwd)/$RES_BENCH
    exit 0
    ;;

    # Remove bench result
    -c|--bench-clean)
    rm -f $(pwd)/$RES_BENCH
    echo "Bench result cleaned"
    exit 0
    ;;

    # Number of the problem to run
    *)    # unknown option
    # Verify that the parameter is a number
    [ -n "$1" ] && [ "$1" -eq "$1" ] 2>/dev/null
    if [ $? -ne 0 ]; then
        echo $1 is not number
        echo "Usage:  $0 n"
        echo "  use $0 --help for more information"
        exit 1
    fi
    NB=$1
    shift # past argument
    ;;
esac
done

if [ -z "$NB" ]; then
    echo "No problem specified"
    echo "  Use $0 --help for more information"
    exit 1
fi

# Find the correct directory
if [ $NB -eq 0 ]; then 
    echo "Launch tests..."
    DIR=$PATH_LIB
elif [ $NB -ge 1 ] && [ $NB -lt 10 ]; then
    DIR="${PATH_PB}/1-49/0$NB"
    if [ ! -d "$(pwd)${DIR}" ]; then 
        DIR="${PATH_PB}/1-49/$NB"
    fi
elif [ $NB -ge 10 ] && [ $NB -lt 50 ]; then
    DIR="${PATH_PB}/1-49/$NB"
elif [ $NB -ge 50 ] && [ $NB -lt 100 ]; then
    DIR="${PATH_PB}/50-99/$NB"
else
    echo "The problem $NB is not resolved yet..."
    exit 1
fi

PATH_EXE=$(pwd)${DIR}

# Test if the folder exist
if [ $NB -eq 0 ]; then
    # Run the tests
    cd $PATH_EXE
    for SCRIPT in $(ls *.py); do
        $PYTHON $SCRIPT
    done

    echo "Done."
elif [ ! -z "$RUN_RUST" ]; then
    PATH_EXE=$PATH_EXE$PATH_RUST
    if [ -d $PATH_EXE ]; then 
        cd $PATH_EXE
        cargo build --release
        ./target/release/rust
    else
        echo "The problem $NB is not resolved yet in rust..."
        exit 1
    fi
else
    if [ -d $PATH_EXE ]; then 
        cd $PATH_EXE
        for SCRIPT in $(ls *.py); do
            $PYTHON $SCRIPT
        done
    else
        echo "The problem $NB is not resolved yet in python..."
        exit 1
    fi
fi