import sys
import base64
import copy
import random
import time

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

# 生成公鑰私鑰，p、q為兩個超大質數
def gen_key(p, q):
    n = p * q
    fy = (p - 1) * (q - 1)      # 計算與n互質的整數個數 尤拉函式
    e = 3889                    # 選取e   一般選取65537
    # e=3
    # generate d
    a = e
    b = fy
    r, x, y = ext_gcd(a, b)
    print(x)   # 計算出的x不能是負數，如果是負數，說明p、q、e選取失敗，一般情況下e選取65537
    d = x
    # 返回：   公鑰     私鑰
    return    (n, e), (n, d)
    
def power(x, y, p): #(x^y)%p 
    res = 1;        #Square-and-Multiply
    x = x % p       
    while (y > 0): 
        if (y & 1): 
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p 
    return res; 

def miillerTest(d, n): 
      
    # Pick a random number in [2..n-2] 
    # Corner cases make sure that n > 4 
    a = 2 + random.randint(1, n - 4); 
  
    # Compute a^d % n 
    x = power(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 
  
    # Keep squaring x while one  
    # of the following doesn't  
    # happen 
    # (i) d does not reach n-1 
    # (ii) (x^2) % n is not 1 
    # (iii) (x^2) % n is not n-1 
    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True; 
  
    # Return composite 
    return False; 
  
# It returns false if n is  
# composite and returns true if n 
# is probably prime. k is an  
# input parameter that determines 
# accuracy level. Higher value of  
# k indicates more accuracy. 
def isPrime(n, k): 
      
    # Corner cases 
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
  
    # Find r such that n =  
    # 2^d * r + 1 for some r >= 1 
    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 
  
    # Iterate given nber of 'k' times 
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
            bin_Init_P = bin_Init_P * 2 + int(random.randint(0,1))
        bin_Init_P = bin_Init_P*2 + 1

        while (isPrime(bin_Init_P, 5) != True):
            bin_Init_P = 1
            for i in range(Si):
                bin_Init_P = bin_Init_P*2 + random.randint(0,1)
            bin_Init_P = bin_Init_P*2 + 1

        random.seed(time.time())
        bin_Init_Q = 1
        for i in range(Si):
            bin_Init_Q = bin_Init_Q * 2 + int(random.randint(0,1))
        bin_Init_Q = bin_Init_Q * 2 + 1
        while ((isPrime(bin_Init_Q, 5) != True )|(bin_Init_Q==bin_Init_P)):
            bin_Init_Q = 1
            for i in range(Si):
                bin_Init_Q = bin_Init_Q*2 + random.randint(0,1)
            bin_Init_Q = bin_Init_Q*2 + 1

        n = bin_Init_P * bin_Init_Q
        fy = (bin_Init_P - 1) * (bin_Init_Q - 1)      # 計算與n互質的整數個數 尤拉函式
        e = 3
        if fy > 3889:
            e = 3889                    # 選取e   一般選取65537
        # e=3
        # generate d
        a = e
        b = fy
        r, x, y = ext_gcd(a, b)

        if x > 0:
            print("P : ")
            print(bin_Init_P)
            print("Q : ")
            print(bin_Init_Q)
            break

    #print(x)   # 計算出的x不能是負數，如果是負數，說明p、q、e選取失敗，一般情況下e選取65537
    d = x
    # 返回：   公鑰     私鑰
    return    (n, e), (n, d)
    #return bin_Init_P , bin_Init_Q
  
# 加密 m是被加密的資訊 加密成為c
def encrypt(m, pubkey):
    n = pubkey[0]
    e = pubkey[1]
    c = power(m, e, n)
    return c

# 解密 c是密文，解密為明文m
def decrypt(c, selfkey):
    n = selfkey[0]
    d = selfkey[1]
    m = power(c, d, n)
    return m
    
    
if __name__ == "__main__":
    
    '''生成公鑰私鑰'''
    #pubkey, selfkey = gen_key(p, q)
    pubkey, selfkey = RSAInit(int(sys.argv[1]))
    
    '''需要被加密的資訊轉化成數字，長度小於祕鑰n的長度，如果資訊長度大於n的長度，那麼分段進行加密，分段解密即可。'''
    #m = "abc123"
    print("N : ")
    print(pubkey[0])
    print("E : ")
    print(pubkey[1])
    print("D : ")
    print(selfkey[1])

    #m=int(bin(m)[2:])
    m=int(sys.argv[2])
    '''資訊加密'''
    
    c = encrypt(m, pubkey)
    print("CipherText : ")
    print(c)

    '''資訊解密'''
    d = decrypt(c, selfkey)
    print("PlainText : ")
    print(d)