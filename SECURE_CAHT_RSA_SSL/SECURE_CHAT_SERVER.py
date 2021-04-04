#!/usr/bin/env python3
import socket
import threading
import os
import random
import string
import ssl, smtplib
import rsa



#--------------initialising ssl connection
context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/home/kali/Downloads/newcert2.pem', '/home/kali/Downloads/newkey2.pem')

ssock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock=context.wrap_socket(ssock, server_side=True)
name=input("ENTER YOUR NAME:")
port=10000
host="0.0.0.0"
h_name=socket.gethostname()
h_addr=socket.gethostbyname("localhost")
print("The server has got address {}".format(h_addr))
sock.bind((host,port))
sock.listen(1)
conn,addr=sock.accept()
print("**************connecting****************")
client_name=conn.recv(1204).decode()
conn.send(name.encode('ascii'))
print("__________connected to {}_______________".format(client_name))



#-------------INITIALISING CONNEcTION

'''sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
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
client_name=conn.recv(1204).decode()
conn.send(name.encode('ascii'))
print("__________connected to {}_______________".format(client_name))'''



#----------------Generating RSA
publickey,privatekey=rsa.newkeys(2048)



#----------------GENERATING PASSW

strings=string.printable
strings=strings.replace(" ","")
char=string.ascii_uppercase+string.digits+string.ascii_lowercase+strings
passw=""
for i in range(15):
    passw+=random.choice(char)

#--------------SENDING EMAIL

def read_cred():
    user = password = ''
    with open("cred.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        password = file[1].strip()

    return user, password


sender, password = read_cred()

receiver = ""

port = 465

message =f"""\
Subject: Welcome To Secure Chat This is your password

{passw}

Thank you
"""

context = ssl.create_default_context()

print("-----------------Starting to send-----------------")

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as serv:
    serv.login(sender, password)
    serv.sendmail(sender, receiver, message)

print("------------------Email Sent----------------------")


user_passw=conn.recv(1024).decode('ascii')

if(user_passw!=passw):
    conn.send(b"_________________YOU HAVE ENTERED THE WRONG PASSWORD.SESSION IS TERMINATING_________________")
    conn.close()
    sock.close()
    quit()
else:
    conn.send(b"successful")
    print("CONNECTED---------------------------->")
    print("***YOU CAN START TYPING YOUR MESSAGE.FOR FILE SHARING ENTER <FILE_SHARE> TO ENABLE FILESHARE OR ENTER <quit> to QUIT***")



#SENDING PUBLIC KEY ------------------------------------------------>
publickey_DER=publickey.save_pkcs1(format='DER')
conn.send(publickey_DER)
print("KEY SENT")



#STARTED------------------------------------------------>
def send():
    while(1):
        message=input()
        if(message=="quit"):
            quit()
        if(message=="FILE_SHARE"):
            conn.send(message.encode('ascii'))
            #thread = threading.Thread(target=file_send)
            #thread.daemon = True
            #thread.start()
            file_send()
        else:
            message_encode=message.encode('ascii')
            ciphertext=rsa.encrypt(message_encode,publickey)
            conn.send(ciphertext)
            print()

def file_send():
    f_name=input("***ENTER THE NAME OF THE FILE")
    conn.send(f_name.encode('ascii'))
    filesize = os.path.getsize(f_name)
    conn.send(str(filesize).encode('ascii'))
    #progress = tqdm(range(filesize), desc=f"SENDING {f_name}", unit="KB")
    with open(f_name,"rb") as fil:
        while(True):
            content=fil.read(1024)
            if(not content):
                conn.send(b"completed")
                print("\n SENT_SUCCESSFULLY------------------>")
                fil.close()
                break
            else:
                conn.send(content)
            #progress.update(len(content))



thread=threading.Thread(target=send)
thread.daemon=True
thread.start()



try:
    for mess in iter(lambda :conn.recv(1029),''):
        if (mess == "FILE_SHARE".encode('ascii')):
            recieved_file_name = conn.recv(1024).decode('ascii')
            r_filesize = int(conn.recv(1024).decode('ascii'))
            with open(recieved_file_name, "wb") as fil:
                #progress = tqdm(range(r_filesize), desc=f"Receiving {recieved_file_name}", unit="KB")
                while (True):
                    r_content = conn.recv(1024)
                    if (r_content == b"completed"):
                        print(f"\n RECIEVED FILE {recieved_file_name}")
                        fil.close()
                       #progress.update(len(r_content))
                        break
                    else:
                        fil.write(r_content)
                    #progress.update(len(r_content))
        else:
            mess=rsa.decrypt(mess,privatekey)
            print("\n" + "    " + client_name + ":" + str(mess.decode('ascii')))
except KeyboardInterrupt:
    conn.close()
    print("CONNECTION CLOSED_____________")
