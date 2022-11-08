import socket
from Cryptodome.Cipher import DES

# Global Variables
s = None
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


# UDP Server Protocol
def udp_server():
    global s

    key = b'abcdefgh'
    des = DES.new(key, DES.MODE_ECB)

    while True:
        try:
            data, addr = s.recvfrom(2048)
            print("IP: " + addr[0] + " | Port: " + str(addr[1]))
            # decrypted_data = des.decrypt(data.decode('utf-8'))
            decrypted_data = des.decrypt(data)
            print("Message: " + str(decrypted_data))

            # tosend = des.encrypt(decrypted_data.upper())
            # s.sendto(tosend, (addr[0], addr[1]))
            s.sendto(decrypted_data, (addr[0], addr[1]))
        except socket.error as msg:
            print(str(msg))

    s.close()

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Main Function
if __name__ == "__main__":
    # created socket
    socket_create()
    # bind socket
    socket_bind()
    # udp server
    udp_server()
