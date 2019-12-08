#coding=utf-8 
import sys
import base64
import copy
import random

def SandM(X,H,N):
    bin_H=bin(H)
    Y=0
    for i in range(len(bin_H))
        Y=POW(Y,2,N)
        if(bin_H[i]==1)
            Y=(Y*X)%N
    return Y

def is_Prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  


def RSAInit(Rsa_Size):


    
    return 

def RSA_E(PlainText,E,N):
    
    return pow(PlainText,E,N)


def RSA_D(CipherText,D,N):

    return pow(CipherText,D,N)



if __name__ == "__main__":
    #輸入錯誤
    if(len(argv)!=5):
        print("Error")
        exit()
    Mode=argv[1]
    Rsa_Size=int 0
    PlainText
    CipherText
    
    if(Mode=="init")
        Rsa_Size=argv[2]
        
        print()
    if(Mode=="e")
       

        print()
    if(Mode=="d")

        print()