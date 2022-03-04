from Crypto.Util.number import getPrime, bytes_to_long, GCD
from sage.all_cmdline import kronecker_symbol, randint

flag = bytes_to_long(b"GLUG{Qu4dr471C_R351dU35_4R3_fun_0r_4r3_7h3y}")

p = getPrime(1024)
q = getPrime(1024)
N= p*q
e = 0x10001
c = pow(flag, e , N)
enc_pq = []
bin_p = bin(p)[2:]
bin_q = bin(q)[2:]
x = randint(1,N)
while(kronecker_symbol(x, N) == 1):
	x = randint(1,N)

for i in range(512):
        while True:
            r = randint(1, N)
            if GCD(r, N) == 1:
                bin_r = bin(r)[2:]
                p_bit = (pow(x, int(bin_r + bin_p[i], 2), N) * r ** 2) % N

                enc_pq.append(p_bit)
                break
for i in range(512):
        while True:
            r = randint(1, N)
            if GCD(r, N) == 1:
                bin_r = bin(r)[2:]
                q_bit = (pow(x, int(bin_r + bin_q[512+i], 2), N) * r ** 2) % N
                enc_pq.append(q_bit)
                break

f = open("Confidential_Output.txt", "w")
f.write(f"{flag = }\n")
f.write(f"{N = }\n")
f.write(f"{p = }\n")
f.write(f"{q = }\n")
f.write(f"{e = }\n")
f.write(f"{c = }\n")
f.write(f"{x = }\n")
f.write(f"{enc_pq = }\n")
f.close()

f = open("Output.txt", "w")
f.write(f"{N = }\n")
f.write(f"{e = }\n")
f.write(f"{c = }\n")
f.write(f"{x = }\n")
f.write(f"{enc_pq = }\n")
f.close()
