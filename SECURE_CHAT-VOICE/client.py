#!/usr/bin/env python3

import socket
import threading
import os
from tqdm import tqdm
import ssl
import rsa
import pyaudio




context=ssl.create_default_context()
context.load_verify_locations('/home/kali/Downloads/newcert2.pem')

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn=context.wrap_socket(sock,server_hostname="localhost")
h_name=input("ENTER YOUR NAME:")
port=10000
host=input("ENTER THE ADDRESS OF tHE HOST TO GET CONNECTED:")
print("**************connecting****************")
print("________________________________________")
conn.connect(("localhost",port))
conn.send(h_name.encode('ascii'))
server_name=conn.recv(1024).decode('ascii')
print("********************connected**********************")
print("***YOU CAN START TYPING YOUR MESSAGE.FOR FILE SHARING ENTER <FILE_SHARE> TO ENABLE FILESHARE***")


#--------------INITIALISING CONNECTION
'''conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
h_name=input("ENTER YOUR NAME:")
port=10000
host=input("ENTER THE ADDRESS OF tHE HOST TO GET CONNECTED:")
print("**************connecting****************")
print("________________________________________")
conn.connect((host,port))
conn.send(h_name.encode('ascii'))
server_name=conn.recv(1024).decode('ascii')'''

#----------------Generating RSA
publickey,privatekey=rsa.newkeys(2048)



#--------------------AUTHENTICATION

'''user_passw=input("ENTER THE PASSWORD SENT TO YOUR MAIL : ")
conn.send(user_passw.encode('ascii'))
auth=conn.recv(1024)
if(auth==b"_________________YOU HAVE ENTERED THE WRONG PASSWORD.SESSION IS TERMINATING_________________"):
    print(auth.decode('ascii'))
    conn.close()
    sock.close()
    quit()
else:
    print("********************connected**********************")
    print("***YOU CAN START TYPING YOUR MESSAGE.FOR FILE SHARING ENTER <FILE_SHARE> TO ENABLE FILESHARE OR ENTER <quit> to QUIT***")'''



#----------------recieving RSA
print("RECIEVING")
server_public_key=conn.recv(4096)
server_public_key=rsa.key.PublicKey.load_pkcs1(server_public_key, format='DER')
print("KEY RECIEVED")

#SENDING PUBLIC KEY ------------------------------------------------>
publickey_DER=publickey.save_pkcs1(format='DER')
conn.send(publickey_DER)
print("KEY SENT")



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

            while True:
                try:
                    data = conn.recv(1024)
                    if (data == b"end"):
                        break
                    playing_stream.write(data)
                except KeyboardInterrupt:
                    break
        except KeyboardInterrupt:
            return 0'''
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
            return




def send():
    while (1):
        message = input()
        if (message == b"quit"):
            quit()
        if (message == "FILE_SHARE"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, server_public_key)
            conn.send(message)
            # thread = threading.Thread(target=file_send)
            # thread.daemon = True
            # thread.start()
            file_send()
        elif (message == "call"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, server_public_key)
            conn.send(message)
            voice()
        else:
            message_encode = message.encode('ascii')
            ciphertext = rsa.encrypt(message_encode, server_public_key)
            conn.send(ciphertext)
            print()

def file_send():
    f_name = input("***ENTER THE NAME OF THE FILE")
    filesize = os.path.getsize(f_name)
    f_name1 = f_name.encode('ascii')
    f_name1 = rsa.encrypt(f_name1, server_public_key)
    conn.send(f_name1)
    conn.send(str(filesize).encode('ascii'))
    # progress = tqdm(range(filesize), desc=f"SENDING {f_name}", unit="KB")
    with open(f_name, "rb") as fil:

        while (True):
            content = fil.read(245)
            if (not content):
                content = b"completed"
                ciphertext = rsa.encrypt(content, server_public_key)
                conn.send(ciphertext)
                print("\n SENT_SUCCESSFULLY------------------>")
                fil.close()
                break
            else:
                ciphertext = rsa.encrypt(content, server_public_key)
                conn.send(ciphertext)
            # progress.update(len(content))


#-----------------thread

thread=threading.Thread(target=send)
thread.daemon=True
thread.start()




try:
    for mess in iter(lambda :conn.recv(1024),''):
        mess = rsa.decrypt(mess, privatekey)
        if(mess=="FILE_SHARE".encode('ascii')):
            received_file_name=conn.recv(1024)
            received_file_name = rsa.decrypt(received_file_name, privatekey)
            received_file_name = received_file_name.decode('ascii')
            r_filesize=int(conn.recv(1024).decode('ascii'))
            with open(received_file_name, "wb") as fil:
                #progress = tqdm(range(r_filesize), desc=f"Receiving {recieved_file_name}", unit="KB")
                while(True):
                    r_content=conn.recv(1024)
                    r_content = rsa.decrypt(r_content, privatekey)
                    if(r_content==b"completed"):
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
            print("\n"+"    "+server_name+":"+mess.decode('ascii'))
except KeyboardInterrupt:
    conn.close()
    print("******************CONNECTION CLOSED*********************")
