import socket

HOST = socket.gethostname() 
PORT = 9500

def connectSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Establishing connection... ')
    
    while True:
    
        s, clientAddress = s.accept()
        print('Connected: ', clientAddress)
        
        data = s.recv(1024).decode()
        if (data == 'hello' or data == 'Hello'):
            response = ('Hi').encode()
            s.send(response)
        else:
            response = ('Goodbye').edncode()
            s.send(response)
            
        print('Terminating connection...')
        s.close()

connectSocket()