import socket
import string

# Global Variables
#s = None
#host = None
#port = None
global host
global port
global s

####
# handle multiple clients simultaneously
# show connection status info in the server console
####

class mySocketError(Exception):
    pass


# Create Server-side Socket
def socket_create():
    global host
    global port
    global s
    host = ''
    port = 12500

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # stream indicates TCP connection
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

# def disconnect(connectionSocket):
#     print("Disconnecting " + connectionSocket)
#     connectionSocket.close()

# def retr_file(connectionSocket, file_name):


# def retr_file(consok, address):
def retr_file(consok):  # send to client
    # Receive filename
    file_name = consok.recv(1024)

    try:
        f = open(file_name, "rb")

        # Send file to client
        consok.send(f.read())
        consok.shutdown(socket.SHUT_WR)  # stops the read stream
        # consok.sendto(f.read(), address)

        f.close()

    except FileNotFoundError as e:
        print(str(e))

def getSentFile(consok):
    # Receive filename
    file_name = consok.recv(1024)
    file_name = bytes.decode(file_name, 'utf-8')
    try:
        f = open("serv_" + file_name, "wb")
        # f = open("serv_" + bytes.decode(file_name, 'utf-8'), "wb")

        # Receive file from client
        recv_file = consok.recv(1024)
        while recv_file:
            f.write(recv_file)
            recv_file = consok.recv(1024)

        f.close()
        # print("file " + file_name + " sent to client")

    except FileNotFoundError as e:
        print(str(e))

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

                print("awaiting command...")
                # cmdIn = connectionSocket.recv(1024).decode('utf-8')

                while True:
                    cmdIn = connectionSocket.recv(1024).decode('utf-8')
                    if cmdIn == "retr":
                        # retr_file(connectionSocket, addr)
                        retr_file(connectionSocket)
                        # file_name = connectionSocket.recv(1024)  # gets filename from client
                        print("file sent to client")
                        # retr_file(connectionSocket, file_name)  # sends file to client
                    elif cmdIn == "getF":
                        getSentFile(connectionSocket)
                        print("file received from client")
                    elif cmdIn == "close":
                        print("connection to " + addr[0] + " closing")
                        connectionSocket.close()
                        break
                    else:
                        # print("client input invalid command")
                        # connectionSocket.sendmsg("invalid command")
                        # break
                        # print("triggered else in loop")  # for debug
                        ...
            # except KeyboardInterrupt as kint:
            #     print("keyboard interrupt")
            #     pass

                # -------------------------------

                # Close connection
                connectionSocket.close()

                # can print "waiting for client" if repeated

            except socket.error as e:
                print(str(e))
                raise mySocketError("Socket protocol error...")

    except socket.error as e:
        print(str(e))
        raise mySocketError(e)
    except KeyboardInterrupt as interr:
        print("keyboard interrupt")
        raise mySocketError(interr)


# Main Function
if __name__ == "__main__":
    global s

    try:
        # created socket
        socket_create()
        # bind socket
        socket_bind()
        # tcp server
        tcp_server()

    except mySocketError as msg:
        print(msg)
    s.close()

