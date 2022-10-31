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

        elif msg == 'RETR':
            ftp.cmd_retr()

        else:
            print("Command not valid.")


# **************************************
if __name__ == "__main__":
    tcp_Client()

