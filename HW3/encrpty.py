#coding=utf-8 
from PIL import Image
import sys
from Crypto.Cipher import AES
import base64
import copy

#pad 使用PKCS
def pad(text):
	padding = 16 - (len(text) % 16)
	return text + bytes([padding] * padding)#補齊不足的

#unpad 使用PKCS
def unpad(text):
	padding = text[-1]
	return text[:-padding]#刪掉多餘的

#兩個大bytes的互斥或
def bytes_xor(bytesL, bytesR):
    parts = []
    for bytesL, bytesR in zip(bytesL, bytesR):
        parts.append(bytes([bytesL ^ bytesR]))
    return b''.join(parts)

#AES加密單個block(使用套件)
def AES_encrypt_block(plain,key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain)
    return ciphertext

#AES解密單個block(使用套件)
def AES_decrypt_block(cipher,key):
    plain = AES.new(key, AES.MODE_ECB)
    plaintext = plain.decrypt(cipher)
    return plaintext

class AESCipher():
    #PPM初始化紀錄圖片型態(P6)大小(pixel)顏色範圍(256)和資料
    def __init__( self,PPM_Text ):
        self.PPMType=PPM_Text.readline()
        string=PPM_Text.readline()
        self.Range=int(PPM_Text.readline())
        self.SizeX=int(string.split()[0])
        self.SizeY=int(string.split()[1])
        self.data_bin=PPM_Text.read()

    #創建一個PPM檔的開頭
    def __bytes__(self):   
        NewPPM = bytes("P6\n","utf-8")+bytes(str(self.SizeX),'utf-8')+bytes(" ","utf-8")+bytes(str(self.SizeY),'utf-8')+bytes("\n","utf-8")+bytes(str(self.range),'utf-8')+bytes("\n","utf-8")+self.pixels_bin
        return NewPPM

    #用ECB加密
    def ECBEncrypt(self,key):
        self.data_bin = pad(self.data_bin)#不足時先補齊
        ECBEncrypt_return = self
        origin = self.data_bin
        ECBEncrypt_return.data_bin=bytes()#創一個PPM檔
        cipherblock =bytes()#密文
        for i in range(int(len(origin)/16)) :
            block = origin[16*i:16*i+16]#將每一個block的資料拿出來
            cipherblock += AES_encrypt_block(block,key)#對每一個block加密
        ECBEncrypt_return.data_bin += cipherblock#將PPM檔開頭和密文和在一起
        return ECBEncrypt_return

    #ECB解密
    def ECBDecrypt(self,key):
        self.data_bin = pad(self.data_bin)#不足時先補齊
        ECBDecrypt_return = self
        origin = self.data_bin
        ECBDecrypt_return.data_bin=bytes()#創一個PPM檔
        plainblock = bytes()#明文
        for i in range(int(len(origin)/16)) :
            block = origin[16*i:16*i+16]#將每一個block的資料拿出來
            plainblock += AES_decrypt_block(block,key)#對每一個block解密
        ECBDecrypt_return.data_bin += plainblock#將PPM檔開頭和明文和在一起
        return ECBDecrypt_return

    #CBC加密
    def CBCEncrypt(self,key):
        Ivector = key[0:16]#init vector
        self.data_bin = pad(self.data_bin))#不足時先補齊
        CBCEncrypt_return = copy.copy(self)
        CBCEncrypt_return.data_bin=bytes()#創一個PPM檔
        tempblock=bytes()#密文
        for i in range(int(len(self.data_bin)/16)) :
            block=self.data_bin[16*i:16*i+16]#選出要計算的block
            block = bytes_xor(block,Ivector)#先跟IV互斥或再運算
            tempblock = AES_encrypt_block(block,key)#對每一個block加密
            Ivector = tempblock#加密輸出當下一次的解密
        CBCEncrypt_return.data_bin+=tempblock
        return CBCEncrypt_return

    #CBC解密
    def CBCDecrypt(self,key):
        Ivector = key[0:16]#init vector
        self.data_bin = pad(self.data_bin)#不足時先補齊
        CBCDecrypt_return = copy.copy(self)
        CBCDecrypt_return.data_bin=bytes()#創PPM檔
        tempblock=bytes()#明文
        for i in range(int(len(self.data_bin)/16)) :
            block=self.data_bin[16*i:16*i+16]#選出要計算的block
            tempblock = AES_decrypt_block(block,key)#對每一個block解密
            tempblock = bytes_xor(tempblock,Ivector)#跟IV互斥或
            Ivector = block
        CBCDecrypt_return.data_bin+=tempblock
        return CBCDecrypt_return

    #cool加密
    def CoolEncrypt(self,key):
        self.data_bin=pad(self.data_bin)
        ECBEncrypt_return = self
        origin = self.data_bin
        ECBEncrypt_return.data_bin=bytes()#創一個PPM檔
        cipherblock =bytes()#密文
        for i in range(int(len(origin)/16)) :
            block = origin[16*i:16*i+16]#將每一個block的資料拿出來
            block = bytes_xor(block,key)#先跟key互斥或
            block = AES_encrypt_block(block,key)#對每一個block加密
            cipherblock+= bytes_xor(block,key)#後跟key互斥或
        ECBEncrypt_return.data_bin += cipherblock#將PPM檔開頭和密文和在一起
        return ECBEncrypt_return

    #cool解密
    def CoolDecrypt(self,key):
        self.data_bin = pad(self.data_bin)#不足時先補齊
        ECBDecrypt_return = self
        origin = self.data_bin
        ECBDecrypt_return.data_bin=bytes()#創一個PPM檔
        plainblock = bytes()#明文
        for i in range(int(len(origin)/16)) :
            block = origin[16*i:16*i+16]#將每一個block的資料拿出來
            block = bytes_xor(block,key)#先跟key互斥或
            block = AES_decrypt_block(block,key)#對每一個block解密
            plainblock+= bytes_xor(block,key)#後跟key互斥或
        ECBDecrypt_return.data_bin += plainblock#將PPM檔開頭和明文和在一起
        return ECBDecrypt_return


