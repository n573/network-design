import socket
import my_ftpLib as myftp

class mySocketError(Exception):
    pass

    # TCP Client

def shell():
    while True:

        msg = input('myturtle> ')
        if msg == 'quit':
            break

        elif msg == 'RETR':
            myftp.cmd_retr()

        elif msg == 'connect':
            myftp.connectServer()

        else:
            print("Command not valid.")

def tcp_Client():
    global host
    global port
    global s

    shell()
    # while True:
    #
    #     msg = input('turtle> ')
    #     if msg == 'quit':
    #         break
    #
    #     elif msg == 'RETR':
    #         cmd_retr()
    #
    #     elif msg == 'connect':
    #         connectServer()
    #
    #     else:
    #         print("Command not valid.")


# **************************************
if __name__ == "__main__":
    tcp_Client()

