import sys, time
from time import sleep
import socket
from random import random

# Socket create
def socket_create():
    global host
    global port
    global s

    host = "127.0.0.1"
    port = 12000
    timeout = 1 # in seconds

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
    global s
    global port
    global host
    global ptime 
    global lost_pkts
    global ping_runtime

    # Sequence number of the ping message
    ptime = 0
    # Number of lost packets 
    lost_pkts = 0
    # Start runtime  
    startTimer = time.time()

    # Ping for 10 times
    while ptime < 10: 
        ptime += 1
        # Format the message to be sent
        if random() > 0.5:
            message = "NO RND"
        else:
            message = "RND"
        
        try:
            # Sent time
            RTTb = time.time()

            # Send the UDP packet with the ping message
            s.sendto(message.encode('utf-8'),(host,port))
            
            # Receive the server response
            response, addr = s.recvfrom(2048)

            # Received time
            RTTa = time.time()

            # Compute RTT
            RTT = (1000*(RTTa - RTTb)) # in miliseconds

            # Display packet time
            print("{0} bytes from {1}: seq = {2} time = {3}ms".format(sys.getsizeof(response),addr[0],ptime,format(RTT,'.4f')))

            sleep(1)
            
        except:
            # Server does not response
            # Assume the packet is lost
            print("Request timed out.")
            # increment number of lost packets
            lost_pkts += 1
            continue
    # end timer
    endTimer = time.time()
    # mark PING run time
    ping_runtime = round(((endTimer - startTimer) * 1000),2)
    # Close socket
    s.close()

# Run ping statistics
def ping_statistics():
    # Global variables
    global s
    global host
    global port
    global ptime
    global lost_pkts
    global ping_runtime

    lostPkts_rate = 100 * (lost_pkts/ptime)
    pkt_recv = ptime - lost_pkts
    print("")
    print("--- {0} ping statistics ---".format(host))
    
    # Print statistics
    print("{0} packets transmitted, {1} received, {2}% packet loss, time {3}ms".format(ptime,pkt_recv,lostPkts_rate,ping_runtime))

#**************************************
if __name__ == "__main__":
    socket_create()
    ping_client()
    ping_statistics()
