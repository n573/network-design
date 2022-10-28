import socket


class mySocketError(Exception):
    pass


# Create Socket
def socket_create():
    global host
    global port
    global s

    host = "localhost"
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

def connectServer():
    global host
    global port
    global s

    socket_create()
    socket_connect()

    host = input("Enter host IP address (ex: 127.0.0.1): ")
    port = input("Enter target port on " + host + ": ")

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

    # TCP Client

def shell():
    while True:

        msg = input('turtle> ')
        if msg == 'quit':
            break

        elif msg == 'RETR':
            cmd_retr()

        elif msg == 'connect':
            connectServer()

        else:
            print("Command not valid.")

def tcp_Client():
    global host
    global port
    global s

    shell()
    # while True:
    #
    #     msg = input('turtle> ')
    #     if msg == 'quit':
    #         break
    #
    #     elif msg == 'RETR':
    #         cmd_retr()
    #
    #     elif msg == 'connect':
    #         connectServer()
    #
    #     else:
    #         print("Command not valid.")


# **************************************
if __name__ == "__main__":
    tcp_Client()

