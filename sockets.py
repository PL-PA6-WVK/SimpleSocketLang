import socket
import sys

testHost = '127.0.0.1'
testPort = 65432

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip = socket.gethostbyname('www.google.com')
# s.connect((ip, testPort))


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((testHost, testPort))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))


client()
