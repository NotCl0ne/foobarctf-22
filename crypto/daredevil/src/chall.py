from Crypto.Util.number import *
import os


FLAG = 'flag{fl4g_15_53rv3d_xD}'

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





def chall():
    s = Sign()
    print('WELCOME TO DAREDEVILS SIGNING SERVER')
    print()
    print("[P]ublic key ")
    print("[S]ign msg (hex)! ")
    print("[V]erify signature (hex)! ")
    print("[Q]uit ")

    while True:
        choice = input("> ").rstrip()
        if choice == 'P':
            print("\nN : {}".format(hex(s.n)))
            print("\ne : {}".format(hex(s.e)))
            print('\n')
        elif choice == 'S':
            try:
                msg = bytes.fromhex(input('msg to sign : '))
                if TOKEN in msg:
                    print('[!] NOT ALLOWED')
                else:
                    m = bytes_to_long(msg)
                    print("\nsignature : {}".format(hex(s.sign(m))))
                    print('\n')
            except:
                print('\n[!] ERROR (invalid input)')

        elif choice == 'V':
            try:

                msg = bytes.fromhex(input("msg : "))
                m = bytes_to_long(msg)
                signature = int(input("signature : "),16)
                if m < 0 or m > s.n:

                    print('[!] ERROR') #sanity check

                if s.verify(m, signature):
                    if long_to_bytes(m) == TOKEN:
                        print(FLAG)
                    else:
                        print('\n[+] Valid signature\n')
                else:
                    print('\n[!]Invalid signature\n')
            except:
                print('\n[!] ERROR(invalid input)')

        elif choice == 'Q':
            print('OK BYE :)')
            exit(0)
        else:
            print('\n[*] SEE OPTIONS')



        pass

if __name__ == '__main__':
    try:
        chall()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
