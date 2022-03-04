from z3 import *
from random import *


#If you want to create a new flag, ensure it is printable (32 <= c <= 127)
# and add it to flag_mid
flag_start = "GLUG{"
flag_mid = "C01nc1d3nc3_c4n_b3_fr3aky_T6LSERDYB6"
flag_end = "}"

flag = flag_start + flag_mid + flag_end
len_flag = len(flag)
print(len(flag))
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

num_eqn = 2*len_flag #I have no idea what this should be, though it should definitely be bigger than len_flag... otherwise non-unique solutions...

E = []


#Given the flag and the number of variables, generate a random contraint
#of the form
#x % y % z  == N
#or
#w % x % y % z  == N
#where x,y,z,w are all chars in flag, and % is either {+.-.*}
def genRandEqn(total_vars, flag):
    num_vars = randint(3,4)
    rand_vars = []
    rand_indices = []
    for i in range(0, num_vars):
        index = randint(0, total_vars-1)
        rand_vars.append( "x[" + str(index) + "]")
        rand_indices.append(index)

    num_symbols = num_vars -1
    symbols = ["+", "-", "*"]

    e = "" #SAT var
    f = "" #flag var
    c = "" #c-code
    for i in range(0, num_symbols):
        s = choice(symbols)
        e += rand_vars[i] + s
        f += str(ord(flag[rand_indices[i]])) + s
        c += "x[" + str(rand_indices[i]) + "]" + s
    e += rand_vars[-1]
    f += str(ord(flag[rand_indices[-1]]))
    c += "x[" + str(rand_indices[-1]) + "]"

    #print("e: " + e)
    #print("f: " + f)
    #print("eval(f) = " + str(eval(f)))

    result = eval(f)

    return eval(e + "==" + str(result)), e + "==" + str(result), c + "==" + str(result)

#Generate num_eqn random contraints. At the moment, it is 2xlen_flag
#Then add it to the Solver, and
#add the string to E for printing to C and Z3 python solver later
for i in range(0, num_eqn):
    g = genRandEqn(len(x), flag)
    s.add(g[0])
    E.append(g[2])

#Ensure satisfiablity (given we constructed it, this should always return 'sat'
print(s.check())

'''
Check whether solution is unique??
f=''
for i in range(0, len(flag)):
    f+= "x["+str(i)+ "] != " + str(ord(flag[i])) + ","

s.add(Or(eval(f[:-1])))

if( str(s.check()) == 'unsat'):
    #only one solution can continue

'''

#Generate a model for the solution
mod = s.model()

#Get the model into a printable form
output = ""
for i in range(0,len_flag):
    output += (chr(int(str(mod[x[i]]))))

print(output)

###########################################
####  Output C file for challenge
###########################################

c_file = open("password.c", "w")

c_head1 = '''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int main(int argc, char *argv[])
{

	char * x = NULL;
	int result = TRUE;
	int password_length = 0;

	if(argc != 2)
	{
		printf("Usage: a.out <password>\\n");
		return -1;
	}

	printf("argv[1]: %s, strlen(password) = %d\\n", argv[1], strlen(argv[1]));

	x = argv[1];

	password_length = strlen(x);
'''

c_head2 = "\tif (password_length != " + str(len_flag) + ")"
c_head3 = '''
	{
		printf("Incorrect password length\\n");
		return -1;
	}

'''

c_file.write(c_head1 + c_head2 + c_head3)

#print C-code
for e in E:
    c_file.write("\tif (!(" + e + "))\n")
    c_file.write("\t{\n")
    c_file.write("\t\tresult = FALSE;\n")
    c_file.write("\t}\n")


c_tail = '''
	if (result == TRUE)
	{
		printf("CONGRATULATIONS!\\n");
		return 0;
	}

	if (result == FALSE)
	{
		printf("Incorrect password\\n");
		return 0;
	}

	return 0;
}
'''
c_file.write(c_tail)
c_file.close()


###########################################
####  Output python Z3 file for solver
###########################################
z3_file = open("password_solve.py", "w")

pyz3_head1 = '''
#python2
#pip install z3

from z3 import *

flag_start = flag{"
flag_end = "}"
'''

pyz3_head2 = "len_flag = " + str(len_flag) + "\n"

pyz3_head3 = '''
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
'''

z3_file.write(pyz3_head1 + pyz3_head2 + pyz3_head3)


#write equations to solve
for e in E:
    z3_file.write("s.add(" + e + ")\n")

pyz3_tail = '''
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

'''

z3_file.write(pyz3_tail)
z3_file.close()

