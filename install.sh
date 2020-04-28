#!/bin/sh

MAIN="${PWD}/main.py"

pip3 install -r requirements.txt
crontab -l > temp
echo "*/5 * * * *  $MAIN" >> temp
crontab temp
rm temp