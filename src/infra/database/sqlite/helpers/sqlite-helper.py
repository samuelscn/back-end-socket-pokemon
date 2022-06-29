import sqlite3

con = sqlite3.connect('escambo.db')

with con:
  cur = con.cursor()
  cur.execute("CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT, name TEXT)")
  cur.execute("CREATE TABLE inventory (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES user(id))")
  cur.execute("CREATE TABLE pokemon (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
  cur.execute("CREATE TABLE trade (id INTEGER PRIMARY KEY AUTOINCREMENT, received_id INTEGER, sender_id INTEGER, received_pokemon_id INTEGER, sender_pokemon_id INTEGER)")
  cur.execute("CREATE TABLE inventorypokemon (id INTEGER PRIMARY KEY AUTOINCREMENT, inventory_id INTEGER, pokemon_id INTEGER, FOREIGN KEY(inventory_id) REFERENCES inventory(id), FOREIGN KEY(pokemon_id) REFERENCES pokemon(id))")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()