"""
1. Iššifuokite afininį Cezario šifrą, jei teksto pradžia yra KIE:

UZČUV ZČĘGC URPGC ĄKOZC DOGAT 
OČZUZ GĄZUG ĄUGUF KŠRHT CKOGC 
ĄZ 

"""

import math

abc = 'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ' # the alphabet
n   = len (abc) # number of letters in the alphabet

# makes text uppercase and filters out non-letters
def prepare (text):
    text = text.upper()
    new_text = ''
    for a in text:
        if a in abc:
            new_text += a
    return new_text

#print (prepare ("Hello, World!"))

# converts a letter a from abc to a number from 0 to n - 1
def letter2number (a):
    return abc.index(a)

#print (letter2number ('B'))
#print (letter2number ('!'))

# converts a number d from 0 to n - 1 to a letter from abc
def number2letter (d):
    return abc[d]

#print (number2letter (5))
#print (number2letter (40))

# encrypts the given plaintext using Caesar cipher with the given key
def encryptCaesar (plaintext, key):
    plaintext = prepare (plaintext)

    ciphertext = ''
    for a in plaintext:
        m = (letter2number (a*key[0] + key[1] % n))
        ciphertext += number2letter (m)

    return ciphertext

#print (encryptCaesar ('ĄČĘjkl', 3))
#print ("[" + encryptCaesar ('', 3) + "]")

# decrypts the given ciphertext using Caesar cipher with the given key
def decryptCaesar (ciphertext, key):
    k1 = key[0]
    k2 = key[1]
    if k1 != 0:
        k1 = 1/k1%n
        print(1/k1%n)
    if k2 != 0:
        k2 = int(1 / k2) % n
    inverse_key = [k1, k2]                          # TODO: hint: inverse of k is 1/k%n
    return encryptCaesar (ciphertext, inverse_key)

#print (decryptCaesar ('mno', 3))

# --------------------------------------------------------------------
# exercise data
ciphertext = '''UZČUV ZČĘGC URPGC ĄKOZC DOGAT 
OČZUZ GĄZUG ĄUGUF KŠRHT CKOGC 
ĄZ'''
beginning_of_plaintext = 'KIE'

# construct the list of possible decryption keys
possible_keys = []
beginning_of_ciphertext = ciphertext[:len(beginning_of_plaintext)]
print (beginning_of_ciphertext)
print (n)
# TODO: hint: don't forget to check the additional condition for k1: gcd(k1, n) == 1
for k1 in range(n): # from 0 to n-1      # TODO: two loops - for k1 and for k2
    if math.gcd(k1, n) == 1:
        for k2 in range(n):
            print (decryptCaesar(beginning_of_ciphertext, [k1, k2]))
            if decryptCaesar (beginning_of_ciphertext, [k1, k2]) == beginning_of_plaintext: 
                possible_keys.append([k1, k2])   
print (possible_keys)

# decrypt the ciphertext with all passible keys and print all possible plaintexts
if possible_keys == []:
    print( "Not possible to decipher")
else:
    for key in possible_keys:
        print (decryptCaesar (ciphertext, key))