import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')


def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        try:
            data = sock.recv(1024)
            print(data.decode())
            time.sleep(1)
            # sock.send(str(time.ctime(float(data))).encode('utf-8'))
            sock.send(str(time.strftime("%Y %m %d %H:%M:%S", time.localtime(
                float(data)))).encode('utf-8'))
        except Exception as e:
            print(e)
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
