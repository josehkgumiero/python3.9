#!/bin/bash
# source ./bash/error_file_3.sh
cd bash
wc < bash_manual.txt > counts 2> error_file
cat counts 2> error_file
cd ..