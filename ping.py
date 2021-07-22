#!/usr/bin/env python3

from scapy.all import *
ip=IP(dst="google.com")
icmp=ICMP(id=100)
packet=ip/icmp
response=sr1(packet,iface="eth0")
print(response)