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
    except socket.error as e:
        print("Socket creation error: " + str(e))
        raise mySocketError("Socket creation error...")


# Bind to Socket
def socket_bind():
    global host
    global port
    global s

    try:
        s.bind((host, port))
        print("The server is ready to receive")
    except socket.error as e:
        print("Socket biding error: " + str(e))
        raise mySocketError("Socket creation error...")


# TCP Server Protocol
def tcp_server():
    global s

    try:

        # Listen for incoming connections
        s.listen(1)
        print("waiting for client...")

        while True:
            try:
                # Accepted connection
                connectionSocket, addr = s.accept()
                print("Client ip: " + addr[0] + " | port: " + str(addr[1]))

                # Protocol...
                # print("working... missing protocol")

                # Recieve filename
                file_name = connectionSocket.recv(1024)

                try:
                    f = open(file_name, "rb")

                    # send file to client
                    connectionSocket.send(f.read())

                    f.close()

                except FileNotFoundError as e:
                    print(str(e))

                # -------------------------------

                # Close connection
                connectionSocket.close()

                # can print "waiting for client" if repeated (threaded)

            except socket.error as e:
                print(str(e))
                raise mySocketError("Socket protocol error...")

    except socket.error as e:
        print(str(e))
        raise mySocketError(e)


# Main Function
if __name__ == "__main__":

    try:
        # created socket
        socket_create()
        # bind socket
        socket_bind()
        # tcp server
        tcp_server()

    except mySocketError as msg:
        print(msg)
