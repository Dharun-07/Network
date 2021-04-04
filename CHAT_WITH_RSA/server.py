#!/usr/bin/env python3

import socket
import rsa


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_name=socket.gethostname()
ip=socket.gethostbyname(sock_name)
sock.bind((ip,10000))
sock.listen(1)
conn,addr=sock.accept()
print("CONNECTED")


pub,pri=rsa.newkeys(2048)
pub=pub.save_pkcs1(format='DER')
conn.send(pub)
mess=conn.recv(4098)
mess=rsa.decrypt(mess,pri)
print(mess.decode('ascii'))

