import socket

# Global Variables
# s = None
# host = None
# port = None


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
def remote_shell():
    global s
    try:
        # created socket
        socket_create()
        # bind socket
        socket_bind()

        # Listen
        s.listen(1)
        s, addr = s.accept()

        while True:
            try:
                
                cmd = input()
                if len(str.encode(cmd)) > 0:
                    s.send(str.encode(cmd))
                    answer = str(s.recv(4096), 'utf-8')

            except socket.error as e:
                print(e)
                raise mySocketError(e)

        s.close()

    except socket.error as e:
        print(str(e))
        raise mySocketError("Socket protocol error...")


# Main Function
if __name__ == "__main__":
    try:
        # tcp server
        remote_shell()
    except mySocketError as msg2:
        print(msg2)
