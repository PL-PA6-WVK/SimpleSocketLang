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
        data = s.recv(1024).decode()

    print('Received from server: ' + data)

def client_start():
    host_IP = input("Enter server IP address: ")
    port = int(input("Enter port to use (server and client must select same port): "))
    socket_for_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # address = ("192.168.0.7", 10000)
    address = (host_IP, port)
    socket_for_client.connect(address)
    while True:
        message = input("Message: ")
        socket_for_client.sendall(message.encode())
        if message == "exit()":
            break