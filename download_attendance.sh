#!/bin/bash
cd attendance
rm -f *
~/gdrive download query "'1B94jfTly_TavU0BhEZGU9eNjhDn2ziOr' in parents and  createdTime > '2019-06-22T00:00:00'"
mv * WeeklyAttendance.csv
cd ..

