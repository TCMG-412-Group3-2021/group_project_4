import re

main_file = open ("http_access_log.txt")

regex = re.compile("\[(\d{2})/([A-Za-z]{3,4})/(\d{4}):(\d{2}:\d{2}:\d{2}).+\] \"([A-Z]{3,6}) (.+) HTTP/1.0\" (\d{3}) .*")

statusCode3xx = 0
statusCode4xx = 0
totalNumberOfRequests = 0

for line in main_file:
    statusCode = regex.findall(line)
    if statusCode:
        if 300 <= int(statusCode[0][6]) < 400:
            statusCode3xx += 1
            totalNumberOfRequests += 1
        elif int(statusCode[0][6]) >= 400: 
            statusCode4xx += 1
            totalNumberOfRequests += 1
    else:
        print('No match found')
        totalNumberOfRequests += 1

question_3_and_4 = open("not_successful_and_redirected_requests.csv", "w")

question_3_and_4.write("Percentage of Requests Not Successful,Percentage of Requests That Redirected\n")

question_3_and_4.write("%.2f,%.2f" % (statusCode4xx/totalNumberOfRequests, statusCode3xx/totalNumberOfRequests))