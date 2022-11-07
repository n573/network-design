import socket
import os
import sys

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


# TCP Client Protocol
def tcp_client():
    global host
    global port
    global s

    while True:
        try:
            socket_create()
            socket_connect()

            #Continuously get keyboard input from client
            while True:
                message = (s.recv(2048)).decode()
                message = input(message)
                s.sendto(message.encode('utf-8'), (host, port))

                if message == "upload":
                    upMsg = (s.recv(2048)).decode()
                    fileName = input(upMsg)
                    s.sendto(fileName.encode('utf-8'), (host, port))
                    try:
                        f = open(fileName, "rb")
                        # Send file to client
                        s.send(f.read())
                        # Close file
                        f.close()
                    except FileNotFoundError as e:
                        print(str(e))
                    message = s.recv(2048).decode()
                    print(message)

                elif message == "download":
                    fileName = input("Input file name: ")
                    s.sendto(fileName.encode('utf-8'), (host,port))

                    f = open("new_" + fileName, "wb")
                    # Receive file
                    recv_file = s.recv(1024)
                    f.write(recv_file)

                    while (sys.getsizeof(recv_file) == 1057):
                        f.write(recv_file)
                        recv_file = s.recv(1024)

                    print("File received.")
                    f.close()
                    print("File saved.")
                    s.sendto("File Saved".encode(), (host,port))

                elif (message == "quit"):
                    break
            # close socket
            s.close()
            print("Socket connection closed")
        except socket.error as msg:
            print(str(msg))
            raise mySocketError("Socket protocol error...")

# Main Function
if __name__ == "__main__":
    try:
        # tcp client
        tcp_client()
    except mySocketError as msg:
        print(msg)
