# read in a simple file
# author: Atacan Buyuktalas

# csv file reading

import csv

FILENAME = "data.csv"
DATADIR = "/Users/atacanbuyuktalas/Desktop/Data Analytics/programming_for_data_analytics/my_work/lectures/datafiles"

with open (DATADIR + FILENAME, "rt") as fp: # open the file in read mode
    reader = csv.reader(fp, delimiter=",", quoting= csv.QUOTE_ALL)  # create a csv reader object
    for line in reader: # iterate over the lines of the file
        print (line) 

'''

FILENAME = "data.txt"
DATADIR = "../week1/"

print (DATADIR + FILENAME) # print the path of the file
with open(DATADIR + FILENAME, "r") as fp: # open the file in read mode
    total = 0 # initialize the total
    for line in fp: # iterate over the lines of the file
        total += int(line) # add the number to the total
        print (f"{line} is size {len(line)}") # print the line and its length
      #   print (line.strip()) # print the line without the newline character
    print (f'total amount of these numbers', total) # print the total

'''