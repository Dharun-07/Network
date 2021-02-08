import socket
import threading

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
h_name=input("ENTER YOUR NAME:")
port=10000
host=input("ENTER THE ADDRESS OF tHE HOST TO GET CONNECTED:")
print("**************connecting****************")
print("________________________________________")
conn.connect((host,port))
conn.send(h_name.encode('ascii'))
server_name=conn.recv(1024).decode('ascii')
print("********************connected**********************")
def send():
    while(1):
        message = input()
        conn.send(message.encode('ascii'))
        print()


thread=threading.Thread(target=send)
thread.daemon=True
thread.start()


for mess in iter(lambda :conn.recv(1024).decode('ascii'),''):
    print("\n"+"    "+server_name+":"+mess)


