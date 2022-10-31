import socket
import osLib as serv
import my_ftpLib as myftp

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


# Server Commands
# def os_cmd(cmd):
#     global s
#
#     s.recv(1024)

def recieveCmd():
    global s

    cmd = s.recv(1024)
    if cmd == 'quit':
        pass

    elif cmd == 'pwd':  # pwd command shows current directory
        serv.getCurrentDirectory()

    elif cmd == 'dir':  # dir shows the directory list/tree
        serv.listFiles()

    else:
        print("Command not valid.")


# TCP Server
def tcp_server():
    global host
    global port
    global s

    # Listen for incoming connections
    s.listen(1)
    print("**********************************")
    print("Waiting for client...")

    while True:
        try:
            connectionSocket, addr = s.accept()
            print("Connected to Client -> IP: " + addr[0] + " | Port: " + str(addr[1]))

            print("enter command: ")
            cmdin = s.recv(1024)
            if cmdin == 'upload':
                myftp.fileSendServ()

            # Close connection
            print("Socket closed.")
            connectionSocket.close()

            print("**********************************")
            print("Waiting for client...")

        except socket.error as e:
            print(str(e))
            break
        except KeyboardInterrupt:
            break


# def fileStuff():
#     # Receive file name
#     file_name = s.recv(1024)
#
#     try:
#         # Open file
#         f = open(file_name, "rb")
#
#         # Send file to client
#         s.send(f.read())
#         s.shutdown(socket.SHUT_WR)
#
#         # Close file
#         f.close()
#     except FileNotFoundError as e:
#         print(str(e))
#     except KeyboardInterrupt:
#         pass


# **************************************
if __name__ == "__main__":
    global s

    try:
        socket_create()
        socket_bind()
        tcp_server()
    except mySocketError as cmd:
        print(cmd)
    except KeyboardInterrupt:
        pass
        # exit(2);

    # Close main server socket
    s.close()
    print("Server offline.")
