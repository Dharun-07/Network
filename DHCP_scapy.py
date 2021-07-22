#!/usr/bin/env python3

'''from scapy.all import *
from random import *


hw = get_if_hwaddr('eth0')
dhcp_discover=Ether(dst="FF:FF:FF:FF:FF:FF")/IP(src='0.0.0.0',dst="192.168.72.254")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw,xid=randint(1,4321455662))/DHCP(options=[('message-type','discover'),'client_id',hw,'lease+time',10000,'end'])
sendp(dhcp_discover,iface="eth0")
#rint(resp.show())'''


'''from scapy.all import *

def dhcp_discover(dst_mac="ff:ff:ff:ff:ff:ff"):
    src_mac = get_if_hwaddr(conf.iface)
    spoofed_mac = RandMAC()
    options = [("message-type", "discover"),
               ("max_dhcp_size",1500),
               ("client_id", mac2str(spoofed_mac)),
               ("lease_time",10000),
               ("end","0")]
    transaction_id = random.randint(1, 900000000)
    dhcp_request = Ether(src=src_mac,dst=dst_mac)\
                    /IP(src="0.0.0.0",dst="255.255.255.255")\
                    /UDP(sport=68,dport=67)\
                    /BOOTP(chaddr=[mac2str(spoofed_mac)],
                                   xid=transaction_id,
                                   flags=0xFFFFFF)\
                    /DHCP(options=options)
    resp=sr1(dhcp_request,
          iface=conf.iface)

if __name__=="__main__":
    dhcp_discover()'''
'''from scapy.all import *

conf.checkIPaddr=False

# configuration
localiface = 'eth0'
myhostname='vektor'
localmac = get_if_hwaddr(localiface)

# craft DHCP DISCOVER
dhcp_discover = Ether(src=localmac, dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0', dst='255.255.255.255')/UDP(dport=67, sport=68)/BOOTP(chaddr=localmac,xid=RandInt())/DHCP(options=[('message-type', 'discover'), 'end'])

# send discover, wait for reply
dhcp_offer = srp1(dhcp_discover,iface=localiface)#,multi=True for identifying rogue DHCP servvers
print (dhcp_offer)

# craft DHCP REQUEST from DHCP OFFER
myip=dhcp_offer[BOOTP].yiaddr
sip=dhcp_offer[BOOTP].siaddr
xid=dhcp_offer[BOOTP].xid
dhcp_request = Ether(src=localmac,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=localmac,xid=xid)/DHCP(options=[("message-type","request"),("hostname",myhostname),("server_id",sip),("requested_addr",myip),("param_req_list","pad"),"end"])
print (dhcp_request.display())

# send request, wait for ack
conf.checkIPaddr=False
dhcp_ack = srp1(dhcp_request,iface=localiface)
print (dhcp_ack.display())'''


'''from scapy.all import *

conf.checkIPaddr=False

# configuration
localiface = 'eth0'
requestMAC = 'fc:4d:d4:33:2f:41'
myhostname='vektor'
localmac = get_if_hwaddr(localiface)
localmacraw = requestMAC

# craft DHCP DISCOVER
dhcp_discover = Ether(src=localmac, dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0', dst='255.255.255.255')/UDP(dport=67, sport=68)/BOOTP(chaddr=localmac,xid=RandInt())/DHCP(options=[('message-type', 'discover'), 'end'])
print(dhcp_discover.display())

# send discover, wait for reply
dhcp_offer = srp1(dhcp_discover,iface=localiface)
print(dhcp_offer.display())

# craft DHCP REQUEST from DHCP OFFER
myip=dhcp_offer[BOOTP].yiaddr
sip=dhcp_offer[BOOTP].siaddr
xid=dhcp_offer[BOOTP].xid
dhcp_request = Ether(src=localmac,dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=localmac,xid=xid)/DHCP(options=[("message-type","request"),("server_id",sip),("requested_addr",myip),("hostname",myhostname),("param_req_list","pad"),"end"])
print(dhcp_request.display())

# send request, wait for ack
dhcp_ack = srp1(dhcp_request,iface=localiface)
print(dhcp_ack.display())'''

#!/usr/bin/env python

from scapy.all import *

conf.checkIPaddr=False

# configuration
localiface = 'eth0'
requestMAC = 'fc:4d:d4:33:2f:41'
myhostname='vektor'
localmac = get_if_hwaddr(localiface)
localmacraw = requestMAC

# craft DHCP DISCOVER
dhcp_discover = Ether(src=localmac, dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0', dst='255.255.255.255')/UDP(dport=67, sport=68)/BOOTP(chaddr=localmacraw,xid=RandInt())/DHCP(options=[('message-type', 'discover'), 'end'])
print(dhcp_discover.display())

# send discover, wait for reply
dhcp_offer = srp1(dhcp_discover,iface=localiface)
print(dhcp_offer.display())

# craft DHCP REQUEST from DHCP OFFER
myip=dhcp_offer[BOOTP].yiaddr
sip=dhcp_offer[BOOTP].siaddr
xid=dhcp_offer[BOOTP].xid
d_mac=dhcp_offer[Ether].src
d_ip=dhcp_offer[BOOTP].siaddr
dhcp_request = Ether(src=localmac,dst="FF:FF:FF:FF:FF:FF")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=localmacraw,xid=xid)/DHCP(options=[('message-type','request'),'end'])
print(dhcp_request.display())

# send request, wait for ack
dhcp_ack = srp1(dhcp_request,iface=localiface)
print(dhcp_ack.display())
