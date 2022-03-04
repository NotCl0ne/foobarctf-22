from Crypto.Util.number import *
import math
from functools import reduce
from gmpy2 import gcd

N =  85613323906917847391199462614421376844553083828748771301593911566433402937203323225240937472007562579427333998909849114887824397637818070051023945356833323031295346898454059510575760942622087273744830539310771816124298898520237849421467436716663064093452683147524125851771171662824045900720704191342361141393
S =  3763993866191919935910240797450849942552039383644696213944727739885620179204953014936120594075485788948333698
def solve(f,S):
    y = []
    for i in f[::-1]:
        if S>= i:
            y.append("1")
            S -= i
        else:
            y.append("0")
    return str(''.join(y)[::-1])


f = [2]
x = 2
for i in range(359):
    x = 2 * x + 1
    f.append(x)
    
c2 = solve(f,S)


block_size=int(math.log(int(math.log(N,2)),2))
assert len(c2) % block_size == 0

r = 89657896589
x = pow(r,2,N)
m = ''
for i in range(0, len(c2), block_size):
    x = pow(x,2,N)
    c = int(c2[i:i+block_size], 2)
    p = int(bin(x)[2:][-block_size:],2)
    m += format(c ^ p, '0' + str(block_size) + 'b')

print(long_to_bytes(int(m, 2)).decode())

#x = math.log(s+1//3,2)