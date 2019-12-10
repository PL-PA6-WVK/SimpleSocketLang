import socket
import time

testHost = '127.0.0.1'
testPort = 65432


# Creates client that connects to fact server
def fact_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((testHost, testPort))
        s.sendall(b'Hello, world')
        data = s.recv(1024).decode()

    print('Fact from server: ' + data)


# Creates client side server for a live chat
def client_chat():
    print('Client Server...')
    time.sleep(1)
    # Get the hostname, IP Address from socket and set Port
    s = socket.socket()
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    # get information to connect with the server
    print(shost, '({})'.format(ip))
    server_host = input('Enter server\'s IP address:')
    name = input('Enter Client\'s name: ')
    port = 1234
    print('Trying to connect to the server: {}, ({})'.format(server_host, port))
    time.sleep(1)
    s.connect((server_host, port))
    print("Connected...\n")
    s.send(name.encode())
    server_name = s.recv(1024)
    server_name = server_name.decode()
    print('{} has joined...'.format(server_name))
    print('Enter exit() to exit.')
    while True:
        msg = s.recv(1024)
        msg = msg.decode()
        print(server_name, ">", msg)
        msg = input(str("Me > "))
        if msg == "exit()":
            msg = "Leaving the Chat room"
            s.send(msg.encode())
            print("\n")
            break
        s.send(msg.encode())


# Creates server side server for a live chat
def server_chat():

    print('Setup Server...')
    time.sleep(1)
    # Get the hostname, IP Address from socket and set Port
    soc = socket.socket()
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    port = 1234

    soc.bind((host_name, port))
    print(host_name, '({})'.format(ip))
    name = input('Enter name: ')
    soc.listen(1) # Try to locate using socket
    print('Waiting for incoming connections...')
    connection, addr = soc.accept()
    print("Received connection from ", addr[0], "(", addr[1], ")\n")
    print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
    # Get a connection from client side
    client_name = connection.recv(1024)
    client_name = client_name.decode()
    print(client_name + ' has connected.')
    print('Enter exit() to leave the chat room')
    connection.send(name.encode())
    while True:
        msg = input('Me > ')
        if msg == 'exit()':
          msg = 'Talk to you later!'
          connection.send(msg.encode())
          print("\n")
          break
        connection.send(msg.encode())
        msg = connection.recv(1024)
        msg = msg.decode()
        print(client_name, '>', msg)
