import socket

def test_socket_timeout(s):
    s.settimeout(1)

if __name__ == "__main__":
    serverName = ""
    serverPort = 12001

    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        clientSocket.settimeout(1)

        sentence = input('msg: ')

        clientSocket.send(sentence.encode())

        modifiedSentence = clientSocket.recv(1024)

        ##incomplete

    except socket.error as msg:
        print()

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

