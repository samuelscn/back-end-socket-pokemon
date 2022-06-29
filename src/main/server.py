import socket
import json
from src.main.adapters.socket_adapters import SocketAdapters
import requests

HOST = 'localhost'
PORT = 8221
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
socketAdapters = SocketAdapters()

# makeTeste =  { "route": 'user/create', "params": { "username": 'teste6@teste.com', "password": '123teste', "name": 'teste' } }
# makeTeste =  { "route": 'user/authenticate', "body": { "email": 'testee@teste.com', "password": '123teste' } }
# makeTeste =  { "route": 'user/inventory', "params": { "id": 6 } }
# print('makeTeste', makeTeste)
# result = socketAdapters.execute(makeTeste)
# print('resultServer', result)
while True:
  con, cliente = tcp.accept()
  print('Conectado por', cliente)
  while True:
    msg = con.recv(1024)
    if not msg: break
    socketRequest = json.loads(msg)
    print(cliente, socketRequest)
    result = socketAdapters.execute(socketRequest)
    print('resultServer', result)
    data = json.dumps(result)
    con.sendall(bytes(data, encoding="utf-8"))
  print('Finalizando conexao do cliente', cliente)
  con.close()
