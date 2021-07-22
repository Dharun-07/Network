#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import hashlib
from Crypto.Cipher import ARC4
from Crypto.Cipher import Blowfish

class Aes():
    def __init__(self,fil):
        while(True):
            self.key=input("ENTER THE KEY : ").strip()
            self.file=fil
            self.file_name=self.file.split("\\")[-1]
            self.file_name=self.file_name.split(".")
            self.file_name=self.file_name[0]+"_encrypted."+self.file_name[1]
            print(self.file_name)
            if(len(self.key)!=16):
                print("Key length should be 16")
            else:
                    break
    def encrypt(self):
        self.crypt_AES=AES.new(self.key,AES.MODE_ECB)
        content = []
        with open(self.file, "r") as fil:
            content += fil.readlines()
            for ind in range(len(content)):
                if (len(content[ind]) % 16 != 0):
                    while (True):
                        if (len(content[ind]) % 16 == 0):
                            break
                        else:
                            content[ind] += " "
        self.hex_content=[]
        for cont in content:
            self.crypt_AES_msg=""
            self.hex_content.append(str(self.crypt_AES.encrypt(cont).hex()))
        with open(self.file_name,"w")  as fil:
            fil.write(" ".join(self.hex_content))
        '''self.plain_content=[]
        for cont in self.hex_content:
            cont=bytes.fromhex(cont)
            self.plain_content.append(self.crypt_AES.decrypt(cont).decode('ascii'))
        print(self.hex_content)
        print(self.plain_content)
        with open("r.txt", "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)'''
        return (" ".join(self.hex_content))

class Des():
    def __init__(self,fil):
        while(True):
            self.key=input("ENTER THE KEY : ").strip()
            self.file=fil
            self.file_name=self.file.split("\\")[-1]
            self.file_name=self.file_name.split(".")
            self.file_name=self.file_name[0]+"_encrypted."+self.file_name[1]
            print(self.file_name)
            if(len(self.key)%8!=0):
                print("Key length should be multiple of 8")
            else:
                    break
    def encrypt(self):
        self.crypt_DES = DES.new(self.key, DES.MODE_ECB)
        content = []
        with open(self.file, "r") as fil:
            content += fil.readlines()
            for ind in range(len(content)):
                if (len(content[ind]) % 8 != 0):
                    while (True):
                        if (len(content[ind]) % 8 == 0):
                            break
                        else:
                            content[ind] += " "
        self.hex_content = []
        for cont in content:
            self.crypt_DES_msg = ""
            self.hex_content.append(str(self.crypt_DES.encrypt(cont).hex()))
        with open(self.file_name, "w")  as fil:
            fil.write(" ".join(self.hex_content))
        '''self.plain_content=[]
        for cont in self.hex_content:
            cont=bytes.fromhex(cont)
            self.plain_content.append(self.crypt_AES.decrypt(cont).decode('ascii'))
        print(self.hex_content)
        print(self.plain_content)
        with open("r.txt", "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)'''
        return (" ".join(self.hex_content))


class RC4():
    def __init__(self,fil):
        while(True):
            self.key=input("ENTER THE KEY : ").strip()
            self.file=fil
            self.file_name=self.file.split("\\")[-1]
            self.file_name=self.file_name.split(".")
            self.file_name=self.file_name[0]+"_encrypted."+self.file_name[1]
            print(self.file_name)
            if(len(self.key)%8!=0):
                print("Key length should be multiple of 8")
            else:
                    break
    def encrypt(self):
        self.crypt_RC4 = ARC4.new(self.key)
        content = []
        with open(self.file, "r") as fil:
            content += fil.readlines()
            for ind in range(len(content)):
                if (len(content[ind]) % 8 != 0):
                    while (True):
                        if (len(content[ind]) % 8 == 0):
                            break
                        else:
                            content[ind] += " "
        self.hex_content = []
        for cont in content:
            self.crypt_RC4_msg = ""
            self.hex_content.append(str(self.crypt_RC4.encrypt(cont).hex()))
        with open(self.file_name, "w")  as fil:
            fil.write(" ".join(self.hex_content))
        '''self.plain_content=[]
        for cont in self.hex_content:
            cont=bytes.fromhex(cont)
            self.plain_content.append(self.crypt_AES.decrypt(cont).decode('ascii'))
        print(self.hex_content)
        print(self.plain_content)
        with open("r.txt", "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)'''
        return (" ".join(self.hex_content))

