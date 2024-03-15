#!/bin/bash
# source ./bash/date_echo.sh
cd bash
while true; do echo -n -e $( date | cut -d' ' -f5 ) "\r"; sleep 1; done