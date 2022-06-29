import sqlite3

con = sqlite3.connect('escambo.db')

# Inserir informações POST
def insertTrade(body):
  with con:
    cur = con.cursor()
    query = "INSERT INTO 'Trade' (received_user_id, sender_user_id, want_pokemon_id, give_pokemon_id, status) VALUES (?, ?, ?, ?, ?)"
    cur.execute(query, (body['received_user_id'], body['sender_user_id'], body['want_pokemon_id'], body['give_pokemon_id'], 'pending'))

# Recupera todas as informações GET
def listTradeWithoutStatusFinished():
  tradeList = []
  with con:
    cur = con.cursor()
    query = "SELECT * FROM 'Trade' AS t INNER JOIN pokemon AS p ON p.id = t.want_pokemon_id AND p.id = t.give_pokemon_id INNER JOIN user AS u ON u.id = t.sender_user_id AND u.id = t.received_user_id WHERE status LIKE 'pending' ORDER BY id ASC"
    cur.execute(query)
    result = cur.fetchall()
    for data in result:
      tradeList.append(data)
  return tradeList

# Atualiza uma informações PUT
def tradePokemon(body):
  result = None
  with con:
    cur = con.cursor()
    query = f"UPDATE inventorypokemon SET pokemon_id = {body['want_pokemon_id']} WHERE inventory_id = {body['inventory_id']} AND pokemon_id = {body['give_pokemon_id']}"
    cur.execute(query)
  return result

# Atualiza uma informações PUT
def updateTradeStatus(id):
  result = None
  with con:
    cur = con.cursor()
    query = f"UPDATE trade SET status = 'finished' WHERE id = {id}"
    cur.execute(query)
  return result




