from random import *
c =choice('essai')
print(c)
print("'"+choice('autre essai')+"'")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(choice(alphabet))
for i in range(30):
    print(choice(alphabet), end='')

del c, alphabet
