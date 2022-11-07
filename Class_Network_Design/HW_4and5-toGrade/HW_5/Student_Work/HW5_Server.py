import socket
import os
import sys
import threading

class mySocketError(Exception):
    pass

def socket_create(): #create socket
    global host
    global port
    global s
    host = ''
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        raise mySocketError("Socket creation error...")

def socket_bind(): #bind socket
    global host
    global port
    global s

    try:
        s.bind((host, port))
        print("Server is ready to recieve")
    except socket.error as msg:
        print("Socket bind error: " + str(msg))
        raise mySocketError("Socket bind error...")

def TCP_server():
    global s

    try:
        socket_create()
        socket_bind()

        s.listen(1)
        print()
        print("Waiting for clients to connect")

        while True:
            try:
                connectionSocket, addr = s.accept()
                # create Working Thread
                x = threading.Thread(target=client_Thread, args=(connectionSocket, addr,))
                x.setDaemon(True)
                x.start()

            except socket.error as e:
                print(str(e))
                raise mySocketError(e)
    except socket.error as e:
        print(str(e))
        raise mySocketError("Socket protocol error...")

def client_Thread(connectionSocket, addr):

    logon(connectionSocket, addr)
    print("Server is connected to IP: " + addr[0] + " | Port: " + str(addr[1]))

    while True:
        try:
            connectionSocket.send("turtle>".encode())
            instruct = connectionSocket.recv(2048).decode()
            if instruct == "help":
                help_func(connectionSocket)
            elif instruct == "upload":
                upload(connectionSocket)
            elif instruct == "download":
                download(connectionSocket)
            elif instruct == "ls":
                ls(connectionSocket)
            elif instruct == "quit":
                print("Client is disconnecting")
                connectionSocket.close()
                print("Connection socket closed\n")
                return
            else:
                message = "Invalid request try 'help'\n"
                connectionSocket.send(message.encode())
        except socket.error as e:
            print(str(e))
            raise mySocketError("Socket protocol error...")
    connectionSocket.close()
    print("Connection socket closed\n")


def logon(connectionSocket, addr):
    print("Client at IP: " + addr[0] + " | Port: " + str(addr[1]) + " is logging in")

    success = False
    while(not success):
        message = "Username: "
        connectionSocket.send(message.encode())
        userName = connectionSocket.recv(2048).decode()

        message = "Password: "
        connectionSocket.send(message.encode())
        password = connectionSocket.recv(2048).decode()

        if( (userName== "IanMattox" and password == "1111") or (userName == "admin" and password=="admin")):
            print("Login Successful")

            success = True
        else:
            message = "Try again\n"
            connectionSocket.send(message.encode())


def help_func(connectionSocket):
    message = "help: Show available commands \ndownload: Download file from server \n" \
                            "upload: Upload files to server \nls: List files on server \n" \
                            "quit: Closes the connection\n\n"
    connectionSocket.send(message.encode())

def ls(connectionSocket):
    pth = os.getcwd()
    filesNames = ""
    # list all files in current directory
    with os.scandir(pth) as entries:
        for entry in entries:
            if entry.is_file():
                filesNames = filesNames + entry.name + "\n"
    connectionSocket.send(filesNames.encode())

def upload(connectionSocket):
    print("Client wants to upload a file")
    message = "Input file name: \n"
    connectionSocket.send(message.encode())
    fileName = connectionSocket.recv(2048)
    fileName = fileName.decode('utf-8')

    # Open new file
    f = open("client_" + fileName, "wb")
    # Receive file
    recv_file = connectionSocket.recv(1024)
    f.write(recv_file)

    while (sys.getsizeof(recv_file) == 1057):
        f.write(recv_file)
        recv_file = connectionSocket.recv(1024)

    print("File received.")
    f.close()
    print("File saved.")

    message = "File Saved"
    connectionSocket.send(message.encode())

def download(connectionSocket):
    print("Client wants to download a file")
    file_name = connectionSocket.recv(2048)

    try:
        f = open(file_name, "rb")
        connectionSocket.send(f.read())
        print(file_name.decode(), "was sent to the client \n")
        f.close()
        message = connectionSocket.recv(2048)
        print(message.decode())

    except FileNotFoundError as e:
        print(str(e))

if __name__ == "__main__":

    try:
        TCP_server()
    except mySocketError as e:
        print(e)