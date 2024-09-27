#sqlite3
import sqlite3
import json

conn = sqlite3.connect('myData.db')

try:
    conn.execute("""
        CREATE TABLE staff(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name CHAR(100) NOT NULL,
                rank CHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                salary REAL NOT NULL
            )
        """)
    print('Table Creation Successful!')
except sqlite3.OperationalError as e:
    print(e)

def InsertData(name, rank, age, salary):
    conn.execute(f"INSERT INTO staff (name, rank, age, salary) \
        VALUES ('{name}', '{rank}', {age}, {salary})")
    conn.commit()
    return f"Thank you for your submission"

"""
res = InsertData('micheal', 'pc', 19, 200000.00)
print(res)
"""

def retrieveData():
    all_data = []
    data = conn.execute("SELECT * FROM staff").fetchall()
    for x in data:
        all_data.append({
            'id':x[0],
            'name':x[1],
            'rank':x[2],
            'age':x[3],
            'salary':x[4]
        })
    return all_data

data = retrieveData()
print(json.dumps(data, indent=2))

def updateData(id, field, value):
    conn.execute(f"UPDATE staff SET {field} = '{value}' WHERE id = {id}")
    conn.commit()   
    return f"update successful, {conn.total_changes} changes made!"

"""
res = updateData(1, 'name', 'daniels')
print(res)

data = retrieveData()
print(json.dumps(data, indent=2))
"""

#def deleteData(id):
 #   conn.execute(f"DELETE FROM staff WHERE id = {id}")
  #  conn.commit()   
   # return f"delete successful, {conn.total_changes} changes made!"

#"""
#res = deleteData(2)
#print(res)
#"""

#def deleteTable(table):
 #   conn.execute(f"DROP TABLE '{table}'")
  #  conn.commit()
   # return f"table {table} deleted successfully"


#res = deleteTable('staff')
#print(res)


"""
create an application that stores its contents to a dabase named data.db
**** use can use class based approach to this
"""