#!/usr/bin/env python3
from Crypto.Util.number import *
import sys
import os
from time import sleep
import colorama
from colorama import Fore
import signal

SECRET = 'GLUG{fl4g_15_53rv3d_xD_E9644V2GG0}'

TOKEN = b'd4r3d3v!l'


class Sign(object):
    def __init__(self):
        p = getPrime(512)
        q = getPrime(512)
        e = 65537
        phi = (p - 1) * (q - 1)
        while GCD(e, phi) != 1:
            p = getPrime(512)
            q = getPrime(512)
            phi = (p - 1) * (q - 1)

        self.d = inverse(e, phi)
        self.n = p * q
        self.e = e

    def sign(self, msg):
        return pow(msg, self.d, self.n)

    def verify(self, msg, sign):
        return pow(sign, self.e, self.n) == msg


signal.alarm(60)

def chall():
    s = Sign()
    print(Fore.GREEN+'AVAILABLE OPTIONS !')
    print()
    print("[E]ncryption function")
    print("[P]ublic key ")
    print("[S]ign msg (hex)! ")
    print("[V]erify signature (hex)! ")
    print("[Q]uit ")
    print('\033[39m')
    while True:
        choice = input("> ").rstrip()
        if choice == 'E':
            with open('enc.py', 'r') as reader:
                line = reader.readline()
                while line != '':
                    print(Fore.YELLOW+line, end='')

                    line = reader.readline()
            print('\033[39m')
        elif choice == 'P':
            print("\nN : {}".format(hex(s.n)))
            print("\ne : {}".format(hex(s.e)))
            print('\n')
        elif choice == 'S':
            try:
                msg = bytes.fromhex(input('msg to sign : '))
                if TOKEN in msg:
                    print(Fore.RED+'[!] NOT ALLOWED')
                    print('\033[39m')
                else:
                    m = bytes_to_long(msg)
                    print("\nsignature : {}".format(hex(s.sign(m))))
                    print('\n')
            except:
                print(Fore.RED+'\n[!] ERROR (invalid input)\n')
                print('\033[39m')
        elif choice == 'V':
            try:

                msg = bytes.fromhex(input("msg : "))
                m = bytes_to_long(msg)
                signature = int(input("signature : "),16)
                if m < 0 or m > s.n:
                    print(Fore.RED+'[!] ERROR')
                    print('\033[39m')
                if s.verify(m, signature):
                    if long_to_bytes(m) == TOKEN:
                        print(Fore.GREEN+SECRET)
                        print('\033[39m')
                    else:
                        print(Fore.GREEN+'\n[+] Valid signature\n')
                        print('\033[39m')
                else:
                    print(Fore.RED+'\n[!]Invalid signature\n')
                    print('\033[39m')
            except:
                print(Fore.RED+'\n[!] ERROR(invalid input)\n')
                print('\033[39m')

        elif choice == 'Q':
            print('OK BYE :)')
            exit(0)
        else:
            print(Fore.YELLOW+'\n[*] SEE OPTIONS')
            print('\033[39m')


        pass

if __name__ == '__main__':
    try:
        welcome = "WELCOME TO DAREDEVIL'S SIGNING SERVER...\n"
        for char in welcome:
            sleep(0.1)
            sys.stdout.write(Fore.RED+char)
            sys.stdout.flush()
        print()
        chall()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
