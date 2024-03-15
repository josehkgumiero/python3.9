#!/bin/bash
# source ./bash/for_seq_echo.sh
cd bash
for i in $( seq 1 13 ) ; do echo $(( i * 17 )); done
cd ..