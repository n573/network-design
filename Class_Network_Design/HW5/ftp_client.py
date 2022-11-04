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

    while True:
        msg = input("turtle> ")

        if msg == "quit":
            break
        # elif msg == "RETR":
            # ftp.cmd_retr()
        elif msg == "connect":
            ftp.socket_create()
            ftp.socket_connect()
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

