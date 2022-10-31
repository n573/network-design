import socket
import my_ftpLib as myftp

class mySocketError(Exception):
    pass

    # TCP Client


def shell():
    msg = input('myturtle> ')
    if msg == 'quit':
        return
    elif msg == 'RETR' or 'retr':
        myftp.cmd_retr()
    elif msg == 'upload':
        myftp.upload()
        # elif msg == 'connect':
        #     myftp.connectServer()
    elif msg == 'help':
        helpMenu()
    elif msg == 'connect':
        myftp.socket_create()
        myftp.socket_connect()
        print("Created and connected socket")
    else:
        print("Command not valid.")


def helpMenu():
    cmds = ['quit', 'retr', 'upload', 'connect (WIP)', 'help (?): displays this message']
    for i in cmds:
        print(i)

def tcp_Client():
    global host
    global port
    global s

    while True:
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
