#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import datetime
import calendar

main_file = open("http_access_log.txt")
question_2 = open("requests_per_week.csv","w")

pattern = re.compile("\d{2}/\D{3}/\d{4}")

result={
"per_week_data":{},
}
main_file = open("http_access_log.txt")
date_day = None
days = 0
week = None


for line in main_file:
   if(len(line)>=56):
     data=line.split()
     date = data[3][1::].split(':')
     if not (date_day == date[0]):
        date_day = date[0]
        days += 1
        if(days%7 == 0):
           week = date_day
  
           
if week in result["per_week_data"]:
              result["per_week_data"][week]+=1
else:
        result["per_week_data"][week] = 0
        print(result)
 


