import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS books(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title Text,
                   author Text,
                   year INTEGER
                   )
                   ''')

books_data = [
    ("the halo","wawos king",2015),
    ("the man","energy witts",2016),
    ("monday","warap mark",2017)
]
#connection.executemany('INSERT INTO books(title,author,year)VALUES(?,?,?)',books_data)
#fetch the data
result = connection.execute('SELECT * FROM books')
data = result.fetchall()
#display the data
for row in data:
    print(f'Title:{row[1]}')
    print(f'Author:{row[2]}')      
    print(f'Year: {row[3]}')
    print('')

connection.commit()
connection.close()