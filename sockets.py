import socket
import sys
import time

testHost = '127.0.0.1'
testPort = 65432

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip = socket.gethostbyname('www.google.com')
# s.connect((ip, testPort))


def fact_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((testHost, testPort))
        s.sendall(b'Hello, world')
        data = s.recv(1024).decode()

    print('Fact from server: ' + data)


def client_chat():
    print('Client Server...')
    time.sleep(1)
    # Get the hostname, IP Address from socket and set Port
    soc = socket.socket()
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    # get information to connect with the server
    print(shost, '({})'.format(ip))
    server_host = input('Enter server\'s IP address:')
    name = input('Enter Client\'s name: ')
    port = 1234
    print('Trying to connect to the server: {}, ({})'.format(server_host, port))
    time.sleep(1)
    soc.connect((server_host, port))
    print("Connected...\n")
    soc.send(name.encode())
    server_name = soc.recv(1024)
    server_name = server_name.decode()
    print('{} has joined...'.format(server_name))
    print('Enter [bye] to exit.')
    while True:
        message = soc.recv(1024)
        message = message.decode()
        print(server_name, ">", message)
        message = input(str("Me > "))
        if message == "[bye]":
            message = "Leaving the Chat room"
            soc.send(message.encode())
            print("\n")
            break
        soc.send(message.encode())


def server_chat():

    print('Setup Server...')
    time.sleep(1)
    #Get the hostname, IP Address from socket and set Port
    soc = socket.socket()
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    port = 1234
    soc.bind((host_name, port))
    print(host_name, '({})'.format(ip))
    name = input('Enter name: ')
    soc.listen(1) #Try to locate using socket
    print('Waiting for incoming connections...')
    connection, addr = soc.accept()
    print("Received connection from ", addr[0], "(", addr[1], ")\n")
    print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
    #get a connection from client side
    client_name = connection.recv(1024)
    client_name = client_name.decode()
    print(client_name + ' has connected.')
    print('Press [bye] to leave the chat room')
    connection.send(name.encode())
    while True:
       message = input('Me > ')
       if message == '[bye]':
          message = 'Good Night...'
          connection.send(message.encode())
          print("\n")
          break
       connection.send(message.encode())
       message = connection.recv(1024)
       message = message.decode()
       print(client_name, '>', message)
