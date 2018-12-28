import socket, threading
from time import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 19999))
s.listen(5)
print('Waiting for connection...')


def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        try:
            recv_msg = sock.recv(1024).decode()
            print(recv_msg)
            # if sock.recv(1024).decode() == "exit":
            #     break
        finally:
            print("Server: " + str(ctime(time())) + " ", end="")
            message = "Server: " + str(ctime(time())) + " "+ input()
            sock.send(message.encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
