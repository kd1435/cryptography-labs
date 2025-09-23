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

# encrypts the given plaintext using Hill cipher with the given key
def encryptHill (plaintext, key):
    plaintext = prepare (plaintext)

    ciphertext = ''
    for a, b in zip(plaintext[::2], plaintext[1::2]):
        m = matrix_multiplication([letter2number(a), letter2number(b)], key)   
        ciphertext += number2letter(m[0])
        ciphertext += number2letter(m[1])

    return ciphertext

# decrypts the given ciphertext using Hill cipher with the given key
def decryptHill (ciphertext, key):
    inverse_key = inverse_matrix(key)                                   
    return encryptHill (ciphertext, inverse_key)

def matrix_multiplication (m, K):
    return [(m[0]*K[0]+m[1]*K[2]) % n, (m[0]*K[1]+m[1]*K[3]) % n]

def inverse_matrix (K):
    det_K = K[0]*K[3] - K[1]*K[2]
    inv_det = det_K
    if (inv_det != 0):
        for i in range(n):
            if (inv_det * i % n == 1):
                inv_det = i
                break
    # inv_det = 1 / det_K % n # only works in SageMath
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
key = [17, 15, 10, 7]

print(decryptHill(ciphertext, key))