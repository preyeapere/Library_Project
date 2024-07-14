import sqlite3 as sql
def init_db():
    connection = sql.connect('database.db')

    with open('sqlschema.sql') as f:
       connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO book(title, author,quantity) VALUES (?, ?,?)",
            ('Gold Truck  for the lord', 'Truck wills',67)
            )
    
    cur.execute("INSERT INTO book(title, author,quantity) VALUES (?, ?,?)",
            ('Civil war', 'The Biafran war was fight with no victor no vanaquished',89)
            )
    cur.execute("INSERT INTO book (title, author,quantity) VALUES (?, ?,?)",
            ('clement Songs', 'Clement Doe',7)
            )
    cur.execute("INSERT INTO book (title, author,quantity) VALUES (?, ?,?)",
            ('Dragon of praise', 'John Wein',27)
            )
    cur.execute("INSERT INTO book (title, author,quantity) VALUES (?, ?,?)",
            ('The golden angels', 'Shakes Wein',56)
            )



        
    connection.commit()
    connection.close()
    print('Recoords posted into the database.')
        
init_db()     
        
      