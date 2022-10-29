from scapy.all import *
import struct
import textwrap

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t '
DATA_TAB_2 = '\t\t '
DATA_TAB_3 = '\t\t\t '
DATA_TAB_4 = '\t\t\t\t '


def turtle_sniffer():
    IFACES.show()

    number = input("NIC number: ")
    iface = IFACES.dev_from_index(number)

    socket = conf.L2socket(iface=iface)

    try:

        while True:

            packet_raw = socket.recv_raw()
            print(packet_raw)

            dest_mac, src_mac, eth_proto, data = ethernet_frame(packet_raw[1])
            print("\nEthernet frame: ")
            print(TAB_1 + "Dest.: {} Source {}")
            # 8 for IPv4
            if eth_proto == 8:
                version, header_len, ttl, proto, src, target, data = ipv4_packet(data)
                print(TAB_1 + "IPv4 Packet: ")
                print(TAB_2 + "Version: {}, Header length: {}, TTL: {}".format(version, header_len, ttl))
                print(TAB_2 + "Protocol: {}, Source: {}, Target: {}".format(proto, src, target))

                # check protocols -- 1 = ICMP, 6 = TCP, 17 = UDP
                if proto == 1:
                    # print("ICMP")
                    icmp_type, code, checksum, data = icmp_packet(data)
                    print(TAB_1 + "ICMP Packet: ")
                    print(TAB_2 + "Type: {}, Code: {}, Checksum: {}".format(icmp_type, code, checksum))
                    print(TAB_2 + "Data: ")
                    print(format_multi_line(DATA_TAB_3, data))

                elif proto == 6:
                    # print("TCP")
                    src_port, dest_port, sequence, acknowledgment, offset_reserved_flags, \
                    flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_segment(data)
                    print(TAB_1 + "TCP Segment: ")
                    print(TAB_2 + "source port: {}, destination port: {}".format(src_port, dest_port))
                    print(TAB_2 + "sequence: {}, acknowledgment: {}".format(sequence, acknowledgment))
                    print(TAB_2 + "Flags:")
                    print(TAB_3 + "URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {}".format(flag_urg, flag_ack,
                                                                                                flag_psh, flag_rst,
                                                                                                flag_syn, flag_fin))

                    print(TAB_2 + "Data: ")
                    print(format_multi_line(DATA_TAB_3, data))

                elif proto == 17:
                    # print("UDP")
                    src_port, dest_port, length, data = udp_segment(data)
                    print(TAB_1 + "UDP Segment: ")
                    print(TAB_2 + "source port: {}, destination port: {}, length: {}".format(src_port, dest_port, length))
                    print(TAB_2 + "Data: ")
                    print(format_multi_line(DATA_TAB_3, data))

            else:
                print("Another Ethernet protocol...")


    except KeyboardInterrupt:
        print("turtle> BYE!!")
        pass


# Unpack ethernet frame
def ethernet_frame(data):
    try:
        dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
        return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]
    except:
        dest_mac = ""
        src_mac = ""
        proto = ""
        return dest_mac, src_mac, proto, ""


# Return properly formatted MAC address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02X}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


# Format data display
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


# Return properly format IPv4 address
def ipv4(addr):
    return '.'.join(map(str, addr))


# Unpack IPv4 Packet
def ipv4_packet(data):
    version_header_len = data[0]
    version = version_header_len >> 4
    header_len = (version_header_len & 15) * 4
    # Start unpacking header
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_len, ttl, proto, ipv4(src), ipv4(target), data[header_len:]


# Unpack ICMP packet
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]


# Unpack TCP segment
def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1

    return src_port, dest_port, sequence, acknowledgment, offset_reserved_flags, \
           flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

# Unpack UDP segment
def udp_segment(data):
    src_port, dest_port, length = struct.unpack('! H H H 2x', data[:8])
    return src_port, dest_port, length, data[8:]


# ------------------------------------
if __name__ == "__main__":
    turtle_sniffer()
    # get_mac_addr()