if __name__ == "__main__":
    #輸入錯誤
    if(len(argv)!=5):
        print("Error")
        exit()
    #開png圖片檔
    InputName=argv[1]
    Inimg = Image.open(InputName)
    PPMimg = InputName[:-4]+".ppm"
    Inimg.save(PPMimg)#存成PPM檔
    Inimg.close()
    PPM=open(PPMimg, 'rb')#開起PPM檔
    EN_DE=argv[2]
    Mode = argv[3]
    KEY=bytes.fromhex(argv[4])
    NPPM=AESCipher(PPM)
    #模式判斷
    if(Mode=="ECB")
        if(EN_DE=="encrypt")
            NPPM=NPPM.ECBEncrypt(KEY)
        if(EN_DE=="decrypt")
            NPPM=NPPM.ECBDecrypt(KEY)
    if(Mode=="CBC")
        if(EN_DE=="encrypt")
            NPPM=NPPM.CBCEncrypt(KEY)
        if(EN_DE=="decrypt")
            NPPM=NPPM.CBCDecrypt(KEY)
    if(Mode=="Cool")
        if(EN_DE=="encrypt")
            NPPM=NPPM.CoolEncrypt(KEY)
        if(EN_DE=="decrypt")
            NPPM=NPPM.CoolDecrypt(KEY)
    #寫回圖片檔
    PPM.close()
    OUTPPM=open(PPMimg, 'Wb')#開起PPM檔
    OUTPPM.write(bytes(NPPM))   #寫入新資料
    OUTPPM.close()

    OUTPng=Image.open(PPMimg)   #用Image開檔(存成png)
    Pngimg=PPMimg[:-4]+"_output.png"#png路徑
    OUTPng.save(Pngimg) #存成png
    OUTPng.close()
  