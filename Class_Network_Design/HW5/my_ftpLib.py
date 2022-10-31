# import ftplib is not allowed
import socket

class mySocketError(Exception):
    pass

def getFile(ftp, filename):
    try:
        # ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
        ...
    except Exception as e:
        print(str(e))

# Create Socket
def socket_create():
    global host
    global port
    global s

    host = "127.0.0.1"
    port = 12500

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket creation error...")


# Connect socket
def socket_connect():
    global host
    global port
    global s

    try:
        s.connect((host, port))
        print("Connected to Server -> IP: " + host + " | Port: " + str(port))

    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket connection error...")

# def connectServer():
#     global host
#     global port
#     global s
#
#     host = input("Enter host IP address (ex: 127.0.0.1): ")
#     port = input("Enter target port on " + host + ": ")
#
#     socket_create()
#     socket_connect()
#     cmd = input("command to send to server?  ")
#     s.send(cmd)


def cmd_retr():
    try:
        # Create socket and connect to server
        socket_create()
        socket_connect()

        print("Connected to Server.")

        file_name = input("File name> ")

        # Send file name
        s.send(file_name.encode('utf-8'))
        print("File name sent. Waiting for file...")

        # Open new file
        f = open("new_" + file_name, "wb")

        # Receive file
        recv_file = s.recv(1024)
        while recv_file:
            f.write(recv_file)
            recv_file = s.recv(1024)

        print("File received.")
        f.close()
        print("File saved.")

        # Close socket
        s.close()
        print("Socket closed.")
        print("**********************************")

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))

def upload():
    try:
        # Create socket and connect to server
        socket_create()
        socket_connect()

        print("Connected to Server.")

        file_name = input("File name> ")
        f = open(file_name, "rb")

        # snd_file = f.read(bytes)
        # while snd_file:
        #     # f.write(recv_file)
        #     s.send(snd_file)

        s.send(f.read())

        # s.send(file_name.encode('utf-8'))
        # print("name sent, awaiting response")

        # Open new file
        # f = open(file_name + "_download", "wb")

        # Receive file
        # recv_file = s.recv(1024)
        # while recv_file:
        #     f.write(recv_file)
        #     recv_file = s.recv(1024)

        print("File received.")
        f.close()
        print("File saved.")

        # Close socket
        s.close()
        print("Socket closed.")
        print("**********************************")

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))


def fileSendServ():
    global s

    # Receive file name
    file_name = s.recv(1024)

    try:
        # Open file
        f = open(file_name, "rb")

        # Send file to client
        s.send(f.read())
        s.shutdown(socket.SHUT_WR)

        # Close file
        f.close()
    except FileNotFoundError as e:
        print(str(e))
    except KeyboardInterrupt:
        pass