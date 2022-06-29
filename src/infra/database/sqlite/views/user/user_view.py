import sqlite3

con = sqlite3.connect('escambo.db')

# Inserir informações POST
def insert(body):
  with con:
    cur = con.cursor()
    query = "INSERT INTO user (email, password, name) VALUES (?, ?, ?)"
    cur.execute(query, (body['username'], body['password'], body['name']))
    result = cur.fetchone()
  return result

# Recupera todas as informações GET
def list():
  userList = []
  with con:
    cur = con.cursor()
    query = "SELECT * FROM 'User' ORDER BY name ASC"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      userList.append(data)
  return userList

# Recupera uma informações GET
def getOne(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' WHERE id = {id}"
    cur.execute(query)
    result = cur.fetchone()
  return result

  # Recupera uma informações GET
def getLastUser():
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' ORDER BY id DESC LIMIT 1"
    cur.execute(query)
    result = cur.fetchone()
  return result

# Recupera uma informações GET
def authenticate(body):
  result = None
  with con:
    cur = con.cursor()
    query = f"SELECT * FROM 'User' WHERE email = '{body['username']}' AND password = '{body['password']}'"
    print('query', query)
    cur.execute(query)
    result = cur.fetchone()
  return result
