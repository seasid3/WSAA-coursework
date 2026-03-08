# this program reads in data and outputs each line as a list

import csv

FILENAME = "data.csv"
DATADIR = ""

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quotin=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: #first row ie header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # add the age to the total
        linecount += 1
    print(f"average is {total/(linecount-1)}") #why -1? because we don't want to include the header row in the average calculation