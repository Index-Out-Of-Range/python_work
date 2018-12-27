import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
while True:
    timestamp = time.time()
    s.send(str(timestamp).encode())
    print(s.recv(1024).decode())
    time.sleep(10)
s.close()

