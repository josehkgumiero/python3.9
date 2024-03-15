#!/bin/bash
# source ./bash/error_file_2.sh
cd bash
wc bash_manual.txt > counts 2> error_file
counts 2> error_file
cd ..