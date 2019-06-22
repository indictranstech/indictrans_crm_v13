#!/bin/bash
cd /home/indictrans/webapps/indictrans/frappe-bench
source ../bin/activate
if [ -z "$1" ]
then
    python -W ignore attendance.py
else
    python -W ignore attendance.py $1

fi
deactivate
