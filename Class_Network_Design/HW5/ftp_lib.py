import socket

class mySocketError(Exception):
    pass

# For sockets:

# Create Socket
def socket_create():
    global host
    global port
    global s

    host = "localhost"
    port = 12500

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

    except socket.error as msg:
        print(str(msg))
        raise mySocketError("Socket connection error...")

def cmd_retr():
    try:
        # Create socket and connect to server
        socket_create()
        socket_connect()

        print("Connected to Server.")

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
        s.close()
        print("Socket closed.")
        print("**********************************")

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))




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
