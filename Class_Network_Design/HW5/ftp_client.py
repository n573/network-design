import socket
import ftp_lib as ftp

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
            ftp.s.close()
            break
        elif msg == "download":  #  & connFlag:
            ftp.cmd_retr()
        elif msg == "send":
            ftp.cmd_send()
        elif msg == "connect":
            ftp.socket_create()
            ftp.socket_connect()
            connFlag = True
        elif msg == "close":
            ftp.s.close()
            connFlag = False
        else:
            print("Command not valid")




# Main Function
if __name__ == "__main__":

    try:
        # tcp client
        tcp_client()

    except mySocketError as msg:
        print(msg)
    except KeyboardInterrupt as interr:
        print("keyboard interrupt")
        raise mySocketError(interr)

