#!/bin/bash
# source ./bash/echo_alphabet_digits_set_fold_shuf.sh
cd bash
echo abcdefghklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789 | tr -d "\n" > SET1
cat SET1 | wc -c
cat SET1 | fold -w1 | shuf | tr -d "\n"
cd ..