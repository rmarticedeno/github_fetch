#!bin/sh

MAIN = '${PWD}/main.py'

pip3 install -r requirements.txt
echo "*/5 * * * *  $MAIN" | crontab
