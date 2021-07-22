#!/usr/bin/env python3

from scapy.all import *

ip=IP(dst="www.skillrack.com")
syn=TCP(sport=6343,dport=40000,flags="S",seq=1000)
segment=ip/syn
synack=sr1(segment,iface="eth0")
synack.show()
ack=ip/TCP(sport=6343,dport=40000,flags="A",seq=synack.ack,ack=synack.seq+1)
ack.show()