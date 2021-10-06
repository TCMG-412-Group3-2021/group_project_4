import re
import datetime
import calendar

def month_string_to_int(argument):
    switcher = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    return switcher.get(argument, "nothing")

def day_int_to_string(argument):
    switcher = {
        0: "Monday", 1: "Tuesday",  2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday",
    }
    return switcher.get(argument, "nothing")

main_file = open ("http_access_log.txt")
question_1 = open("requests_per_day.csv", "w")

datePattern = re.compile("\d{2}/\D{3}/\d{4}")

#array of number of requests on each day
#   days_of_the_week[0] = monday
#   days_of_the_week[1] = tuesday
#   and so on
days_of_the_week = [0] * 7

for line in main_file:
    dateString = datePattern.findall(line)
    if dateString:
        dateStringSplit = dateString[0].split('/')
        day = dateStringSplit[0]
        month = month_string_to_int(dateStringSplit[1])
        year = dateStringSplit[2]

        dayOfWeek = datetime.datetime(int(year), int(month), int(day)).weekday()
        days_of_the_week[dayOfWeek] += 1
    else:
        print('No match found')

question_1.write("Day Of The Week,Number of Requests\n")
for i in range(7):
    question_1.write("%s,%d\n" % (day_int_to_string(i), days_of_the_week[i]))

question_1.close()


