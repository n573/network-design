import socket

serverPort = 12001

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort))

# incoming connections (1) = 1 client at a time
serverSocket.listen(1)

while 1:
    connectionSocket, addr = serverSocket.accept()
    
    message = connectionSocket.recv(1024)
    modifiedMessage = message.upper()
    
    connectionSocket.send(modifiedMessage)
    connectionSocket.close()
    
