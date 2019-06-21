import pandas as pd
import numpy as np
import calendar 
from datetime import datetime
import sys

#if len(sys.argv) > 1:
#    file_name = sys.argv[1]
#else:
#    _today = datetime.today()
#    weekNumber = _today.isocalendar()[1]
#    year = _today.year
#    file_name = "%s-%s-WeeklyAttendance.csv" %(weekNumber-1, year)

#filepath="sites/indictrans/private/files/%s" %(file_name)

#print filepath

import os.path
from os import path

#if path.exists(filepath):
#    print ("File exist")
#else:
#    print ("File not exist")
#    exit("Bye")


print "Continue...."

import requests

#URL = "https://hr.indictranstech.com"

#auth = URL + "/api/method/login"
#params = {'usr':'gupteshwar@indictranstech.com','pwd':'gdj@1729'}

filepath = "DailyAttendanceLogsDetails.csv"
areader = pd.read_csv(filepath, header=0, usecols=[0,1,2,10,11,15])
#areader = pd.read_csv(filepath, header=0, usecols=["Date","Employee\ Code","Employee\ Name","In\ Time","Out\ Time","Status"])
print areader.head()



#with requests.session() as s:
    # fetch the login page
    #s.get(URL, verify=False)
    
    # post to the login form
    #r = s.post(auth,data=params, verify=False)
    #print(r.text)
for index, row in areader.iterrows():
    #print row
    #datetime = datetime.strptime(row[0], '%d-%b-%y')
    #print "1:",row[0]
    #print "2:",row[1]
    #print "3:",row[2]
    #print "4:",row[3]
    #print "5:",row[4]
    #print "6:",row[5]
    datetime = datetime.strptime(row[0], '%Y-%m-%d')
    #datetime = row[0]
    #emp_code = "EMP/%s" %(str(row[1]).zfill(4))
    emp_code = row[1]
    if row[5].strip() == "Present" or  row[5].strip() == "WeeklyOff Present" or row[5].strip() == "Present On WeeklyOff":
        attdata = '{"naming_series": "ATT-","attendance_date": "%s","company": "Indictrans","status": "%s","employee": "%s", "in_time":"%s","out_time":"%s"}' %(datetime.date(), row[5].strip(),emp_code, row[3], row[4])
        print "AD:",attdata
    #else:
    #    print "Absent"
        #atturl = URL + '/api/resource/Attendance';
            #try:
                #p = s.post(url=atturl, data=attdata, verify=False)
                #print (p.text)
                #try:
                    #data = p.json()
                    #_attdata = '{"name":"%s","docstatus":1}' %(data["data"]["name"])
                    #__atturl = '/api/resource/Attendance/%s' %(data["data"]["name"])
                    #_atturl = URL + __atturl
                    #print _atturl
                    #u = s.put(url=_atturl, data=_attdata, verify=False)
                    #print (u.text)
                #except:
                    #print "Error"
            #except requests.exceptions.RequestException as e:  # This is the correct syntax
                #print e

            
                
                

    
    
