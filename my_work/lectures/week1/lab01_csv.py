# Lab 01 - CSV file reading
# author: Atacan Buyuktalas

# csv file reading

import csv

FILENAME = "data.csv"
DATADIR = "my_work/lectures/datafiles/"

''' dealing with header
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount:
            print(f'{line}\n-------------------------')
        else: 
            print (line)
        linecount += 1

        
        #taking average of the ages 
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            pass
        else:
            total += int(line[1]) # the age is in the second column
        linecount += 1 
    print (f'average is {total/(linecount-1)}') # -1 is for the header line
'''
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting = csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += int(line['age'])
        count += 1 
    print (f'average is {total/(count)}') 