#!/bin/bash 
# Run all the programs and verify that the result is correct
# Compute 

if [ ! $# -eq 2 ]; then 
    echo "Usage:  $0 path_src_problems path_res_file"
    exit 1
fi

PATH_PBS=$1
PATH_RES=$2

rm -f $PATH_RES $PATH_RES

# To stop de script with ctrl+C
STOP_FC=0

echo "Bench launched"

for folder in $(ls $PATH_PBS); do
    if [ ! -d $PATH_PBS/$folder ]; then 
        continue
    fi

    for problem in $(ls $PATH_PBS/$folder); do
        echo -n "Running problem $problem..."

        cd $PATH_PBS/$folder/$problem

        # Reset to 0 and set to 1 after frama-c command
        # to detect ctrl+c 
        STOP_FC=0 

        # Run Python version
        for prog in $(ls *.py); do
            /usr/bin/time  -f " (%U user)" -o tmp_time.txt python3 $prog > tmp_res_test.txt || break
            STOP_FC=1
            echo "Python $problem $(cat tmp_time.txt) $(cat tmp_res_test.txt)" >> $PATH_RES

            rm -f tmp_time.txt tmp_res_test.txt
        done

        if [ $STOP_FC -eq 0 ]; then
            echo -e "\nBench stopped"
            exit 1
        fi

        # Run rust version
        if [ -d rust ]; then
            cd rust
            cargo build --release -q
            /usr/bin/time  -f " (%U user)" -o tmp_time.txt ./target/release/rust > tmp_res_test.txt || break
            STOP_FC=1
            echo "Rust $problem $(cat tmp_time.txt) $(cat tmp_res_test.txt)" >> $PATH_RES

            rm -f tmp_time.txt tmp_res_test.txt
        fi
        echo -n -e "\\r\033[2K"
    done

    if [ $STOP_FC -eq 0 ]; then
        echo -e "\nBench stopped"
        exit 1
    fi
done