st, port))
        print("Connected to Server -> IP: " + host + " | Port: " + str(port))

        # Authentication
        print("Login:")
        username = input("Username> ")
        password = input("Password> ")

        # Send message
        msg = "LOGIN|" + username + "|" + password
        s.send(msg.encode('utf-8'))
        print("Message sent. Waiting for reply...")

        # Receive reply
        answer = s.recv(1024)
        str_answer = str(answer.decode('utf-8'))
        print("Reply from Server: " + str_answer)

        # Close socket
        s.close()
        #print("Socket closed.")
        #print("**********************************")

        if str_answer == "accepted":
            turtle_ftp()
        else:
            print("Wrong authentication")
            # return to turtle shell

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))

# FTP Retrieve
def ftp_retr():
    # Retrieve file from server
    global host
    global port
    global s

    try:
        # Create socket and connect to server
        socket_create()
        socket_connect((host, port))

        # File name
        file_name = input("File name> ")

        # Send message
        msg = "RETR|" + file_name
        s.send(msg.encode('utf-8'))
        print("Message sent. Waiting for reply...")

        # Receive reply
        answer = s.recv(1024)
        str_answer = str(answer.decode('utf-8'))
        #print("Reply from Server: " + str_answer)

        if str_answer == "error":
            print("Reply from Server: " + str_answer)
        else:
            # Save file locally
            file = open("retr_" + file_name, "wb")

            # Receive file
            data = s.recv(1024)
            while data:
                file.write(data)
                data = s.recv(1024)

            file.write(data)

            file.close()
            print(file_name + " retrieved successfully.")

        # Close socket
        s.close()
        # print("Socket closed.")
        # print("**********************************")

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))

# FTP Store
def ftp_stor():
    # Send file to server
    global host
    global port
    global s

    try:
        # Create socket and connect to server
        socket_create()
        socket_connect((host, port))

        try:
            # Open File
            file_name = input("File name> ")
            file = open(file_name, "rb")

            # Send message
            msg = "STOR|" + file_name
            s.send(msg.encode('utf-8'))

            # Send file
            s.send(file.read())
            s.shutdown(socket.SHUT_WR)

            print("Sending file to server...")
            # Close file
            file.close()

            # Wait for answer from server
            answer = s.recv(1024)
            str_answer = str(answer.decode('utf-8'))
            if str_answer == "received":
                print(file_name + " stored successfully.")
            else:
                print(str_answer)

        except FileNotFoundError as e:
            print(str(e))
            # Send error
            msg = "ERROR|" + file_name
            s.send(msg.encode('utf-8'))

        # Close socket
        s.close()

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))

# FTP List
def ftp_list():
    # Send file to server
    global host
    global port
    global s

    try:
        # Create socket and connect to server
        socket_create()
        socket_connect((host, port))

        # Send message
        msg = "LIST"
        s.send(msg.encode('utf-8'))
        print("Message sent. Waiting for reply...")

        # Wait for answer from server
        answer = s.recv(1024)
        str_answer = str(answer.decode('utf-8'))

        # Split message
        files_name = str_answer.split("|")
        for x in range(len(files_name)):
            print(files_name[x])
        print("")

        # Close socket
        s.close()

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))

# FTP Remove
def ftp_remv():
    # Retrieve file from server
    global host
    global port
    global s

    try:
        # Create socket and connect to server
        socket_create()
        socket_connect((host, port))

        # File name
        file_name = input("File name> ")

        # Remove confirmation
        confirmation = input("Are you sure you want to remove " + file_name + "? [y/n]: ")

        if confirmation == "y":
            # Send message
            msg = "REMV|" + file_name
            s.send(msg.encode('utf-8'))
            print("Message sent. Waiting for reply...")

            # Receive reply
            answer = s.recv(1024)
            str_answer = str(answer.decode('utf-8'))
            print("Reply from Server: " + str_answer)

            if str_answer == "valid":
                print("File removed.")
            else:
                print("File doesn't exist.")

        else:
            # Send Error
            msg = "ERROR"
            s.send(msg.encode('utf-8'))

        # Close socket
        s.close()

    except socket.error as e:
        print(str(e))
    except mySocketError as e:
        print(str(e))

# turtle FTP Client
def turtle_ftp():

    while True:

        msg = input('command> ')
        print("")
        if msg == 'quit':
            print("Leave server...")
            print("")
            break

        elif msg == 'help':
            turtle_help("ftp_command")

        elif msg == 'list':
            ftp_list()

        elif msg == 'retr':
            ftp_retr()

        elif msg == 'stor':
            ftp_stor()

        elif msg == 'remv':
            ftp_remv()

        else:
            print("Command not available.")
            print("")

# Turtle Help
def turtle_help(command):
    print("turtle FTP commands available")
    print("***********************")

    if command == "turtle_shell":
        print("login -> login to an FTP server")
        print("quit - > exit turtle FTP")

    elif command == "ftp_command":
        print("list - > list available files to retrieve")
        print("retr - > retrieve file from server")
        print("stor - > store file on server")
        print("remv - > remove file on server")
        print("quit - > leave server")

    print("help -> available commands")
    print("")

# turtle FTP Shell
def turtle_shell():

    print("")
    print("***********************************")
    print("Welcome to turtle FTP")
    print("-> type help to see available commands")
    print("***********************************")
    print("")

    while True:

        msg = input('turtle> ')
        print("")
        if msg == 'quit':
            print("turtle says bye.")
            print("")
            break

        elif msg == 'help':
            turtle_help("turtle_shell")

        elif msg == 'login':
            ftp_login()

        else:
            print("Command not available.")
            print("")

# **************************************
if __name__ == "__main__":
    turtle_shell()
