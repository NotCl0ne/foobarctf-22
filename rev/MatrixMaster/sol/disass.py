import struct

base = 0x3018
d = bytearray(open("matrix","rb").read()[base:base+0x90])

pc = 0
# print(d)
# print(d[2])
while pc < len(d)-2:
    print("%.2x : " % pc,end=' ')
    if(d[pc] == 0):
        print("XOR r%i, r%i\n" % (d[pc+1],d[pc+2]))
        pc+=3
        continue

    if(d[pc] == 1):
        print("AND r%i, r%i \n" % (d[pc+1],d[pc+2]))
        pc+=3
        continue

    if(d[pc] == 2):
        print("OR r%i, r%i \n" % (d[pc+1],d[pc+2]))
        pc+=3
        continue

    if(d[pc] == 3):
        print("MOV r%i, r%i \n" % (d[pc+1],d[pc+2]))
        pc+=3
        continue

    if(d[pc] == 4):
        print("MOVI r%i, 0x%.8x \n" % (d[pc+1],struct.unpack("I",d[pc+2:pc+2+4])[0]))
        pc+=6
        continue
    if(d[pc] == 5):
        print("LEFT r%i, 0x%.8x \n" % (d[pc+1],struct.unpack("I",d[pc+2:pc+2+4])[0]))
        pc+=6
        continue
    if(d[pc] == 6):
        print("RIGHT r%i, 0x%.8x \n" % (d[pc+1],struct.unpack("I",d[pc+2:pc+2+4])[0]))
        pc+=6
        continue
    if(d[pc] == 0xfc):
        print("Add r%i, 0x%.8x \n" % (d[pc+1],struct.unpack("I",d[pc+2:pc+2+4])[0]))
        pc+=6
        continue
    if(d[pc] == 0xfd):
        print("Sub r%i, 0x%.8x \n" % (d[pc+1],struct.unpack("I",d[pc+2:pc+2+4])[0]))
        pc+=6
        continue
    if(d[pc] == 0xfe):
        print("Rand r%i, 0x%.8x \n" % (d[pc+1],struct.unpack("I",d[pc+2:pc+2+4])[0]))
        pc+=6
        continue
    else :
        print("")
        pc+=1
        continue
