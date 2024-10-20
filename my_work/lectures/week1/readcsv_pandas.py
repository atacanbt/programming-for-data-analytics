# reading in the CSV as a pandas table
# author: Atacan Buyuktalas

FILENAME = "data.csv"
DATADIR = "my_work/lectures/datafiles/"

import pandas as pd
df = pd.read_csv(DATADIR + FILENAME)
print (df)
