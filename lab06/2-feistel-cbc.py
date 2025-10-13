"""
2. Feistelio šifro su trimis iteracijomis iteracijų raktai = [210, 247, 155].
Iteracijos funkcija F yra tokia: (r|k)^((r//16)&k).
Inicializacijos vektorius = [66, 107].
Iššifruokite šifrą, sudarytą CBC režimu: 

[[56, 215], [68, 120], [46, 202], [84, 120], [44, 196], [66, 110], [38, 206], [73, 116], [32, 205], [91, 115], [56, 206], [81, 118], [33, 211], [84, 111], [40, 210], [83, 122], [49, 216], [95, 126], [41, 201], [75, 124], [63, 202], [89, 116], [54, 208], [85, 125], [58, 215], [92, 112], [54, 210], [89, 106], [55, 207], [85, 97], [63, 214], [68, 122], [60, 194], [90, 97], [53, 202], [83, 122], [121, 161]]
"""

# converts a number d to the corresponding Unicode character
def number2letter (d):
    return chr (d)

#print (number2letter (261), number2letter (65), number2letter (90), f"[{number2letter(32)}]")

# One iteration of the Feistel scheme.
# Takes as input a message M (a list of two bytes - left and right), 
# a key k (a byte), and an iteration function f 
# that takes as input the right side r of the message M and the key k, and outputs a byte
def iter(M, k, f):
    r = M[1]
    l = M[0]^eval(f)
    return [r, l]

#f='(r*k+r)%256'; M=[123,55]; k=112; print(iter(M,k,f))

def feistel (M, key, f):
    M = iter(M, key[0], f)
    M = iter(M, key[1], f)
    M = iter(M, key[2], f)
    return [M[1], M[0]]

ciphertext = [[56, 215], [68, 120], [46, 202], [84, 120], [44, 196], [66, 110], [38, 206], [73, 116], [32, 205], [91, 115], [56, 206], [81, 118], [33, 211], [84, 111], [40, 210], [83, 122], [49, 216], [95, 126], [41, 201], [75, 124], [63, 202], [89, 116], [54, 208], [85, 125], [58, 215], [92, 112], [54, 210], [89, 106], [55, 207], [85, 97], [63, 214], [68, 122], [60, 194], [90, 97], [53, 202], [83, 122], [121, 161]]
key = [210, 247, 155]
f = '(r|k)^((r//16)&k)'
IV = [66, 107]


# TODO: fix IndexError
M = feistel(ciphertext[0], [key[2], key[1], key[0]], f)
print(number2letter(M[0] ^ IV[0]), number2letter(M[1] ^ IV[1]), sep="", end="") # first iter
for i, block in enumerate(ciphertext):
    M = feistel(ciphertext[i + 1], [key[2], key[1], key[0]], f)
    print(number2letter(M[0] ^ ciphertext[i][0]), number2letter(M[1] ^ ciphertext[i][1]), sep="", end="") 
    # Iterations after: they xor current deciphered ciphertext block with previous ciphertext block 


# solution:
# PERSIJUOSDAVOPANCIUKADNESUZAVETUISISTODAVOIKLUMPESIRISIMETESANUPRAIVEZIMA