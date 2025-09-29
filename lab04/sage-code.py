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

#print (inv ([1, 2, 0]))