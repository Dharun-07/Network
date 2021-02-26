from scapy.all import *

print("-------------------------------------GET_MAC------------------------------------")
a=input("Enter the ip address : ")

response,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=a),timeout=2,retry=10)
for s,r in response:
    print(r[Ether].src)