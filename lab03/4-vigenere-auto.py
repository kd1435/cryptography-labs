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
n  = len (abc) # number of letters in the alphabet

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
plaintext = ""
key = list(key)

for i, cipher_letter in enumerate(ciphertext):
    decr_letter = number2letter((letter2number(cipher_letter) - letter2number(key[i])) % n)
    key.append(cipher_letter)
    plaintext += decr_letter

# Turn plaintext back into string
key = "".join(plaintext)
print(plaintext)

# Couldn't get a sensical plaintext, the output I got:
# GIBARIANASNEBEGYVASJEIGERAISUPRATAUKĄKALBĖJOSNAUTASTAINUOJOMIRTIESTEPRAĖJOKELIOLIKAVALANDŲKURDĖJOJOPALAIKUSARPALAIDOJOTIESAŠIOJEPLANETOJETOPADARYTINEGALIMAGALVOJAUAPIETAIILGOKAITARSIVELIONIOLIKIMASBŪTŲBUVĘSSVARBIAUSIASDALYKAS