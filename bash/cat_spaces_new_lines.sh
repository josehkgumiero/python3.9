#!/bin/bash
# source ./bash/cat_spaces_new_lines.sh
cd bash
echo -e "\n"
cat spaces_new_lines.txt
echo -e "\n"
cat spaces_new_lines.txt | tr -d " "
echo -e "\n"
cd ..