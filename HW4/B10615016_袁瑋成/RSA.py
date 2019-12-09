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
# Utility function to do 
# modular exponentiation. 
# It returns (x^y) % p 
def power(x, y, p): 
      
    # Initialize result 
    res = 1;  
      
    # Update x if it is more than or 
    # equal to p 
    x = x % p;  
    while (y > 0): 
          
        # If y is odd, multiply 
        # x with result 
        if (y & 1): 
            res = (res * x) % p; 
  
        # y must be even now 
        y = y>>1; # y = y/2 
        x = (x * x) % p; 
      
    return res; 
  
# This function is called 
# for all k trials. It returns 
# false if n is composite and  
# returns false if n is 
# probably prime. d is an odd  
# number such that d*2<sup>r</sup> = n-1 
# for some r >= 1 
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
    bin_Init_P = 1
    for i in range (Rsa_Size-2)
        bin_Init_P*2 + random.randint(0,1))
    bin_Init_P = bin_Init_P*2 + 1
    while(isPrime(bin_Init_P, 4)!=true)
        bin_Init_P = 1
        for i in range (Rsa_Size-2)
            bin_Init_P*2 + random.randint(0,1))
        bin_Init_P = bin_Init_P*2 + 1
    
    bin_Init_Q = 1
    for i in range (Rsa_Size-2)
        bin_Init_Q*2 + random.randint(0,1))
    bin_Init_Q = bin_Init_Q*2 + 1
    while(isPrime(bin_Init_Q, 4)!=true)
        bin_Init_Q = 1
        for i in range (Rsa_Size-2)
            bin_Init_Q*2 + random.randint(0,1))
        bin_Init_Q = bin_Init_Q*2 + 1
    if(bin_Init_P!=bin_Init_Q)
        



    
    return -1

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