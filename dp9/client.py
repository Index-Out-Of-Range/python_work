import socket
from time import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 19999))
while True:
    print("Client: " + str(ctime(time())) + " ", end="")
    message = "Client: " + str(ctime(time())) + " " + input()
    s.send(message.encode())
    print(s.recv(1024).decode())
s.close()

