#!/usr/bin/env python3
from Crypto.Cipher import AES,DES,ARC4,Blowfish


class Aes():
    def __init__(self,fil):
        while (True):
            self.key = input("ENTER THE KEY : ").strip()
            self.file = fil
            self.file_name = self.file.split("\\")[-1]
            self.file_name = self.file_name.split(".")
            self.file_name = self.file_name[0].split("_")[0] + "_decrypted." + self.file_name[1]
            print(self.file_name)
            self.file=fil.split("\\")[-1]
            if (len(self.key) != 16):
                print("Key length should be 16")
            else:
                break
    def decrypt(self):
        self.crypt_AES = AES.new(self.key, AES.MODE_ECB)
        self.plain_content = []
        self.hex_content = []
        with open(self.file,"r") as fil:
            cont = fil.read().split()
        self.hex_content+=cont
        for cont in self.hex_content:
            cont = bytes.fromhex(cont)
            self.plain_content.append(self.crypt_AES.decrypt(cont).decode('ascii'))
        with open(self.file_name, "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)
class Des():
    def __init__(self,fil):
        while (True):
            self.key = input("ENTER THE KEY : ").strip()
            self.file = fil
            self.file_name = self.file.split("\\")[-1]
            self.file_name = self.file_name.split(".")
            self.file_name = self.file_name[0].split("_")[0] + "_decrypted." + self.file_name[1]
            print(self.file_name)
            self.file=fil.split("\\")[-1]
            if (len(self.key) != 16):
                print("Key length should be 16")
            else:
                break
    def decrypt(self):
        self.crypt_DES = DES.new(self.key, DES.MODE_ECB)
        self.plain_content = []
        self.hex_content = []
        with open(self.file,"r") as fil:
            cont = fil.read().split()
        self.hex_content+=cont
        for cont in self.hex_content:
            cont = bytes.fromhex(cont)
            self.plain_content.append(self.crypt_DES.decrypt(cont).decode('ascii'))
        with open(self.file_name, "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)
class RC4():
    def __init__(self,fil):
        while (True):
            self.key = input("ENTER THE KEY : ").strip()
            self.file = fil
            self.file_name = self.file.split("\\")[-1]
            self.file_name = self.file_name.split(".")
            self.file_name = self.file_name[0].split("_")[0] + "_decrypted." + self.file_name[1]
            print(self.file_name)
            self.file=fil.split("\\")[-1]
            if (len(self.key) != 16):
                print("Key length should be 16")
            else:
                break
    def decrypt(self):
        self.crypt_RC4 = ARC4.new(self.key)
        self.plain_content = []
        self.hex_content = []
        with open(self.file,"r") as fil:
            cont = fil.read().split()
        self.hex_content+=cont
        for cont in self.hex_content:
            cont = bytes.fromhex(cont)
            self.plain_content.append(self.crypt_RC4.decrypt(cont).decode('ascii'))
        with open(self.file_name, "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)

class BLOWFISH():
    def __init__(self,fil):
        while (True):
            self.key = input("ENTER THE KEY : ").strip()
            self.file = fil
            self.file_name = self.file.split("\\")[-1]
            self.file_name = self.file_name.split(".")
            self.file_name = self.file_name[0].split("_")[0] + "_decrypted." + self.file_name[1]
            print(self.file_name)
            self.file=fil.split("\\")[-1]
            if (len(self.key) != 16):
                print("Key length should be 16")
            else:
                break
    def decrypt(self):
        self.crypt_BLOWFISH = BLOWFISH.new(self.key)
        self.plain_content = []
        self.hex_content = []
        with open(self.file,"r") as fil:
            cont = fil.read().split()
        self.hex_content+=cont
        for cont in self.hex_content:
            cont = bytes.fromhex(cont)
            self.plain_content.append(self.crypt_BLOWFISH.decrypt(cont).decode('ascii'))
        with open(self.file_name, "w") as f:
            for c in self.plain_content:
                c = c[:c.index("\n")] + c[c.index("\n"):].replace(" ", "")
                f.write(c)








fil=input("Enter the  name of the file").strip()
while(True):
        type=input("ENTER THE TYPE OF DECRYPTION YOU WANT TO MAKE : ").strip()
        if(type=="AES"):
            fil = input("Enter the Name of the file : ")
            decipher_Aes=Aes(fil)
            decipher_Aes.decrypt()
            break
        elif(type=="DES"):
            fil = input("Enter the Name of the file : ")
            decipher_Des=Des(fil)
            decipher_Des.decrypt()
            break
        elif (type == "RC4"):
            fil = input("Enter the Name of the file : ")
            decipher_Rc4 = RC4(fil)
            decipher_Rc4.decrypt()
            break
        elif (type == "BLOWFISH"):
            fil = input("Enter the Name of the file : ")
            decipher_Blowfish = BLOWFISH(fil)
            decipher_Blowfish.decrypt()
            break
        else:
            print("Enter AES or DES or RC4 or BLOWFISH")



