import sys
import base64
import copy
import random
import time
import hashlib import sha1

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
  
def DSAInit():
    q = random.getrandbits(160)
    while(True):
            if(isPrime(q,5)):
                break
            q = random.getrandbits(160) 
    k = random.getrandbits(1024 - 160)

    while(True):
            p = k * q + 1
            if(isPrime(p,5) and p.bit_length()==1024):
                break
            k = random.getrandbits(1024 - 160)
    d = random.randint(1,q)
    h = random.randint(1,p)
    A = power(h, k ,p)
    B = power(A, d, p)
    return   p, q, A, B, d

def modinv(a, m):
    g, x, y =ext_gcd(a, m)
    if g != 1:
        raise Exception("INV ERROR")  
    else:
        return x % m
    
if __name__ == "__main__":
    
    if sys.argv[1] == "keygen" :
        P, Q, A, B, D = DSAInit()
        print("Public Key : ")
        print("P : ")
        print(P)
        print("Q : ")
        print(Q)
        print("A : ")
        print(A)
        print("B : ")
        print(B)
        print("Private Key : ")
        print("D : ")
        print(D)

    if sys.argv[1] == "sign" :
        m = int(encode(sys.argv[2]),2)  #字串轉換
        print("Text Encode To : ")     #轉換結果
        print(m)
        P=sys.argv[3]
        Q=sys.argv[4]
        A=sys.argv[5]
        B=sys.argv[6]
        D=sys.argv[7]

        Ke = random.randint(0, Q)
        KeInv= modinv(Ke, Q)
        r = power(A, Ke, P) % Q
        Sha = sha1(m).hexdigest()
        s = []
        for c in SHA:
            temp = ((ord(c) + D * r) * keinv) % Q
            s.append(temp)

        print("Sign : ")
        print("M",m)
        print("r",r)
        print("s",s)

    if sys.argv[1] == "verify":

        M = int(sys.argv[2])
        R = sys.argv[3]
        S = sys.argv[4]
        #sign info
        P = sys.argv[5]
        Q = sys.argv[6]
        A = sys.argv[7]
        B = sys.argv[8]

        v= [] 
        for i in range(len(S)):
            w = modinv(S[i],q)
            p1 = (w * ord(sha1(m).hexdigest())) % Q
            p2 = (w * R) % Q
            a = (power(A,p1,P)*power(B,p2,P))
            v.append(a)

        NOTYOU = False
        for _v in v:
            if(_v % Q != R):
                NOTYOU = True
                print("DSA Verify invalid")
        if(not NOTYOU):
            print("DSA Verify valid")
