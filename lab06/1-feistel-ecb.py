"""
1. Feistelio šifro su trimis iteracijomis iteracijų raktai = [210, 247, 155].
Iteracijos funkcija F yra tokia: (r|k)^((r//16)&k).
Iššifruokite šifrą, sudarytą ECB režimu: 

[[41, 191], [35, 183], [37, 183], [60, 179], [46, 187], [44, 191], [59, 182], [44, 170], [46, 183], [37, 183], [43, 170], [38, 164], [38, 177], [38, 185], [50, 165], [53, 162], [43, 187], [47, 173], [43, 187], [47, 173], [59, 182], [58, 165], [42, 191], [33, 185], [54, 162], [53, 181], [34, 164], [33, 191], [33, 188], [50, 165], [33, 163], [44, 183], [33, 186], [39, 184], [45, 173], [42, 191], [46, 170], [38, 164], [43, 180], [58, 176], [35, 160], [47, 178], [36, 191], [52, 167], [38, 162], [43, 176], [36, 191], [41, 170], [39, 165], [41, 187], [43, 191], [58, 180], [51, 182], [47, 173], [42, 181], [34, 191], [41, 185], [32, 187], [47, 173], [63, 182], [52, 164], [34, 175], [45, 177], [34, 191], [117, 213]]
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

ciphertext = [[41, 191], [35, 183], [37, 183], [60, 179], [46, 187], [44, 191], [59, 182], [44, 170], [46, 183], [37, 183], [43, 170], [38, 164], [38, 177], [38, 185], [50, 165], [53, 162], [43, 187], [47, 173], [43, 187], [47, 173], [59, 182], [58, 165], [42, 191], [33, 185], [54, 162], [53, 181], [34, 164], [33, 191], [33, 188], [50, 165], [33, 163], [44, 183], [33, 186], [39, 184], [45, 173], [42, 191], [46, 170], [38, 164], [43, 180], [58, 176], [35, 160], [47, 178], [36, 191], [52, 167], [38, 162], [43, 176], [36, 191], [41, 170], [39, 165], [41, 187], [43, 191], [58, 180], [51, 182], [47, 173], [42, 181], [34, 191], [41, 185], [32, 187], [47, 173], [63, 182], [52, 164], [34, 175], [45, 177], [34, 191], [117, 213]]
key = [210, 247, 155]
f = '(r|k)^((r//16)&k)'

for block in ciphertext:
    M = feistel(block, [key[2], key[1], key[0]], f)
    print(number2letter(M[0]), number2letter(M[1]), sep="", end="")

# solution:
# NADABARLIEKATIKTAIBALTARAGIOURSULEISLEISTIUZMANOPUSBERNIOJURGUCIOLINKSMAITAREJUODVALKISPATENKINTASNELAUKTAISEKMINGOMISPIRSLYBOMIS