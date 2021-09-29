import re
from collections import Counter 
import csv

def reader(filename):
    with open(filename) as f:
        http_access_log = f.read()

        month1 = re.findall("Oct/1994", http_access_log)
        month2 = re.findall("Nov/1994", http_access_log)
        month3 = re.findall("Dec/1994", http_access_log)
        month4 = re.findall("Jan/1995", http_access_log)
        month5 = re.findall("Feb/1995", http_access_log)
        month6 = re.findall("Mar/1995", http_access_log)
        month7 = re.findall("Apr/1995", http_access_log)
        month8 = re.findall("May/1995", http_access_log)
        month9 = re.findall("Jun/1995", http_access_log)
        month10 = re.findall("Jul/1995", http_access_log)
        month11 = re.findall("Aug/1995", http_access_log)
        month12 = re.findall("Sep/1995", http_access_log)
        month0 = re.finall("Oct/1995", http_access_log)
        requests_per_month = month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12, month0
        print(requests_per_month)

def count(requests_per_month):
    print(Counter(requests_per_month))

def write_csv(counter):
    with open("requests_per_month.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["Month", "Requests"]

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]) )
