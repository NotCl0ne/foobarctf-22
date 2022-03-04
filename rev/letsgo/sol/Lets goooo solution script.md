### Lets goooo solution script   



Basically on running the program we can see that the program gives us nothing as output and automatically terminates lets open it up on ghidra to see whats actually happening.We can check out the main.main function to see the decompiled output of the main function.we can see a function call to main.mod63268() is made which basically on analysis we can see the programs uses the net library to access some data from an api.

Now from the global variables we know that the flag is acessed from the server endpoint 34.100.233.12:1337  so we can basically nc to this port to see if it responds and as we can see it prints out the text EYF45#NDJFJ^DSHSKhdh53728#cksa08xns. On thorough analaysis of our decompiled code we can see that that this string is basically trimmed to a key of length 32 and is used to encrypt the secrets.txt file which might be containing our flag. So assuming this encrypteddata.txt contains the encrypted data and we have the key which can be trimmed to a length of 32 .We can use any aes decryption tool to decrypt this text,doing so we find our flag GLUG{G0oo_b1n4r1Es_ar3_fuN_4563}.

