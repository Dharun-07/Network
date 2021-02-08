import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=10000
host=input("ENTER THE IP ADDRESS:")
sock.connect((host,port))
print("-----------------------CONNECTION ESTABLISHED-------------------------------------------------------------------------------->")
f_name=input("ENTER THE NAME OF FILE TO SEND:")
with open(f_name,"rb") as file:
    while True:
        content=file.read(1024)
        if(not content):
            sock.send("COMPLETED...".encode('ascii'))
            break
        sock.send(content)
print("TRANSFFERED SUCCESSFULLY-------------------------->")
