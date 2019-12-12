import sys
import base64
import copy
import random
import time


def encode(s):      #字串轉數字
    return ''.join([bin(ord(c)).replace('0b','')for c in s])


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def ext_gcd(a, b):
    if b == 0:
        x1 = 1
        y1 = 0
        x = x1
        y = y1
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a // b * y1
        return r, x, y
    
def power(x, y, p): #(x^y)%p 
    res = 1;        #Square-and-Multiply
    x = x % p       
    while (y > 0): 
        if (y & 1): 
            res = (res * x) % p     #Multiply
        y = y>>1
        x = (x * x) % p     #Square
    return res; 

def miillerTest(d, n): 

    a = 2 + random.randint(1, n - 4);  
    x = power(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 
  
    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True; 
  
    return False; 
def isPrime(n, k): 
    
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
 
    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 
  
    for i in range(k): 
        if (miillerTest(d, n) == False): 
            return False; 
    return True; 
  
def RSAInit(Rsa_Size):

    while True:
        random.seed(time.time())

        bin_Init_P = 1
        Si = Rsa_Size-2
        
        for i in range(Si):
            bin_Init_P = bin_Init_P * 2 + int(random.randint(0,1))  #亂數二進制數字
        bin_Init_P = bin_Init_P*2 + 1   #在二進制最前和最後加一位1 確保有到達指定位數的加密長度 和確定是奇數(偶數不會是質數)

        while (isPrime(bin_Init_P, 5) != True): #確定是奇數
            bin_Init_P = 1                      #不是的話繼續亂數重找
            for i in range(Si):
                bin_Init_P = bin_Init_P*2 + random.randint(0,1)
            bin_Init_P = bin_Init_P*2 + 1

        random.seed(time.time())
        bin_Init_Q = 1
        for i in range(Si):
            bin_Init_Q = bin_Init_Q * 2 + int(random.randint(0,1))       #亂數二進制數字
        bin_Init_Q = bin_Init_Q * 2 + 1               #在二進制最前和最後加一位1 確保有到達指定位數的加密長度 和確定是奇數(偶數不會是質數)
        while ((isPrime(bin_Init_Q, 5) != True )|(bin_Init_Q==bin_Init_P)):      #確定是奇數並且跟上一個找到的不一樣
            bin_Init_Q = 1                                                       #不是的話繼續亂數重找
            for i in range(Si):
                bin_Init_Q = bin_Init_Q*2 + random.randint(0,1)
            bin_Init_Q = bin_Init_Q*2 + 1

        n = bin_Init_P * bin_Init_Q                 #計算n
        fy = (bin_Init_P - 1) * (bin_Init_Q - 1)        #計算與n互質的整數個數

        e = 3            #選e 夠大的話選3889
        if fy > 3889:               
            e = 3889                    

        a = e           
        b = fy
        r, x, y = ext_gcd(a, b)     # 產生d

        if x > 0:               # 計算出的x不能是負數，如果是負數，說明p或q選取失敗，不是質數，要重選
            print("P : ")
            print(bin_Init_P)
            print("Q : ")
            print(bin_Init_Q)
            break

    d = x
    # 返回：   公鑰     私鑰
    return    (n, e), (n, d)
  
# 加密 m是被加密的資訊 加密成為c
def encrypt(m, n, e):
    c = power(m, e, n)
    return c

# 解密 c是密文，解密為明文m
def decrypt(c, n, d):
    m = power(c, d, n)
    return m
    
    
if __name__ == "__main__":
    
    if sys.argv[1] == "init" :
        pubkey, selfkey = RSAInit(int(sys.argv[2]))
        print("Public Key : ")
        print(pubkey[0])
        print(pubkey[1])
        print("Private Key : ")
        print(selfkey[0])
        print(selfkey[1])

    if sys.argv[1] == "E" :
        m = int(encode(sys.argv[2]),2)  #字串轉換

        print("Text Encode To : ")     #轉換結果
        print(m)
        c = encrypt(m, int(sys.argv[3]), int(sys.argv[4]))    #加密
        print("CipherText : ")              #輸出密文
        print(c)

    if sys.argv[1] == "D":
        c = int(sys.argv[2])
        d = decrypt(c,int(sys.argv[3]), int(sys.argv[4])) #解密
        print("PlainText : ")       #輸出明文
        print(d)