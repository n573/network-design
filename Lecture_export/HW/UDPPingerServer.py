import socket
from random import random


# Create Socket
def socket_create():
    global host
    global port
    global s

    host = ''
    port = 12000

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket
def socket_bind():
    global host
    global port
    global s

    try:
        s.bind((host, port))
        print("The server is ready to receive")
    except socket.error as msg:
        print("Socket binding error: " + str(msg))


# Ping server
def ping_server():
    global host
    global port
    global s

    flag = 0

    while True:
        message, clientAddress = s.recvfrom(2048)

        str_msg = str(message.decode('utf-8'))

        print("Message from {0}: {1}".format(clientAddress[0], str_msg))

        try:
            if (str_msg == "NO RND"):  # NO PKTs LOSS
                flag = 1
            elif (str_msg == "RND"):  # PKTs LOSS
                # Generate a random number
                if random() > 0.5:
                    flag = 0
                else:
                    flag = 1

            if (flag == 1):
                message = "GOOD STRING"
                s.sendto(message.encode('utf-8'), clientAddress)

        except:
            print("Sending message error...")


# **************************************
if __name__ == "__main__":
    socket_create()
    socket_bind()
    ping_server()
