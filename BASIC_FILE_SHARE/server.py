import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

h_name=socket.gethostname()
host=socket.gethostbyname(h_name)
port=10000
print("ip address of the SERVER:",host)
sock.bind((host,port))
sock.listen(1)
conn,addr=sock.accept()
f=open("new.mp4","wb")
for mess in iter(lambda :conn.recv(1024),""):
    if(mess.decode('ascii')=="COMPLETED..."):
        f.close()
        conn.close()
        break
    else:f.write(mess)
print("RECIEVED-------------------------------------->")
