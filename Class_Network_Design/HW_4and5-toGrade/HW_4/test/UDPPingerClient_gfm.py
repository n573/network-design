import sys, time  # with the line below time does not need to be in this line
from time import sleep  # keep this import for time and change the above line to simply 'import sys
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
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Set socket timeout as 1 second
        s.settimeout(timeout)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Ping client
def ping_client():
    global host
    global port
    global s
    global address
    global ptime
    global cnt_lost
    global tic
    global toc
    
    # Sequence number of the ping message
    ptime = 0
    cnt_lost = 0

    tic = time.time()

    # Ping for 10 times
    while ptime < 10: 
        ptime += 1
        # Format the message to be sent
        data = "NO RND".encode("utf-8") #Packets don't get lost
        #data = "RND".encode("utf-8") #Packets can get lost

        ## Should include some implementation to
        ##    use both NO RND and RND in the same run execution

        try:
            # Sent time
            RTTb = time.time()

            # Send the UDP packet with the ping message
            s.sendto(data,(host, port))
            # Receive the server response
            message, address = s.recvfrom(1024)  

            str_message = str(message.decode('utf-8'))

            # Received time
            RTTa = time.time()

            RTT = round((RTTa - RTTb)*1000, 3)
            if(str_message != "GOOD STRING"):
                print(str_message)
            print("{3} bytes from {0}: seq={1} time={2} ms".format(address[0],
                                                                   ptime,
                                                                   RTT,
                                                                   len(message)))

            sleep(1)
            
        except:
            # Server does not response
            # Assume the packet is lost
            print("Request timed out.")
            cnt_lost += 1
            continue

    # Close socket
    s.close()

    toc = time.time()

# Run ping statistics
def ping_statistics():
    global host
    global port
    global s
    global address
    global ptime
    global cnt_lost
    global tic
    global toc
    
    print("")
    print("--- {0} ping statistics ---".format(host))
    ##!!## CONSOLE THROWS ERROR: ADDRESS IS NEVER DEFINED ##!!##
    #  -- easy fix here would be to just use host rather than address[0]
    pkt_received = ptime - cnt_lost
    pkt_lost = round((float(cnt_lost)/float(ptime))*100, 0)
    running_time = round((toc-tic)*1000,0)
    print("{0} packets transmitted, {1} received, {2}% packet loss, time {3}ms".format(ptime,
                                                                                  pkt_received,
                                                                                  pkt_lost,
                                                                                  running_time))

#**************************************
if __name__ == "__main__":
    socket_create()
    ping_client()
    ping_statistics()
