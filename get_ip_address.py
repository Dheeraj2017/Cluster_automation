#!/usr/bin/python2  -tt

import socket
import fcntl,struct
def get_ip_address(ifname):
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s',ifname[:15])
            #struct.pack('256s', bytes(ifname[:15],'utf-8'))
        )[20:24])


