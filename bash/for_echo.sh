#!/bin/bash
# source ./bash/for_echo.sh
cd bash
for i in 1 2 3 ; do echo $(( i * 17 )); done
cd ..