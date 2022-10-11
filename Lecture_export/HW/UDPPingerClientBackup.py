import sys, time
from time import sleep
import socket

# Globals:
# s = None
host = None
port = None
ptime = 0


def test_socket_timeout(s):
    s.settimeout(1)


# Socket create
def socket_create():  # 1st
    # host = "127.0.0.1" # localhost
    global host
    global port
    global s
    global ptime

    s = None
    host = "192.168.0.10" # if of my dell on home lan
    port = 12000
    timeout = 1  # in seconds
    ptime = 0

    try:
        # Create UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Set socket timeout as 1 second - <socket_name>.settimeout(timeout)
        s.settimeout(timeout)

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Ping client
def ping_client():
    # Global variables
    global host
    global port
    # global s
    global ptime

    # Sequence number of the ping message

    # Ping for 10 times
    while ptime < 10:
        ptime += 1
        # Format the message to be sent
        # todo...
        message = input("Message: ")

        try:
            # Sent time
            RTTb = time.time()

            # Send the UDP packet with the ping message
            s.sendto(message.encode('utf-8'), (host, port))

            # Receive the server response
            data, addr = s.recvfrom(2048)
            print("IP: " + addr[0] + " | Port: " + str(addr[1]))
            print("Message: " + str(data.decode('utf-8')))

            # Received time
            RTTa = time.time()

            # Compute RTT
            # todo...

            # Display packet time
            # todo...

            sleep(1)

        except:
            # Server does not response
            # Assume the packet is lost
            print("Request timed out.")

            continue

    # Close socket
    s.close()


# Run ping statistics
def ping_statistics():
    # Global variables
    global s


    print("")
    print("--- IP ping statistics ---")

    # Print statistics
    # todo...


# **************************************
if __name__ == "__main__":  # main function
    socket_create()
    ping_client()
    ping_statistics()
