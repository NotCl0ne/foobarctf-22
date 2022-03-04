#!/usr/bin/env python 

from __future__ import print_function

print("=========================")
print("  WELCOME TO FOOBAR JAIL ")
print("=========================")



blacklist = [
    "import",
    "exec",
    "eval",
    "os",
    "pickle",
    "subprocess",
    "input",
    "blacklist",
    "sys"
]

builtin = __builtins__.__dict__.keys()
builtin.remove('raw_input')
builtin.remove('print')
for modules in builtin:
    del __builtins__.__dict__[modules]

while 1 == 1:
    try:
        print(">>>", end=' ')
        val = raw_input()
        
        for word in blacklist:
            if word.lower() in val.lower():
                print("Sorry!! You cannot use that here.")
                break
            else: 
                exec val   
    except:
        print ("What are you doing ? :(")
        continue
    