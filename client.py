import socket

HOST = socket.gethostname() 
PORT = 9500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

request = input('Type message to server: ')

s.connect((HOST, PORT))

result = s.recv(1024).decode()
print(result)
s.close()