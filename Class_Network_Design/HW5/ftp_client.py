import os
import socket
import ftp_lib as myftp

# Global Variables
s = None
host = None
port = None

####
# Must be able to:
# Login
# list (dir or ls) on server
# download
# upload
# show help
# show connection status
#
####
class mySocketError(Exception):
    pass


# Create Socket
# def socket_create():
#     global host
#     global port
#     global s
#     host = "localhost"
#     port = 1001
#
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     except socket.error as msg:
#         print("Socket creation error: " + str(msg))
#         raise mySocketError("Socket creation error...")
#
#
# def socket_connect():
#     global host
#     global port
#     global s
#
#     try:
#
#         s.connect((host, port))
#         print("Connected to Server -> IP: " + host + " | Port: " + str(port))
#
#     except socket.error as msg:
#         print(str(msg))
#         raise mySocketError("Socket connection error...")



# TCP Client Protocol
def tcp_client():
    global host
    global port
    global s
    connFlag = False

    while True:
        if connFlag == False:
            msg = input("turtle> ")
        elif connFlag == True:
            msg = input("turtle_server> ")
        else:
            print("something went wrong")

        if msg == "quit":
            if connFlag == True:
               myftp.s.close()
            break
        elif msg == "login":
            myftp.socket_create()
            myftp.socket_connect()  # contains login prompt
        elif msg == "download":
            myftp.cmd_retr()
        elif msg == "send":
            myftp.cmd_send()
        elif msg == "connect":
            myftp.socket_create()
            myftp.socket_connect()
            connFlag = True
        elif msg == "list":
            if connFlag == True:
                myftp.ls()
            elif connFlag == False:
                listFiles()  # clientside works
        elif msg == "close":
            myftp.s.close()
            connFlag = False
        elif msg == "help" and connFlag == True:
            print("since you're connected to a server...")
            # planned to send server a cmd code to display but that seemed overcomplicated
            print("download, send, close, list, --- login (WIP)")
        elif msg == "help" and connFlag == False:
            print("clientside commands are:\nconnect, help, quit")
        else:
            print("Command not valid")


def listFiles():
    # Get current directory
    path = os.getcwd()
    # List all files in current directory
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)


# Main Function
if __name__ == "__main__":

    try:
        # tcp client
        tcp_client()

    except mySocketError as msg:
        print(msg)
    # except KeyboardInterrupt as interr:
    #     print("keyboard interrupt")
    #     raise mySocketError(interr)

