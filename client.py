import socket

HOST = '127.0.0.1' 
PORT = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    request = input('Type message to server: ').encode()
    s.send(request)
    result = s.recv(1024).decode()
    print(result)
    s.close()