import socket

global host
global port
global s


class mySocketError(Exception):
    pass

# For sockets:

# Create Client-side Socket
def socket_create():
    global host
    global port
    global s

    host = "localhost"
    port = 12500

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # stream indicates TCP connection
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("socket created")  # for testing
    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket creation error...")


# Connect socket
def socket_connect():
    global host
    global port
    global s

    try:
        s.connect((host, port))
        print("Connected to Server -> IP: " + host + " | Port: " + str(port))
        # send_cmd()  # opens server shell
    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket connection error...")


def send_cmd():  # sends a command to the server (server shell)
    # CURRENTLY DISABLED
    while True: 
        cmd = input("turtle server> ")
        if cmd == "quit": 
            print("disconnecting from server")
            s.close()  # closes client socket
            break
        elif cmd == "download":
            s.send("retr".encode('utf-8'))  # sends server which command to expect
            cmd_retr()  # client-side portion of retrieve
            # s.send("retr".encode('utf-8'))  # sends server which command to expect
        elif cmd == "upload":
            ...
        elif cmd == "help":
            print("quit, download, upload, help")
        elif cmd == "close":  # ideally only admins, stops server
            s.send("close".encode('utf-8'))
            break
        else:
            print("command not valid")


def cmd_retr():
    try:
        # Create socket and connect to server
        # socket_create()
        # socket_connect()

        # print("Connected to Server.")
        s.send("retr".encode('utf-8'))  # tells server what cmd to expect

        file_name = input("File name> ")

        # Send file name
        s.send(file_name.encode('utf-8'))
        print("File name sent. Waiting for file...")

        # Open new file
        f = open("new_" + file_name, "wb")

        # Receive file
        recv_file = s.recv(1024)
        while recv_file:
            f.write(recv_file)
            recv_file = s.recv(1024)

        print("File received.")
        f.close()
        print("File saved.")

        # Close socket
        # s.close()
        # print("Socket closed.")
        # print("**********************************")

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))


def cmd_send():  # send file from client -> server
    try:
        # Create socket and connect to server
        # socket_create()
        # socket_connect()

        s.send("getF".encode('utf-8'))  # executes server-side

        file_name = input("File to send> ")

        s.send(file_name.encode('utf-8'))  # tells server what the original filename is

        f = open(file_name, "rb")

        # Send file
        print("File " + file_name + " sending... Waiting for completion...")
        s.send(f.read())
#        s.shutdown(socket.SHUT_WR)  # !!not sure if this is good, check later
        s.shutdown(1)  # This tells the server “This client is done sending, but can still receive.”
        print("File sent.")
        f.close()
        # print("File save confirmed.") # get ACK from server that it received the file
        print("File send completed.")

        # Close socket
        # s.close()
        # print("Socket closed.")
        # print("**********************************")

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))


def login(user, passwd):
    ...


def ls():
    s.send("dir".encode('utf-8'))

# def clientReq(): # client request to server (for example, which command the server should execute)
#     global host
#     global port
#     global s
#
#     socket_create()
#     socket_connect()
#     msg = input("what do you need from the server?\nturtle> ")
#     s.send(msg.encode('utf-8'))
#     print("sent \'" + msg + "\' to the server")
#     # s.close()  # CHECK THIS FIRST IF THINGS DONT WORK


# def getFile(ftp, filename):
#     try:
#         ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
#     except Exception as e:
#         print(str(e))
#
#
# def main():
#
#     try:
#         ftp = ftplib.FTP("ftp.nluug.nl")
#         ftp.login("anonymous", "ftplib-example-1")
#         ftp.dir()
#
#         input()
#         ftp.cwd("/pub/")
#         ftp.dir()
#
#         input()
#         getFile(ftp, 'README.nluug')
#         ftp.quit()
#
#     except Exception as e:
#         print(str(e))
#
#
# if __name__ == "__main__":
#     main()
