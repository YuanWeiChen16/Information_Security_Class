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
        to_return = self
        datas_bin_origin = self.data_bin
        to_return.data_bin=bytes()#創一個PPM檔
        cipherblock =bytes()#密文
        for i in range(int(len(datas_bin_origin)/16)) :
            block = datas_bin_origin[16*i:16*i+16]#將每一個block的資料拿出來
            cipherblock += AES_encrypt_block(block,key)#對每一個block加密
        to_return.data_bin += cipherblock#將PPM檔開頭和密文和在一起
        return to_return

    #ECB解密
    def ECBDecrypt(self,key):
        self.data_bin = pad(self.data_bin)#不足時先補齊
        to_return = self
        datas_bin_origin = self.data_bin
        to_return.data_bin=bytes()#創一個PPM檔
        plainblock = bytes()#明文
        for i in range(int(len(datas_bin_origin)/16)) :
            block = datas_bin_origin[16*i:16*i+16]#將每一個block的資料拿出來
            plainblock += AES_decrypt_block(block,key)#對每一個block解密
        to_return.data_bin += plainblock#將PPM檔開頭和明文和在一起
        return to_return

    #CBC加密
    def CBCEncrypt(self,key):
        self.data_bin = pad(self.data_bin))#不足時先補齊
        to_return = copy.copy(self)
        to_return.data_bin=bytes()#創一個PPM檔
        processed_block=bytes()#密文
        Initvector = key[0:16]#init vector??
        for i in range(int(len(self.data_bin)/16)) :
            block=self.data_bin[16*i:16*i+16]
            block = bytes_xor(block,vector)#CBC先跟IV互斥或再運算
            processed_block = AES_encrypt_block(block,key)#對每一個block加密
            vector = processed_block#加密輸出當下一次的解密
        to_return.data_bin+=processed_block
        return to_return


    def CBCDecrypt(self,key):
         self.data_bin = pad(self.data_bin)
        to_return = copy.copy(self)
        to_return.data_bin=bytes()
        processed_block=bytes()
        vector = key[0:16]
        for i in range(int(len(self.data_bin)/16)) :
            block=self.data_bin[16*i:16*i+16]
            processed_block = AES_decrypt_block(block,key)
            processed_block = bytes_xor(processed_block,vector)
            vector = block
           to_return.data_bin+=processed_block
        return to_return

if __name__ == "__main__":
    # argv=[hw3.py, filepath, encrypt/decrypt, mode, key]
    if(len(argv)!=6):
        print("Arguments error")
        exit()
    Inimg = Image.open(argv[1])
    PPMimg=Inimg[:-4]+".ppm"
    Inimg.save(PPMimg)
    Inimg.close()
    PPM=open(PPMimg, 'rb')

    with Image.open(input_png_path) as input_png_file :
        input_ppm_path = input_png_path[:-4]+".ppm"
        input_png_file.save(input_ppm_path)
    
    key=0
    NPPM=AESCipher(PPM)

    


    im=Image.open("./asda.ppm")
    im.save("./Output.png")
    PPM.close()
main()