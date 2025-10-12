""" 
4. Vigenere-auto šifro raktas = KNYGOS. Iššifruokite šifrą 

UŽKGG CUMKĄ VFŪŠU JUFNĘ AŲČJF 
ĘIMZČ ŽĘDMŠ OASDC UŪJHŪ RURĖH 
NJUBŲ DĘZYO ĘŲAGO HAĄPA ONJPD 
EDŽCE LRDŪC SLFGS NLĘYM EĘAŲC 
MSĘIH VFSVĄ HYFCB PUBBJ ĖIUUY 
CSMJH YRVHC UOJLA CŽODŽ TJMUJ 
ŽGŲČU TŽŲŠŠ FTTŲĮ ČJMTĘ TPTEF 
ĘDYTŪ ANBOG ĖOEYĖ ŲOČMA ĖMRAH 
ŲGINĘ BMĘIF FYMĄC PFDSĄ OCTDY

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

# converts a letter a from abc to a number from 0 to n - 1
def letter2number (a):
    return abc.index(a)

# converts a number d from 0 to n - 1 to a letter from abc
def number2letter (d):
    return abc [d]

# encrypts the given plaintext using Vigenere cipher with the given key
# the key is given as a word
def encryptVigenere (plaintext, key):
    plaintext = prepare (plaintext)
    key = prepare (key)
    
    # converts the key to a list of numbers
    keys = []
    key_length = len(key)
    for i in range (key_length):
        keys.append (letter2number (key [i]))

    # encrypts
    cyphertext = ""
    plaintext_length = len (plaintext)
    for i in range (plaintext_length):
        cyphertext += number2letter ((letter2number (plaintext [i]) + keys [i % key_length]) % n)
    return cyphertext

ciphertext = '''UŽKGG CUMKĄ VFŪŠU JUFNĘ AŲČJF 
ĘIMZČ ŽĘDMŠ OASDC UŪJHŪ RURĖH 
NJUBŲ DĘZYO ĘŲAGO HAĄPA ONJPD 
EDŽCE LRDŪC SLFGS NLĘYM EĘAŲC 
MSĘIH VFSVĄ HYFCB PUBBJ ĖIUUY 
CSMJH YRVHC UOJLA CŽODŽ TJMUJ 
ŽGŲČU TŽŲŠŠ FTTŲĮ ČJMTĘ TPTEF 
ĘDYTŪ ANBOG ĖOEYĖ ŲOČMA ĖMRAH 
ŲGINĘ BMĘIF FYMĄC PFDSĄ OCTDY'''
key = 'KNYGOS'


key_length = len(key)

ciphertext = prepare(ciphertext)
# Assign key to plaintext as list, because plaintext will be mutable / appended to
plaintext = list(key) 

for letter in ciphertext:
    text = "?"
    plaintext += text