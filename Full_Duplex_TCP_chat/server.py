import socket
import threading

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=input("ENTER YOUR NAME:")
port=10000
host="0.0.0.0"
h_name=socket.gethostname()
h_addr=socket.gethostbyname(h_name)
print("The server has got address {}".format(h_addr))
sock.bind((host,port))
sock.listen(1)
conn,addr=sock.accept()
print("**************connecting****************")
print("________________________________________")
client_name=conn.recv(1204).decode()
conn.send(name.encode('ascii'))
print("connected to {}".format(client_name))
def send():
    while(1):
        message=input()
        conn.send(message.encode('ascii'))
        print()

thread=threading.Thread(target=send)
thread.daemon=True
thread.start()

for mess in iter(lambda :conn.recv(1024).decode('ascii'),''):
    print("\n"+"    "+client_name+":"+mess)


