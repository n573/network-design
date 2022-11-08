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
    host = "localhost"
    port = 1001

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# UDP Client Protocol
def udp_client():
    global host
    global port
    global s

    key = b'abcdefgh'
    des = DES.new(key, DES.MODE_ECB)

    while True:
        message = input("Message: ")
        if message == "quit":
            break
        else:
            padded = pad(message)
            encrypted_msg = des.encrypt(bytes(padded, 'utf-8'))
            try:
                # s.sendto(message.encode('utf-8'), (host, port))
                s.sendto(encrypted_msg, (host, port))

                data, addr = s.recvfrom(2048)
                print("IP: " + addr[0] + " | Port: " + str(addr[1]))
                print("Message: " + str(data.decode('utf-8')))
                # print("Message: " + str(des.decrypt(data.decode('utf-8'))))
                # des.decrypt(data.decode('utf-8'))
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
    # udp client
    udp_client()

