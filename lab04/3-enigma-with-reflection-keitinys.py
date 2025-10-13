""" 
3. Enigma šifro (su atspindžiu) raktas = [19, 0].
Rotoriai:
 lambda_1 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14],
 lambda_2 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5].
Atspindžio keitinys:
 pi = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20].
Iššifruokite šifrą 

OZCOS RUEOY JNELL LGZTC RRPKF 
CRZSI YAOKQ ULTBF EBUPC AHPNS 
M 
"""

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # the alphabet
n   = len (abc) # number of letters in the alphabet

# makes text uppercase and filters out non-letters
def prepare (text):
    text = text.upper()
    new_text = ''
    for a in text:
        if a in abc:
            new_text += a
    return new_text

# converts a letter a from abc to a number from 0 to n - 1
def letter2number (a):
    return abc.index(a)

# converts a number d from 0 to n - 1 to a letter from abc
def number2letter (d):
    return abc [d]

# encrypts the letter a with the rotor defined by the substitution lmbda shifted (rotated) by m positions
def rotor (lmbda, a, m):
    b = (a + m) % n
    b = lmbda [b]
    return (b - m) % n 

#lmbda = [1, 2, 0] + [i for i in range (3, n)]; print(lmbda); print (rotor (lmbda, 1, 1))
       
# inverts the substitution lmbda
def inv (lmbda):
    lmbda_inv = [0] * len (lmbda)
    for i in range (len (lmbda)):
        lmbda_inv [lmbda [i]] = i
    return lmbda_inv

def decr(c, k, lambda_1, lambda_2, k1, k2):
    # k - m1 = n * m2 + n**2 * m3 + ...
        # n(m2 + n*m3 + ...)
    # (k - m1) / 2 = m2 + n2 * m3 + ...
    c = letter2number(c)
    m1 = k % n
    m2 = ((k - m1) // n) % n
    a = rotor(inv(lambda_2), c, m2 + k2)
    return number2letter(rotor(inv(lambda_1), a, m1 + k1))

#print (inv ([1, 2, 0]))

lambda_1 = [5, 3, 2, 0, 17, 10, 8, 24, 20, 11, 1, 12, 9, 22, 16, 6, 25, 4, 18, 21, 7, 13, 15, 23, 19, 14]
lambda_2 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]

ciphertext = """OZCOS RUEOY JNELL LGZTC RRPKF 
CRZSI YAOKQ ULTBF EBUPC AHPNS 
M"""
ciphertext = prepare(ciphertext)

key = [19, 0]

for k, c in enumerate(ciphertext):
    print (decr(c, k, lambda_1, lambda_2, key[0], key[1]), end="")