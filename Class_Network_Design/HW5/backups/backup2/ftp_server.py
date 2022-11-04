import socket


class mySocketError(Exception):
    pass


# Create Socket
def socket_create():
    global host
    global port
    global s

    host = ''
    port = 12500

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket creation error...")


# Bind socket
def socket_bind():
    global host
    global port
    global s

    try:
        s.bind((host, port))
    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket binding error...")


# def retr_file(file_name):  # send file to client
def retr_file():  # send file to client (client download)
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

def get_sent(): # helper func to recieve upload
    filename = s.recv(1024)  # receives name sent by client
    file_in = s.recv(4096)  # receives the file itself
    f = open(filename, 'wb')
    while file_in:
        f.write(file_in)
        file_in = s.recv(1024)

# TCP Server
def tcp_server():
    global host
    global port
    global s

    socket_create()
    socket_bind()
    # Listen for incoming connections
    s.listen(1)
    print("**********************************")
    print("Waiting for client...")

    while True:
        try:
            connectionSocket, addr = s.accept()
            print("Connected to Client -> IP: " + addr[0] + " | Port: " + str(addr[1]))

            # determine cmd
            # cmd = input("input command> ")

            print("waiting for command from " + addr[0])
            cmd = s.recv(1024)


            # if (cmd == 'retr'):
            #     retr_file()
            # elif cmd == 'exit':
            #     exit('user said to exit')
            # else:
            #     print("please enter a valid command.")

            # # Receive file name
            # file_name = connectionSocket.recv(1024)
            #
            # try:
            #     # Open file
            #     f = open(file_name, "rb")
            #
            #     # Send file to client
            #     connectionSocket.send(f.read())
            #     connectionSocket.shutdown(socket.SHUT_WR)
            #
            #     # Close file
            #     f.close()
            # except FileNotFoundError as e:
            #     print(str(e))

            # Close connection
            print("Socket closed.")
            connectionSocket.close()

            print("**********************************")
            print("Waiting for client...")
            
        except socket.error as e:
            print(str(e))
            break

#**************************************
if __name__ == "__main__":
    global s

    try:
        socket_create()
        socket_bind()
        tcp_server()
    except mySocketError as msg:
        print(msg)

    # Close main server socket
    s.close()
    print("Server offline.")
