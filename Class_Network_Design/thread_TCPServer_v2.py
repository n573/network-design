import socket
import threading

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
    host = ''
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        raise mySocketError("Socket creation error...")


# Bind to Socket
def socket_bind():
    global host
    global port
    global s

    try:
        s.bind((host, port))
        print("The server is ready to receive")
    except socket.error as msg:
        print("Socket biding error: " + str(msg))
        raise mySocketError("Socket connection error...")


def tcp_server():
    global host
    global port
    global s

    try:
        # Listen
        s.listen(1)
        while True:
            try:
                connectionSocket, addr = s.accept()
                data = connectionSocket.recv(2048)
                print("IP: " + addr[0] + " | Port: " + str(addr[1]))
                print("Message: " + str(data.decode('utf-8')))

                connectionSocket.sendto(data.upper(), (addr[0], addr[1]))

                connectionSocket.close()

                # create working thread
                x = threading.Thread(target=client_Thread(), args=(connectionSocket, addr,))
            except socket.error as msg:
                print(str(msg))
                raise mySocketError(msg)
    except socket.error as e:
        print(str(e))
        raise mySocketError(e)

# TCP Server Protocol
def client_Thread(connectionSocket, addr):
    global s
    try:
        data = connectionSocket.recv(2048)
        print("IP: " + addr[0] + " | Port: " + str(addr[1]))
        print("Message: " + str(data.decode('utf-8')))

        connectionSocket.sendto(data.upper(), (addr[0], addr[1]))

        connectionSocket.close()
    except socket.error as e:
        print(str(e))
        raise mySocketError(e)


# Main Function
if __name__ == "__main__":
    try:
        socket_create()
        socket_bind()
        # tcp server
        tcp_server()
    except mySocketError as msg2:
        print(msg2)
