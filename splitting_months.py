main_file = open("http_access_log.txt")

oct = open("October.log", "w")
nov = open("November.log", "w")
dec = open("December.log", "w")
jan = open("January.log", "w")
feb = open("Feburary.log", "w")
mar = open("March.log", "w")
apr = open("April.log", "w")
may = open("May.log", "w")
jun = open("June.log", "w")
jul = open("July.log", "w")
aug = open("August.log", "w")
sep = open("September.log", "w")

for line in main_file:
        if line.__contains__("Oct"): 
                oct.write(line)
        if line.__contains__("Nov"): 
                nov.write(line)
        if line.__contains__("Dec"): 
                dec.write(line)
        if line.__contains__("Jan"): 
                jan.write(line)
        if line.__contains__("Feb"): 
                feb.write(line)
        if line.__contains__("Mar"): 
                mar.write(line)
        if line.__contains__("Apr"): 
                apr.write(line)
        if line.__contains__("May"): 
                may.write(line)
        if line.__contains__("Jun"): 
                jun.write(line)
        if line.__contains__("Jul"): 
                jul.write(line)
        if line.__contains__("Aug"): 
                aug.write(line)
        if line.__contains__("Sep"): 
                sep.write(line)




    
