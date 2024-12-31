import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

books = {}
books['title'] = input("Enter the title of the book: ")
books['author'] = input("Enter the author of the book: ")
books['ISBN'] = input("Enter the ISBN of the book: ")

data = [books]
sql = "INSERT INTO books VALUES (:title, :author, :ISBN)"
cur.executemany(sql, data)
con.commit()

for row in cur.execute("SELECT * FROM books;"):
    print(f"row{row}")


