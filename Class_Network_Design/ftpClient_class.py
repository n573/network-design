import socket

# Global Variables
s = None
host = None
port = None


class mySocketError(Exception):
    pass


# Create Socket
def socket_create():
    global host
    global port
    global s
    host = "localhost"
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        raise mySocketError("Socket creation error...")


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


def cmd_retr():
    global s
    try:
        # created socket
        socket_create()
        # connect to socket
        socket_connect()

        # Protocol...
        # print("working... missing protocol")
        file_name = input("File Name> ")

        # send file name to server
        s.send(file_name.encode('utf-8'))
        print("File name sent, waiting for file...")

        # open new file
        f = open("new_" + file_name, "wb")

        # receive file
        recv_file = s.recv(1024)
        while recv_file:
            f.write(recv_file)
            recv_file = s.recv(1024)

        # ------------------------------------

        # close socket
        s.close()
        print("socket closed")

    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket protocol error...")

# TCP Client Protocol
def tcp_client():
    global host
    global port
    global s

    while True:
        message = input("turtle> ")

        if message == "quit":
            break
        elif message == "RETR":
            cmd_retr()
        else:
            print("Command not valid")


# Main Function
if __name__ == "__main__":

    try:
        # tcp client
        tcp_client()

    except mySocketError as msg:
        print(msg)

