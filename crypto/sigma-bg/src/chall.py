#!/usr/bin/env python3

from Crypto.Util.number import *
import math

flag = b'GLUG{lif3_1s_n0_N1n7end0_g4m3_JSYN1HEKMF}'

def S2B(s):
    return ''.join(bin(ord(i))[2:].zfill(8) for i in s)

def keygen(bits):
    while True:
        p,q = getPrime(bits),getPrime(bits)
        if (p % 4 == 3) and (q % 4 == 3 ) and (p != q):
            n = p * q
            break
    return n

def keygen2():
    M = [2]
    x = 2
    for i in range(len((C))):
        x = 2 * x + 1
        M.append(x)
    return M

def encrypt1(m,h,n):
    while len(m)%h!=0:
        m = '0'+ m
    l = len(m) // h
    r = 89657896589
    x=pow(r,2,n)
    C = ''
    for i in range(l):
        x = pow(x,2,n)
        p_i = (bin(x)[2:])[-h:]
        c_i = int(p_i,2)^int(m[i*h:(i+1)*h],2)
        cx = bin(c_i)[2:].zfill(h)
        C+=cx
    return C


def encrypt2(C, M):
    S = 0
    for x, m in zip(C, M):
        S += int(x) * m
    return S

n = keygen(512)
h = int(math.log(int(math.log(n,2)),2))
m = ''.join(bin(ord(i))[2:].zfill(8) for i in str(flag))
C = encrypt1(m,h,n)
M = keygen2()
S = encrypt2(C,M)

print("n =  {}".format(n))
print("S =  {}".format(S))

