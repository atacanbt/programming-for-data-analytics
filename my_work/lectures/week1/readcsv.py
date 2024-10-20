# read in a simple csv file
# author: Atacan Buyuktalas

# csv file reading

import csv

FILENAME = "data.csv"
DATADIR = "my_work/lectures/datafiles/"

with open (DATADIR + FILENAME, "rt") as fp: # open the file in read mode
    reader = csv.reader(fp, delimiter=",", quoting= csv.QUOTE_ALL)  # create a csv reader object
    total = 0 # initialize the total    
    linecount = 0 # initialize the line count
    for line in reader: # iterate over the lines of the file
        if not linecount: # if this is the first line , if there is a header line use this logic!!!
            print(f"{line}\n------------------------") # print the header
        else: # if this is not the first line / all subsequent rows
            total += int(line[0]) # add the number to the total
            print (line) # print the line
        linecount += 1 # increment the line count
