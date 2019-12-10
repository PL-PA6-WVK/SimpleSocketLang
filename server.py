import socket
import random as rand
extPort = 80
ip = socket.gethostbyname('www.google.com')


def local_server():

    testHost = '127.0.0.1'
    testPort = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((testHost, testPort))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                msg = rand_msg()
                conn.sendall(msg)


def rand_msg():
    msg = [b'The first computer programmer was a woman', b'The first computer bug was named after a real bug',
           b'The first digital computer game never made any money']

    return msg[rand.randrange(2)]


local_server()