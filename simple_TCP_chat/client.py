import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = input("Enter server address to get connected:\n")
server_address = (addr, 10000)
h_name = socket.gethostname()
print("connecting to {} server to port {}\n".format(h_name, server_address[-1]))
conn.connect(server_address)
print("Connected\n")
conn.send(h_name.encode())
s_name = conn.recv(1024)
s_name = s_name.decode()
print("{} has connected:\n".format(s_name))
while True:
    message = input("Me:")
    conn.send(message.encode())
    mess = conn.recv(1024).decode()
    print(">>>{}:{}".format(s_name, mess))
