import socket

serverName = "localhost"
#serverName = "10.5.5.249"
#serverName = "192.168.0.101"
#serverPort = 12012
serverPort = 12001

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

message = input("Message: ")

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage)

clientSocket.close()
