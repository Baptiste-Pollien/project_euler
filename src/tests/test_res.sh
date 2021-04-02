#!/bin/bash 

rm -f res_diff.txt tmp_res_test.txt

echo "Running scripts"
for folder in $(ls src/problems/1-49/); do
    echo -n "Problem $folder..."
    /usr/bin/time  -f " (%U user)" -o tmp_time.txt ./run.sh $folder >> tmp_res_test.txt
    echo -n "Done"
    cat tmp_time.txt
done

diff tmp_res_test.txt res.txt > res_diff.txt

if [ $? -eq 0 ]; then
    echo "All the scripts are correct"
else
    echo "ERROR"
    cat res_diff.txt
fi

rm -f res_diff.txt tmp_res_test.txt tmp_time.txt 