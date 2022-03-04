
#python2
#pip install z3

from z3 import *

flag_start = flag{"
flag_end = "}"
len_flag = 42

s = Solver()
#initiate instances
x=[]
for i in range(0,len_flag):
    x.append(Int('x'+str(i)))

#add printable ASCII contraints to solver
for i in range(0,len_flag):
    s.add( x[i] >= 32 )
    s.add( x[i] < 127 )

#add known components of flag
def addKnown(s, x, flag_start, flag_end):
    for i in range(0, len(flag_start)):
        s.add( x[i] == ord(flag_start[i]))

    for i in range(0, len(flag_end)):
        s.add( x[len(x)-len(flag_end) + i] == ord(flag_end[i]))

addKnown(s,x,flag_start, flag_end)
s.add(x[13]+x[7]+x[8]==269)
s.add(x[0]-x[1]+x[14]+x[0]==165)
s.add(x[21]*x[16]+x[34]+x[38]==9482)
s.add(x[41]+x[8]*x[6]+x[23]==5500)
s.add(x[30]-x[30]-x[41]-x[21]==-223)
s.add(x[18]*x[4]*x[11]+x[19]==639710)
s.add(x[23]+x[33]*x[34]==6403)
s.add(x[18]*x[14]-x[33]==5072)
s.add(x[24]-x[39]-x[30]-x[22]==-110)
s.add(x[30]+x[10]-x[19]+x[1]==110)
s.add(x[15]-x[20]-x[41]==-169)
s.add(x[15]*x[35]-x[41]*x[8]==-10231)
s.add(x[11]*x[31]+x[36]-x[32]==8428)
s.add(x[25]+x[29]+x[40]==289)
s.add(x[7]-x[12]+x[24]==100)
s.add(x[21]*x[30]-x[6]==9262)
s.add(x[33]*x[38]*x[3]==480244)
s.add(x[20]-x[31]*x[0]-x[2]==-5954)
s.add(x[27]+x[12]*x[21]==5095)
s.add(x[6]+x[11]*x[8]-x[8]==10938)
s.add(x[34]-x[5]+x[7]*x[24]==5014)
s.add(x[40]-x[18]-x[2]==-83)
s.add(x[11]-x[31]+x[9]*x[24]==10114)
s.add(x[7]-x[7]-x[41]==-125)
s.add(x[28]+x[30]-x[16]*x[3]==-6543)
s.add(x[18]*x[25]-x[11]==5828)
s.add(x[9]*x[8]*x[11]==1089000)
s.add(x[3]*x[25]-x[29]*x[6]==2286)
s.add(x[36]-x[7]*x[33]==-3642)
s.add(x[32]-x[1]+x[20]==73)
s.add(x[39]+x[5]*x[4]==8307)
s.add(x[39]*x[0]*x[8]==515460)
s.add(x[12]-x[13]+x[31]==25)
s.add(x[41]+x[10]+x[18]+x[41]==351)
s.add(x[1]*x[14]+x[7]+x[22]==7624)
s.add(x[18]*x[24]+x[27]+x[14]==5500)
s.add(x[20]-x[41]*x[6]+x[18]==-5853)
s.add(x[33]-x[2]-x[31]*x[25]==-9585)
s.add(x[11]*x[18]*x[37]==353600)
s.add(x[7]+x[8]+x[17]-x[39]==192)
s.add(x[11]-x[35]-x[31]*x[9]==-8285)
s.add(x[23]-x[29]+x[39]==40)
s.add(x[28]+x[25]*x[10]*x[20]==530777)
s.add(x[29]*x[32]*x[3]==463914)
s.add(x[32]-x[22]+x[30]==98)
s.add(x[0]-x[13]+x[40]-x[38]==-74)
s.add(x[21]+x[17]-x[38]==108)
s.add(x[0]-x[41]*x[23]==-11804)
s.add(x[29]*x[2]*x[27]==997645)
s.add(x[25]-x[19]*x[35]==-7476)
s.add(x[16]-x[19]*x[7]==-5295)
s.add(x[33]+x[12]*x[26]+x[22]==2728)
s.add(x[24]+x[41]+x[32]==281)
s.add(x[31]*x[23]*x[14]==790020)
s.add(x[35]-x[6]*x[35]-x[14]==-3342)
s.add(x[31]+x[40]-x[25]*x[17]==-11148)
s.add(x[18]*x[36]+x[13]*x[19]==16364)
s.add(x[40]-x[5]+x[2]*x[18]==4407)
s.add(x[21]-x[25]+x[3]==55)
s.add(x[13]+x[14]+x[14]-x[2]==223)
s.add(x[36]*x[35]-x[5]*x[29]==-2449)
s.add(x[41]-x[39]+x[1]==135)
s.add(x[35]-x[0]*x[35]+x[0]==-4759)
s.add(x[8]-x[21]*x[10]-x[31]==-4776)
s.add(x[29]-x[24]+x[28]==126)
s.add(x[0]*x[10]-x[32]-x[8]==3315)
s.add(x[32]*x[28]+x[41]==5903)
s.add(x[37]-x[24]+x[32]==20)
s.add(x[20]*x[10]-x[15]+x[31]==4688)
s.add(x[36]-x[9]-x[18]*x[18]==-2721)
s.add(x[7]*x[9]+x[16]*x[30]==13876)
s.add(x[24]+x[34]+x[18]-x[7]==188)
s.add(x[27]*x[16]+x[20]==9310)
s.add(x[22]-x[30]-x[37]-x[9]==-211)
s.add(x[41]*x[4]*x[27]-x[38]==1491286)
s.add(x[35]-x[29]*x[8]+x[13]==-13131)
s.add(x[23]-x[7]-x[24]-x[22]==-107)
s.add(x[4]*x[37]*x[5]==560388)
s.add(x[17]*x[32]-x[15]==5295)
s.add(x[32]+x[23]*x[18]-x[5]==4927)
s.add(x[3]+x[8]*x[39]+x[39]==7397)
s.add(x[7]*x[25]-x[3]+x[36]==5597)
s.add(x[9]-x[24]-x[33]==-79)
s.add(x[30]+x[14]*x[36]==8213)

print(s.check())
mod = s.model()

output = ""

for i in range(0,len_flag):
    output += (chr(int(str(mod[x[i]]))))

print output

e=''
for i in range(0, len(output)):
        e += "x["+str(i) + "]==" + str(ord(output[i])) + ","

s.add(Not(And(eval(e[:-1]))))

if str(s.check()) == 'unsat':
    print("Unique Solution!")
else:
    print("Non-unique solutions exist... more work needed")

