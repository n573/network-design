import socket
import ftp_lib as ftp

class mySocketError(Exception):
    pass

    # TCP Client


def tcp_Client():
    global host
    global port
    global s

    while True:

        msg = input('turtle> ')
        if msg == 'quit':
            break
        elif msg == 'retr':
            ftp.cmd_retr()
        elif msg == 'send':
            ftp.cmd_send()
        elif msg == 'req':
            ftp.clientReq()
        # elif msg != 'quit':
        #     ftp.socket_create()
        #     ftp.socket_connect()
        #     cmd = input("insert command for server \nturtle>")

        else:
            print("Command not valid.")




# **************************************
if __name__ == "__main__":
    tcp_Client()

