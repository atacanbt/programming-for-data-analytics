import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# checking if there is any data in the table
result = cur.execute("SELECT * FROM books;")
print(result.fetchall())

# inserting data into the table
sql = """
INSERT INTO books VALUES
    ('The Catcher in the Rye', 'J.D. Salinger', '978-0-316-76948-7'),
    ('To Kill a Mockingbird', 'Harper Lee', '0-06-112008-1'),
    ('1984', 'George Orwell', '978-0-452-28423-4');
"""
cur.execute(sql)
con.commit()

# checking if the data has been inserted
result = cur.execute("SELECT * FROM books;")
print(result.fetchall())

con.close()