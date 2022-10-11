import struct


# UDP Checksum Function
def checksum_func(data):
    checksum = 0
    data_len = len(data)

    # Appends 0's to the end of data and adjusts data_len
    if (data_len % 2):
        data_len += 1
        data += struct.pack('!B', 0)

    # Compute the sum
    for i in range(0, data_len, 2):
        w = (data[i] << 8) + (data[i + 1])
        checksum += w

    # Wrap around bit
    checksum = (checksum >> 16) + (checksum & 0xFFFF)

    # Complement the result
    checksum = ~checksum & 0xFFFF
    return checksum


# Main Function
if __name__ == '__main__':
    # Example 1
    msg = bytes("Hello".encode('utf-8'))
    answer = checksum_func(msg)
    print(answer)

    # Example 2
    msg = bytes(1234)
    answer = checksum_func(msg)
    print(answer)
