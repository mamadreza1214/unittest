import sqlite3
conn = sqlite3.connect('my_database.db')
c = conn.cursor()
c.execute('''CREATE TABLE karmand(
           first text
           a null
         )''')
conn.commit
conn.close