import socket
import json
from src.main.adapters.socket_adapters import SocketAdapters

HOST = 'localhost'
PORT = 5051
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
socketAdapters = SocketAdapters()
# makeTeste =  { "route": 'user/create', "body": { "email": 'teste@teste.com', "password": '123teste', "name": 'teste' } }
makeTeste =  { "route": 'user/authenticate', "body": { "email": 'testee@teste.com', "password": '123teste' } }
print('makeTeste', makeTeste)
result = socketAdapters.execute(makeTeste)
print('resultServer', result)
while True:
  con, cliente = tcp.accept()
  print('Conectado por', cliente)
  while True:
    msg = con.recv(1024)
    if not msg: break
    socketRequest = json.loads(msg)
    print(cliente, socketRequest)
  print('Finalizando conexao do cliente', cliente)
  con.close()
