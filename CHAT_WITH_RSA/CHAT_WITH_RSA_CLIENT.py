#!/usr/bin/env python3
import socket
import rsa

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input("ENTER IP : ")
sock.connect((ip,10000))

print("CONNECTED")

s_pub=sock.recv(4098)
s_pub = rsa.key.PublicKey.load_pkcs1(s_pub, format='DER')
print("recieved pub")
mess=input("ENTER the text to send : ")
mess=rsa.encrypt(mess.encode('ascii'),s_pub)
sock.send(mess)
print("sent")
