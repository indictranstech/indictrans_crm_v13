import pandas as pd
import numpy as np
#import calendar 
from datetime import datetime
import sys

filepath = "attendance/WeeklyAttendance.csv"
areader = pd.read_csv(filepath, header=0, usecols=[0,1,2,10,11,15])
print areader.head()

print "Continue...."

import requests

URL = "https://office.indictranstech.com"
auth = URL + "/api/method/login"
params = {'usr':'contact@indictranstech.com','pwd':'2XBKPDbHup2vbYdB'}

with requests.session() as s:
    # fetch the login page
    s.get(URL, verify=False)
    
    # post to the login form
    r = s.post(auth,data=params, verify=False)
    print(r.text)
    for index, row in areader.iterrows():
        datetime = datetime.strptime(row[0], '%d-%m-%Y')
        emp_code = row[1]
        empurl = ""
        empurl = URL + '/api/resource/Employee?filters='
        empdata = '[["Employee","attendance_card_id","=","%s"]]' %(emp_code)
        empurl = empurl + empdata
        p = s.get(url=empurl, verify=False)
        emp_data = p.json()
        print emp_data
        print emp_data["data"][0]["name"]
        if row[5].strip() == "Present" or  row[5].strip() == "WeeklyOff Present" or row[5].strip() == "Present On WeeklyOff":
            attdata = '{"naming_series": "ATT-","attendance_date": "%s","company": "New Indictrans Technologies Pvt. Ltd.","status": "%s","employee": "%s", "in_time":"%s","out_time":"%s"}' %(datetime.date(), row[5].strip(),emp_data["data"][0]["name"], row[3], row[4])
            print "AD:",attdata
            atturl = URL + '/api/resource/Attendance';
            try:
                p = s.post(url=atturl, data=attdata, verify=False)
                print (p.text)
                try:
                    data = p.json()
                    _attdata = '{"name":"%s","docstatus":1}' %(data["data"]["name"])
                    __atturl = '/api/resource/Attendance/%s' %(data["data"]["name"])
                    _atturl = URL + __atturl
                    print _atturl
                    u = s.put(url=_atturl, data=_attdata, verify=False)
                    print (u.text)
                except:
                    print "Error"
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print e


    
