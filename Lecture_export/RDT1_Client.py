import socket

# Global Variables
port = None
host = None


# Create Socket
def socket_create():
    global host
    global port
    global s
    host = "localhost"
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# State0
def state0():
    global host
    global port
    global s

    message = input("Message: ")
    if message == "quit":
        return None
    else:
        try:
            s.sendto(message.encode('utf-8'), (host, port))
        except socket.error as msg:
            print("Error sending message: " + str(msg))

    return state0


# Main Function
if __name__ == "__main__":
    global s

    # created socket
    socket_create()

    # Initial State
    state = state0
    while state:
        state = state()  # FSM Loop

    s.close()
    print("FSM Done")
