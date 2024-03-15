#!/bin/bash
# source ./bash/cat_wc_bash_manual.sh
cd bash
man bash > bash_manual.txt
cat bash_manual.txt | wc
cd ..