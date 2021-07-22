#!/usr/bin/env python3
import socket
import threading
import os
import random
import string
import ssl, smtplib
import rsa
import pyaudio



#--------------initialising ssl connection
context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/home/kali/Downloads/newcert2.pem', '/home/kali/Downloads/newkey2.pem')

ssock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock=context.wrap_socket(ssock, server_side=True)
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

'''def read_cred():
    user = password = ''
    with open("cred.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        password = file[1].strip()

    return user, password


sender, password = read_cred()

receiver = "e8ec064@sairamtap.edu.in"

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
print("recieved user_passw")

if(user_passw!=passw):
    conn.send(b"_________________YOU HAVE ENTERED THE WRONG PASSWORD.SESSION IS TERMINATING_________________")
    conn.close()
    sock.close()
    quit()
else:
    conn.send(b"successful")
    print("CONNECTED---------------------------->")
    print("***YOU CAN START TYPING YOUR MESSAGE.FOR FILE SHARING ENTER <FILE_SHARE> TO ENABLE FILESHARE OR ENTER <quit> to QUIT***")'''



#SENDING PUBLIC KEY ------------------------------------------------>
publickey_DER=publickey.save_pkcs1(format='DER')
conn.send(publickey_DER)
print("KEY SENT")

#----------------recieving RSA
print("RECIEVING")
client_public_key=conn.recv(4096)
client_public_key=rsa.key.PublicKey.load_pkcs1(client_public_key, format='DER')
print("KEY RECIEVED")

#STARTED------------------------------------------------>


def voice():
        '''try:
            chunk_size = 1024  # 512
            audio_format = pyaudio.paInt16
            channels = 1
            rate = 20000

            # initialise microphone recording
            p = pyaudio.PyAudio()
            playing_stream = p.open(format=audio_format, channels=channels, rate=rate, output=True,
                                    frames_per_buffer=chunk_size)
            recording_stream = p.open(format=audio_format, channels=channels, rate=rate, input=True,
                                      frames_per_buffer=chunk_size)

            print("Connected to Server")

            def receive_server_data():
                while True:
                    try:
                        data =conn.recv(1024)
                        if(data==b"end"):
                            break
                        playing_stream.write(data)
                    except KeyboardInterrupt:
                        conn.send(b'end')
                        break

            def send_data_to_server():
                while True:
                    try:
                        data = recording_stream.read(16200)
                        conn.sendall(data)
                    except KeyboardInterrupt:
                        conn.send(b'end')
                        break

                    # start threads

            receive_thread = threading.Thread(target=receive_server_data)
            receive_thread.daemon = True
            receive_thread.start()
            send_data_to_server()

            while True:
                try:
                    data = conn.recv(1024)
                    if (data == b"end"):
                        break
                    playing_stream.write(data)
                except KeyboardInterrupt:
                    break
        except KeyboardInterrupt:
            return '''
        try:
            chunk_size = 1024  # 512
            audio_format = pyaudio.paInt16
            channels = 2
            rate = 20000

            # initialise microphone recording
            p = pyaudio.PyAudio()
            playing_stream = p.open(format=audio_format, channels=channels, rate=rate, output=True,
                                    frames_per_buffer=chunk_size)
            recording_stream = p.open(format=audio_format, channels=channels, rate=rate, input=True,
                                      frames_per_buffer=chunk_size)

            print("Connected to Server")

            def receive_server_data():
                while True:
                    try:
                        data = conn.recv(1024)
                        if (data == b"end"):
                            break
                        playing_stream.write(data)
                    except KeyboardInterrupt:
                        conn.send(b'end')
                        break

            def send_data_to_server():
                while True:
                    try:
                        data = recording_stream.read(16200)
                    except KeyboardInterrupt:
                        conn.send(b'end')
                        conn.sendall(data)
                        break


                # start threads

            receive_thread = threading.Thread(target=receive_server_data)
            receive_thread.daemon = True
            receive_thread.start()
            send_data_to_server()

            '''while True:
                try:
                    data = conn.recv(1024)
                    if (data == b"end"):
                        break
                    playing_stream.write(data)
                except KeyboardInterrupt:
                    break'''
        except KeyboardInterrupt:
            return 0




def send():
    while(1):
        message=input()
        if(message==b"quit"):
            quit()
        if(message=="FILE_SHARE"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, client_public_key)
            conn.send(message)
            #thread = threading.Thread(target=file_send)
            #thread.daemon = True
            #thread.start()
            file_send()
        elif(message=="call"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, client_public_key)
            conn.send(message)
            voice()
        else:
            message_encode=message.encode('ascii')
            ciphertext=rsa.encrypt(message_encode,client_public_key)
            conn.send(ciphertext)
            print()

def file_send():
    f_name=input("***ENTER THE NAME OF THE FILE")
    filesize = os.path.getsize(f_name)
    f_name1=f_name.encode('ascii')
    f_name1=rsa.encrypt(f_name1, client_public_key)
    conn.send(f_name1)
    conn.send(str(filesize).encode('ascii'))
    #progress = tqdm(range(filesize), desc=f"SENDING {f_name}", unit="KB")
    with open(f_name,"rb") as fil:

        while(True):
            content=fil.read(245)
            if(not content):
                content=b"completed"
                ciphertext = rsa.encrypt(content, client_public_key)
                conn.send(ciphertext)
                print("\n SENT_SUCCESSFULLY------------------>")
                fil.close()
                break
            else:
                ciphertext= rsa.encrypt(content, client_public_key)
                conn.send(ciphertext)
            #progress.update(len(content))



thread=threading.Thread(target=send)
thread.daemon=True
thread.start()






try:
    for mess in iter(lambda :conn.recv(1029),''):
        mess = rsa.decrypt(mess, privatekey)
        if (mess == "FILE_SHARE".encode('ascii')):
            received_file_name = conn.recv(1024)
            received_file_name = rsa.decrypt(received_file_name, privatekey)
            received_file_name=received_file_name.decode('ascii')
            r_filesize = int(conn.recv(1024).decode('ascii'))
            with open(received_file_name, "wb") as fil:
                #progress = tqdm(range(r_filesize), desc=f"Receiving {recieved_file_name}", unit="KB")
                while (True):
                    r_content = conn.recv(1024)
                    r_content = rsa.decrypt(r_content, privatekey)
                    if (r_content == b"completed"):
                        print(f"\n RECIEVED FILE {received_file_name}")
                        fil.close()
                       #progress.update(len(r_content))
                        break
                    else:
                        fil.write(r_content)
                    #progress.update(len(r_content))
        elif(mess=="call".encode('ascii')):
            voice()
        else:
            print("\n" + "    " + client_name + ":" + str(mess.decode('ascii')))
except KeyboardInterrupt:
    conn.close()
    print("CONNECTION CLOSED_____________")