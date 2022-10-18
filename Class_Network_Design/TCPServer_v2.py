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


# TCP Server Protocol
def tcp_server():
    global s
    try:
        # created socket
        socket_create()
        # bind socket
        socket_bind()

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

            except mySocketError as msg:
                print(msg)
                raise mySocketError(msg)

    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket protocol error...")


# Main Function
if __name__ == "__main__":
    try:
        # tcp server
        tcp_server()
    except mySocketError as msg2:
        print(msg2)
