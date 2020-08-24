import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "admin", "pass")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

select_query = "SELECT * FROM users"
for value in cursor.execute(select_query):
    print(value)

connection.commit()
connection.close()