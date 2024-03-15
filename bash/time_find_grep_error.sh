#!/bin/bash
# source ./bash/time_find_grep_error.sh
cd bash
time find / 2>error_file.txt | grep " " | wc -l 1> results
cd ..