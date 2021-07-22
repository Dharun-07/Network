#!/usr/bin/env python3

from scapy.all import *

dns_req=IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='www.skillrack.com'))
answer=sr(dns_req)
print(answer)