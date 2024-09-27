import sqlite3

connection = sqlite3.connect('mydata.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS employee(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name Text,
                   title Text,
                   age INTEGER,
                   address Text
                   )
                   ''')
emp_data = [
    ("Wawos","Software Eng", 22, "Mbale"),
    ("Deno","Mechinacial Eng", 23, "kampala"),
    ("Elon Musk","Software Developer", 25, "Jinja"),
    ("Json","Sales", 22, "Mbale"),
    ("Mason","Software Eng", 26, "Kira"),
    ("Online","Tech Eng", 23, "Aura"),
    ("Phos","Sales", 22, "Lira"),
    ("Mask","Tech Eng", 22, "Mbale"),
    ("Alex","Software developer", 24, "Aura"),

]
#insert the data
#connection.executemany('INSERT INTO employee (name, title, age, address)VALUES (?,?,?,?)', emp_data)
results = connection.execute('SELECT * FROM employee ORDER BY age ASC')
data = results.fetchall()
# display the data
for row in data:
    print(f'Name:{row[1]}')
    print(f'Title:{row[2]}')
    print(f'Age: {row[3]}')
    print(f'Address: {row[4]}')
    print('')

connection.commit()