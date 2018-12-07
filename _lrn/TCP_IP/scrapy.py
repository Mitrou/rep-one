import sys
import socket
from scapy.all import *
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while 1:
    packet = s.recvfrom(2000);
    packet = packet[0]
    ip = TCP(packet)
    ip.show()