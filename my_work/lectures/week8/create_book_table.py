import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

cur.execute("CREATE TABLE books (title, author, ISBN)")

result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(result.fetchall())

con.close()
