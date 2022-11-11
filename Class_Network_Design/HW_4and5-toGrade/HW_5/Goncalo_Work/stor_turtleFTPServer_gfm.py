import socket
import threading
import os

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

            x = threading.Thread(target=client_thread, args=(connectionSocket, addr, ))
            x.setDaemon(True)
            x.start()

            print("**********************************")
            print("Waiting for client...")

        except socket.error as e:
            print(str(e))
            break

# Client socket connection
def client_thread(connectionSocket, addr):
    print("[Thread Port: " + str(addr[1]) + "] Connected to Client -> IP: " + addr[0])

    try:
        # Receive message from client
        message = connectionSocket.recv(1024)
        str_message = str(message.decode('utf-8'))
        print("[Thread Port: " + str(addr[1]) + "] Client Message> " + str_message)

        # Get commands
        cmd = str_message.split("|")

        # cmd = LOGIN|username|password
        if cmd[0] == "LOGIN":
            # Check username and password
            if cmd[1] == "gfm" and cmd[2] == "12345":
                answer = "accepted"
            else:
                answer = "denied"

            # Send answer
            connectionSocket.send(answer.encode('utf-8'))
            print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")
            # Close connection
            connectionSocket.close()

        # cmd = RETR|filename
        elif cmd[0] == "RETR":
            # Get file name
            file_name = cmd[1]

            try:
                # Open file
                file = open(file_name, "rb+")

                # Send answer
                answer = "valid"
                connectionSocket.send(answer.encode('utf-8'))

                # Send file
                connectionSocket.send(file.read())
                connectionSocket.shutdown(socket.SHUT_WR)

                print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")
                # Close file
                file.close()

                # Close connection
                connectionSocket.close()

            except FileNotFoundError as e:
                answer = "error"
                # Send answer
                connectionSocket.send(answer.encode('utf-8'))
                print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")
                # Close connection
                connectionSocket.close()

        # cmd = STOR|filename
        elif cmd[0] == "STOR":
            # Get file name
            file_name = cmd[1]

            try:
                # Create file
                file = open("stor_" + file_name, "wb")
                print("Receiving file...")

                # Receiving data...
                recv_file = connectionSocket.recv(1024)
                while recv_file:
                    file.write(recv_file)
                    recv_file = connectionSocket.recv(1024)

                # Close file
                file.close()
                print("File Received...")

                # Send answer
                answer = "received"
                connectionSocket.send(answer.encode('utf-8'))
                print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")
                # Close connection
                connectionSocket.close()

            except FileNotFoundError as e:
                print(str(e))

        elif cmd[0] == "LIST":

            # List all files in current directory
            files_list = "LIST"
            basepath = os.getcwd()
            with os.scandir(basepath) as entries:
                for entry in entries:
                    if entry.is_file():
                        #print(entry.name)
                        files_list += "|" + entry.name

            # Send answer
            connectionSocket.send(files_list.encode('utf-8'))
            print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")

            # Close connection
            connectionSocket.close()

        elif cmd[0] == "REMV":
            # Get file name
            file_name = cmd[1]

            # Check if file exists...
            if os.path.exists(file_name):
                answer = "valid"
                os.remove(file_name)
            else:
                answer = "invalid"

            # Send answer
            connectionSocket.send(answer.encode('utf-8'))
            print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")

            # Close connection
            connectionSocket.close()

        # cmd = ERROR|data
        elif cmd[0] == "ERROR":
            # Close connection
            connectionSocket.close()

        # cmd = ?
        else:
            # Modify message
            answer = "Command not recognized"
            # Send modified message to client
            connectionSocket.send(answer.encode('utf-8'))
            print("[Thread Port: " + str(addr[1]) + "] Reply sent to client.")

            # Close connection
            connectionSocket.close()

    except socket.error as e:
        print(str(e))

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