class BLOWFISH():
    def __init__(self,fil):
        while(True):
            self.key=input("ENTER THE KEY : ").strip()
            self.file=fil
            self.file_name=self.file.split("\\")[-1]
            self.file_name=self.file_name.split(".")
            self.file_name=self.file_name[0]+"_encrypted."+self.file_name[1]
            print(self.file_name)
            if(len(self.key)%8!=0):
                print("Key length should be multiple of 8")
            else:
                    break
    def encrypt(self):
        self.crypt_BLOWFISH = Blowfish.new(self.key)
        content = []
        with open(self.file, "r") as fil:
            content += fil.readlines()
            for ind in range(len(content)):
                if (len(content[ind]) % 8 != 0):
                    while (True):
                        if (len(content[ind]) % 8 == 0):
                            break
                        else:
                            content[ind] += " "
        self.hex_content = []
        for cont in content:
            self.crypt_BLOWFISH_msg = ""
            self.hex_content.append(str(self.crypt_BLOWFISH.encrypt(cont).hex()))
        with open(self.file_name, "w")  as fil:
            fil.write(" ".join(self.hex_content))
        '''self.plain_content=[]
        for cont in self.hex_content:
            cont=bytes.fromhex(cont)
            self.plain_content.append(self.crypt_AES.decrypt(cont).decode('ascii'))
        print(self.hex_content)
        print(self.plain_content)
        with open("r.txt", "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)'''
        return (" ".join(self.hex_content))





mode=input("ENTER HASH OR ENCRYPTION : ").strip()
if(mode=="E"):
    while(True):
        type=input("ENTER THE TYPE OF ENCRYPTION YOU WANT TO MAKE : ").strip()
        if(type=="AES"):
            fil = input("Enter the Name of the file : ")
            cipher_Aes=Aes(fil)
            cipher_Aes.encrypt()
            break
        elif(type=="DES"):
            fil = input("Enter the Name of the file : ")
            cipher_Des=Des(fil)
            cipher_Des.encrypt()
            break
        elif (type == "RC4"):
            fil = input("Enter the Name of the file : ")
            cipher_Rc4 = RC4(fil)
            cipher_Rc4.encrypt()
            break
        elif (type == "BLOWFISH"):
            fil = input("Enter the Name of the file : ")
            cipher_Blowfish = BLOWFISH(fil)
            cipher_Blowfish.encrypt()
            break
        else:
            print("Enter AES or DES or RC4 or BLOWFISH")
elif(mode=="H"):
    fil=input("Enter the name of the file").strip()
    h_type=input("Enter the hash type preffered : ")
    if(h_type=="md5"):print(hashlib.md5(open(fil,"rb").read()).hexdigest())
    elif(h_type=="blake2s"):print(hashlib.blake2s(open(fil,"rb").read()).hexdigest())
    elif (h_type == "blake2b"):print(hashlib.blake2b(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha1"):print(hashlib.sha1(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha256"):print(hashlib.sha256(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha224"):print(hashlib.sha224(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha384"):print(hashlib.sha384(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha3_384"):print(hashlib.sha3_384(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha3_256"):print(hashlib.sha3_256(open(fil, "rb").read()).hexdigest())
    elif (h_type == "sha3_224"):print(hashlib.sha3_224(open(fil, "rb").read()).hexdigest())
else:
    print("input should be H or E")

'''from Crypto.Cipher import AES

key = 'abcdefghijklmnop'

cipher = AES.new(key, AES.MODE_ECB)
msg = cipher.encrypt('TechTutorialsX!!TechTutorialsX!!')
print(type(msg))

print(msg.hex())

decipher = AES.new(key, AES.MODE_ECB)
print(decipher.decrypt(msg))'''
'''content=[]
with open("requirements.txt","r") as fil:
    content+=fil.readlines()
    for ind in range(len(content)):
        if(len(content[ind])%16!=0):
            while(True):
                if(len(content[ind])%16==0):break
                else:content[ind]+=" "
    print(content)
with open("r.txt","w") as f:
    for c in content:
        c=c[:c.index("\n")]+c[c.index("\n"):].replace(" ","")
        f.write(c)
    print(content)'''