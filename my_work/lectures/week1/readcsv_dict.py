# read in a simple csv file as a dictionary
# author: Atacan Buyuktalas

# csv file reading

import csv

FILENAME = "data.csv"
DATADIR = "my_work/lectures/datafiles/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.DictReader(fp, delimiter=",", quoting= csv.QUOTE_NONNUMERIC)  
    total = 0
    for line in reader:
        total += int(line['id'])
        print (line) 
