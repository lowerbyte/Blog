import socket
import struct

def ipPacket(data):
    version = data[0] >> 4
    ihl = (data[0] & 0xF) * 4 
    total_length, ttl, protocol, src_address, dst_address = struct.unpack('!2xH4xBB2x4s4s', data[:20])
    return version, ihl, total_length, ttl, protocol, \
'.'.join(map(str,src_address)), '.'.join(map(str,dst_address)), data[ihl:]

def tcp(data):
    src_port, dst_port, seq, ack, flags = struct.unpack('!HHLLH', data[:14])
    data_offset = (flags >> 12) * 4
    flag_urg = (flags & 0x20) >> 5
    flag_ack = (flags & 0x10) >> 4
    flag_psh = (flags & 0x8 ) >> 3
    flag_rst = (flags & 0x4 ) >> 2
    flag_syn = (flags & 0x2 ) >> 1
    flag_fin = (flags & 0x1 )
    return src_port, dst_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst,\
flag_syn, flag_fin, data[data_offset:]

def mainLoop():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, 6)
    while True:
        data, addr = s.recvfrom(1024)
        version, ihl, total_length, ttl, protocol, src_address, dst_address, data = ipPacket(data) 
        print('------------------------------------------------------------')
        print('IP Packet:')
        print('Version: %s, IHL: %s, Total length: %s, TTL: %s\n Protocol: %s, Source address: %s, Destination address: %s\n' % (version, ihl,\
                    total_length, ttl, protocol, src_address, dst_address))

        src_port, dst_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst,\
flag_syn, flag_fin, data = tcp(data)
        print('TCP Packet')
        print('Source port: %s, Destination port: %s, Sequence: %s, \
Acknowledgment: %s\nFlags:\nURG: %s, ACK: %s, PSH: %s, RST: %s, SYN: %s, FIN:%s\n' % (src_port, dst_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
        
        print(data)
        print('------------------------------------------------------------')
        
if __name__ == '__main__':
    mainLoop()




