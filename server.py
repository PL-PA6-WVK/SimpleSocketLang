import socket

testHost = '127.0.0.1'
testPort = 65432
extPort = 80
ip = socket.gethostbyname('www.google.com')

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
            msg = b'Victor no hace nah'
            conn.sendall(msg)
