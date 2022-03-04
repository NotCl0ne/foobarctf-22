from pwn import *
from Crypto.Util.number import *
from math import  prod


#p = remote('localhost',1234)
p = process('./server.py')

#TOKEN = b'd4r3d3v!l'
# factor of bytes_to_long()

f = [2, 2, 175143733 , 2638480856911]


def getkey():
    p.sendlineafter('> ','P')
    x = p.recvuntil('\n\n').decode().strip()
    y = x.split()
    return int(y[-1],16)


def sign(m):
    p.sendlineafter('> ','S')
    p.sendlineafter('sign : ',str(m))
    x = p.recvuntil('\n\n').decode().strip()
    y = x.split()
    return int(y[-1],16)

def verify(m,s):
    p.sendlineafter('> ','V')
    p.sendlineafter('msg : ',str(m))
    p.sendlineafter('signature : ',str(s))
    return p.recvline().decode()


print('h4x0rrrr ....')

n = getkey()
si = []
for i in range(len(f)):
    s = sign(long_to_bytes(f[i]).hex())
    si.append(s)



signature = prod(si) % n
x = b'd4r3d3v!l'.hex()
y = long_to_bytes(signature).hex()
print(verify(x,y))

p.close()
