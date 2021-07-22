#!/usr/bin/env python3
import socket
import threading
import os, time, sys
import random
import string
import ssl, smtplib
import rsa
import pyaudio
import pyfiglet
from termcolor import colored


def start_animation(msg):
    load_str = msg
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0
    print()
    while (counttime != 100):

        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        res = ''

        for j in range(ls_len):
            res = res + load_str_list[j]

        sys.stdout.write("\r" + animation[anicount] + res + animation[anicount])
        sys.stdout.flush()

        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

    print()


def HELP():
    print()
    GType(colored(""" 
        Type 'FILE_SHARE' for sharing files\n
        Type 'call' for enable voice call\n
        Type 'quit' to exit the application\n 
        """, color='green'))


def GType(msg):
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.065)


def Withinp(msg):
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.065)

    k = input()
    return k


start_animation("starting secure chat application")
os.system('clear')
print((colored(pyfiglet.figlet_format("\tSecureChat", font='slant', justify='center'), color='green')))
print((colored("\t" + '-' * 60, color='green')))
print((colored("\t[-] Secure Chat", color='green')))
print((colored("\t[-] Built By -- @DharunKrishna @SaiKrishnan @Vignesh", color='green')))
print((colored("\t[-] Run 'pip install -r requirements.txt To install the dependencies", color='green')))
print((colored("\t" + '-' * 60, color='green')))
print()



context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/home/kali/Downloads/newcert2.pem', '/home/kali/Downloads/newkey2.pem')

ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock = context.wrap_socket(ssock, server_side=True)

start_animation("        initialising ssl connection     ")
name = Withinp(colored("[+]ENTER YOUR NAME:", color='yellow'))
port = 10000
host = "0.0.0.0"
h_name = socket.gethostname()
h_addr = socket.gethostbyname("localhost")
h_addr = colored(h_addr, color='blue')
GType(colored("THE SERVER HAS GOT ADDRESS ---->{}", color='yellow').format(h_addr))
print()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()
start_animation("          connecting         ")
print()
client_name = conn.recv(1204).decode()
client_name = colored(client_name, color='blue')
conn.send(name.encode('ascii'))
GType(colored("Connected to ------------>{}", color='yellow').format(client_name))
print()
GType(colored("---------------WAIT FOR THE BANNER AND YOU CAN START TYPING-----------------", color='green'))
print()
# -------------INITIALISING CONNEcTION

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

# start_animation("             generating rsa         ")

publickey, privatekey = rsa.newkeys(2048)

# ----------------GENERATING PASSW

strings = string.printable
strings = strings.replace(" ", "")
char = string.ascii_uppercase + string.digits + string.ascii_lowercase + strings
passw = ""
for i in range(15):
    passw += random.choice(char)

# --------------SENDING EMAIL

def read_cred():
    user = password = ''
    with open("cred.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        password = file[1].strip()

    return user, password


sender, password = read_cred()

receiver = "securechat101@gmail.com"

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
    print("***YOU CAN START TYPING YOUR MESSAGE.FOR FILE SHARING ENTER <FILE_SHARE> TO ENABLE FILESHARE OR ENTER <quit> to QUIT***")

# start_animation("                sending public key             ")
publickey_DER = publickey.save_pkcs1(format='DER')
conn.send(publickey_DER)
# GType(colored("KEY SENT",color='yellow'))

# start_animation("                recieving RSA                  ")
# print("RECIEVING")
client_public_key = conn.recv(4096)
client_public_key = rsa.key.PublicKey.load_pkcs1(client_public_key, format='DER')
# GType(colored("KEY RECIEVED",color='yellow'))
start_animation("                   STARTED                    ")
HELP()
GType(colored("YOU CAN START TYPING YOUR MESSAGE OR TYPE HELP FOR FEATURES", color='yellow'))


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

def HELP():
    print()
    GType(colored(""" 
        Type 'FILE_SHARE' for sharing files\n
        Type 'call' for enable voice call\n
        Type 'quit' to exit the application\n 
        """, color='green'))


def send():
    while (1):
        message = input()
        if (message == "quit"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, client_public_key)
            conn.send(message)
            conn.close()
            GType(colored("---------------------CONNECTION CLOSED---------------------", color='yellow'))
            quit()
        if (message == "FILE_SHARE"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, client_public_key)
            conn.send(message)
            # thread = threading.Thread(target=file_send)
            # thread.daemon = True
            # thread.start()
            file_send()
        elif (message == "call"):
            message = message.encode('ascii')
            message = rsa.encrypt(message, client_public_key)
            conn.send(message)
            voice()
        elif (message == 'HELP'):
            HELP()
        else:
            message_encode = message.encode('ascii')
            ciphertext = rsa.encrypt(message_encode, client_public_key)
            conn.send(ciphertext)
            print()


def file_send():
    f_name = Withinp(colored("[+]ENTER THE NAME OF THE FILE:", color='yellow'))
    filesize = os.path.getsize(f_name)
    f_name1 = f_name.encode('ascii')
    f_name1 = rsa.encrypt(f_name1, client_public_key)
    conn.send(f_name1)
    conn.send(str(filesize).encode('ascii'))
    # progress = tqdm(range(filesize), desc=f"SENDING {f_name}", unit="KB")
    with open(f_name, "rb") as fil:

        while (True):
            content = fil.read(245)
            if (not content):
                content = b"completed"
                ciphertext = rsa.encrypt(content, client_public_key)
                conn.send(ciphertext)
                GType(colored("\n -----SENT {} SUCCESSFULLY-----", color='yellow').format(f_name))
                fil.close()
                break
            else:
                ciphertext = rsa.encrypt(content, client_public_key)
                conn.send(ciphertext)
            # progress.update(len(content))


thread = threading.Thread(target=send)
thread.daemon = True
thread.start()

try:
    for mess in iter(lambda: conn.recv(1029), ''):
        mess = rsa.decrypt(mess, privatekey)
        if (mess == "FILE_SHARE".encode('ascii')):
            received_file_name = conn.recv(1024)
            received_file_name = rsa.decrypt(received_file_name, privatekey)
            received_file_name = received_file_name.decode('ascii')
            #received_file_name = colored(received_file_name, color='blue')
            r_filesize = int(conn.recv(1024).decode('ascii'))
            with open(received_file_name, "wb") as fil:
                # progress = tqdm(range(r_filesize), desc=f"Receiving {recieved_file_name}", unit="KB")
                while (True):
                    r_content = conn.recv(1024)
                    r_content = rsa.decrypt(r_content, privatekey)
                    if (r_content == b"completed"):
                        GType(colored("RECEIVED FILE ----->{}", color='yellow').format(received_file_name))
                        fil.close()
                        # progress.update(len(r_content))
                        break
                    else:
                        fil.write(r_content)
                    # progress.update(len(r_content))
        elif (mess == "call".encode('ascii')):
            voice()
        elif (mess == "quit".encode('ascii')):
            conn.close()
            GType(colored("---------------------CONNECTION CLOSED---------------------", color='yellow'))
        else:
            print("\n" + "    " + client_name + ":" + str(mess.decode('ascii')))
except KeyboardInterrupt:
    conn.close()
    GType(colored("---------------------CONNECTION CLOSED---------------------", color='yellow'))