import socket

serverName = "localhost"
#serverName = "10.5.5.249"
#serverName = "192.168.0.101"
serverPort = 12001

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#port 12000
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

clientSocket.connect((serverName, serverPort))

message = input("Message: ")

clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(1024)

print("From Server: ", modifiedMessage)

clientSocket.close()
