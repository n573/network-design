import sys, time
from time import sleep
import socket

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
        #todo...
        # Set socket timeout as 1 second - <socket_name>.settimeout(timeout)
        #todo...
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Ping client
def ping_client():
    # Global variables
    #todo...
    
    # Sequence number of the ping message
    #todo...

    # Ping for 10 times
    while ptime < 10: 
        ptime += 1
        # Format the message to be sent
        #todo...
        
        try:
            # Sent time
            RTTb = time.time()

            # Send the UDP packet with the ping message
            #todo...
            
            # Receive the server response
            #todo...

            # Received time
            RTTa = time.time()

            # Compute RTT
            #todo...
            
            # Display packet time
            #todo...

            sleep(1)
            
        except:
            # Server does not response
            # Assume the packet is lost
            print("Request timed out.")
            
            continue

    # Close socket
    #todo...

# Run ping statistics
def ping_statistics():
    # Global variables
    #todo...
    
    print("")
    print("--- IP ping statistics ---")
    
    # Print statistics
    #todo...

#**************************************
if __name__ == "__main__":
    socket_create()
    ping_client()
    ping_statistics()
