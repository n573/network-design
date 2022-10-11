import socket

# Global Variables
host = None
port = None


# Create Socket
def socket_create():
    global host
    global port
    global s
    host = ''
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind to Socket
def socket_bind():
    global host
    global port
    global s

    try:
        s.bind((host, port))
        print("The server is ready to receive")
    except socket.error as msg:
        print("Socket biding error: " + str(msg))


# State 0
def state0():
    global s

    try:
        data, addr = s.recvfrom(2048)
        print("IP: " + addr[0] + " | Port: " + str(addr[1]))
        print("Message: " + str(data.decode('utf-8')))
    except socket.error as msg:
        print(str(msg))

    return state0


# Main Function
if __name__ == "__main__":
    global s

    # created socket
    socket_create()
    # bind socket
    socket_bind()

    # Initial State
    state = state0
    while state:
        state = state()  # FSM Loop

    s.close()
    print("FSM Done")
