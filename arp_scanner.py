#!/usr/bin/env python3

from scapy.all import *

broadcast="FF:FF:FF:FF:FF:FF"
ip_range="192.168.75.1/24"
ether=Ether(dst=broadcast)
arp=ARP(pdst=ip_range)
fragment=ether/arp
ans,unans=srp(fragment,iface="eth0",timeout=2)
for send,recv in ans:
    ip=recv[ARP].psrc
    mac=recv[ARP].hwsrc
    print("IP=",ip,"mac=",mac)