from Crypto.Util.number import *

flag = b"GLUG{ded1cati0n_i5_4_tal3n7_4ll_0n_it5_0wn}"

p,q = getPrime(1024),getPrime(1024)

print(p)
print(q)

N = p * p * q
e = 0x10001

phi = p * (p-1) * (q-1)

d = inverse(e, phi)
m = bytes_to_long(flag)

ct = pow(m, e, N)

assert pow(ct, d, N) == m

x = (p * q) % 2**1337

print("N =  {}".format(N))
print("e =  {}".format(e))
print("ct =  {}".format(ct))
print("x =  {}".format(x))


