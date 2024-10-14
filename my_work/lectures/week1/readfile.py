# read in a simple file
# author: Atacan Buyuktalas

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