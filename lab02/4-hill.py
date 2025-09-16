""" 
4. Iššifruokite Hillo šifrą, jei raktas = [17, 15, 10, 7]:

ĖČEGD ĘČŽČR NĘĖGG TIBRG ĘDĘCD 
ZMPJR YZEGN IZYFĖ MYFSE CZYŽĮ 
ĘCŠO 

"""

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
# def encryptCaesar (plaintext, key):
#     plaintext = prepare (plaintext)

#     ciphertext = ''
#     for a in plaintext:
#         m = (letter2number (a) + key) % n                                    # TODO: affine Caesar cipher: key = [k1, k2]
#         ciphertext += number2letter (m)

#     return ciphertext

# #print (encryptCaesar ('ĄČĘjkl', 3))
# #print ("[" + encryptCaesar ('', 3) + "]")

# # decrypts the given ciphertext using Caesar cipher with the given key
# def decryptCaesar (ciphertext, key):
#     inverse_key = -key                                                        # TODO: hint: inverse of k is 1/k%n
#     return encryptCaesar (ciphertext, inverse_key)

# #print (decryptCaesar ('mno', 3))


def matrix_multiplication (m, K):
    return [m[0]*K[0]+m[1]*K[2], m[0]*K[1]+m[1]*K[3]]

def inverse_matrix (K):
    det_K = K[0]*K[3] - K[1]*K[2]
    inv_det = 1 / det_K % n
    for i in range(n):
        if (inv_det * i) % n == 1:
            inv_det = i
            break
    return [K[3]*inv_det % n, -K[1]*inv_det % n, -K[2]*inv_det % n, K[0]*inv_det % n]

print(inverse_matrix([17, 15, 10, 7]))

# --------------------------------------------------------------------
# exercise data
ciphertext = '''ĖČEGD ĘČŽČR NĘĖGG TIBRG ĘDĘCD 
ZMPJR YZEGN IZYFĖ MYFSE CZYŽĮ 
ĘCŠO'''
# beginning_of_plaintext = 'JK'

# construct the list of possible decryption keys
possible_keys = []
# beginning_of_ciphertext = ciphertext[:len(beginning_of_plaintext)]
# print (beginning_of_ciphertext)
# for key in range(n): # from 0 to n-1                                           # TODO: two loops - for k1 and for k2
    # if decryptCaesar (beginning_of_ciphertext, key) == beginning_of_plaintext: # TODO: hint: don't forget to check the additional condition for k1: gcd(k1, n) == 1
        # possible_keys.append(key)
# print (possible_keys)

# decrypt the ciphertext with all passible keys and print all possible plaintexts
# if possible_keys == []:
#     print( "Not possible to decipher")
# else:
#     for key in possible_keys:
#         print (decryptCaesar (ciphertext, key))