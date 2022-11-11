import sys, time
from time import sleep
import socket


# Global Variables
s: socket = socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = None
port = None
ptime: int = 0
RTT: float = 0.0


# Socket create
def socket_create():
    global host
    global port
    global s

    # host = "127.0.0.1"
    host = "192.168.0.10"
    port = 12000
    # timeout = 1  # in seconds
    timeout = 0.1  # in seconds -- for testing

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
    global s
    global ptime
    global RTT

    # Sequence number of the ping message
    ptime = 0

    # Ping for 10 times
    while ptime < 10:
        ptime += 1
        # Format the message to be sent
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
            RTT += RTTa - RTTb

            # Display packet time
            # print("packet time: %f", RTT * ptime)
            print("packet time: %f", RTT)

            sleep(1)

        except socket.error or socket.timeout > s.timeout:
            # Server does not response
            # Assume the packet is lost
            print("Request timed out.")

            continue

    # Close socket
    s.close()


# Run ping statistics
def ping_statistics():
    # Global variables
    global RTT
    global ptime
    global s
    global host
    global port

    print("")
    print("--- IP ping statistics ---")

    # Print statistics
    print("Reply from %s:%s: bytes=%d time < %d s TTL=%d" % (host, port, socket.socket.__sizeof__(s), RTT, ptime))
    # print("Reply from %s:%s: bytes=%d time < %d s TTL=%d" % (host, port, bytes.decode(s, '%s'), RTT, ptime))


# **************************************
if __name__ == "__main__":
    socket_create()
    ping_client()
    ping_statistics()
