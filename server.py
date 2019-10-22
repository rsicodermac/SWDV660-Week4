import socket

HOST = '127.0.0.1' 
PORT = 9500

def connectSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Establishing connection... ')
    
    while True:
    
        x, clientAddress = s.accept()
        print('Connected: ', clientAddress)
        
        data = x.recv(1024).decode()
        if (data == 'hello' or data == 'Hello'):
            response = ('Hi').encode()
            x.send(response)
            break
        else:
            response = ('Goodbye').encode()
            x.send(response)
            break
    print('Terminating connection...')
    x.close()

connectSocket()