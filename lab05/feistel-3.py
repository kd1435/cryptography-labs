""" 
3. Feistelio šifro su dviem iteracijomis raktas nežinomas.
Iteracijos funkcija yra tokia: (r|k)^((k//16)&r).
Žinome, kad tekstas prasideda PR.
Iššifruokite šifrą 

[[38, 2], [57, 10], [34, 1], [53, 10], [63, 1], [49, 7], [52, 16], [38, 7], [59, 4], [52, 17], [50, 11], [34, 30], [41, 26], [55, 24], [51, 29], [55, 16], [53, 24], [40, 27], [39, 18], [38, 2], [57, 10], [63, 6], [63, 13], [55, 24], [48, 24], [36, 23], [35, 17], [34, 0], [35, 6], [43, 24], [55, 25], [53, 10], [34, 1], [63, 2], [50, 15], [41, 28], [42, 27], [47, 26], [53, 7], [44, 30], [56, 13], [48, 11], [49, 23], [55, 17], [51, 12], [38, 2], [47, 26], [42, 27], [56, 3], [59, 2], [49, 31]]
"""

# converts a number d to the corresponding Unicode character
def number2letter (d):
    return chr (d)

# print (number2letter (261), number2letter (65), number2letter (90), f"[{number2letter(32)}]")

# One iteration of the Feistel scheme.
# Takes as input a message M (a list of two bytes - left and right), 
# a key k (a byte), and an iteration function f 
# that takes as input the right side r of the message M and the key k, and outputs a byte
def iter(M, k, f):
    r = M[1]
    l = M[0] ^ eval(f)
    return [r, l]

def decr (M, key, f):
    M = iter(M, key[1], f)
    M = iter(M, key[0], f)
    return [M[1], M[0]]

f='(r|k)^((k//16)&r)'

cipher = [[38, 2], [57, 10], [34, 1], [53, 10], [63, 1], [49, 7], [52, 16], [38, 7], [59, 4], [52, 17], [50, 11], [34, 30], [41, 26], [55, 24], [51, 29], [55, 16], [53, 24], [40, 27], [39, 18], [38, 2], [57, 10], [63, 6], [63, 13], [55, 24], [48, 24], [36, 23], [35, 17], [34, 0], [35, 6], [43, 24], [55, 25], [53, 10], [34, 1], [63, 2], [50, 15], [41, 28], [42, 27], [47, 26], [53, 7], [44, 30], [56, 13], [48, 11], [49, 23], [55, 17], [51, 12], [38, 2], [47, 26], [42, 27], [56, 3], [59, 2], [49, 31]]
first_text = "PR"

possible_keys = []

for k1 in range(256):
    for k2 in range(256):
        a, b = decr([38, 2], [k1, k2], f)
        a = number2letter(a)
        b = number2letter(b)
        if (a == first_text[0] and b == first_text[1]):
            possible_keys.append([k1, k2])
            # print(a, b, end="\n", sep="")
    # print ()

# print(len(possible_keys))
# print(possible_keys)

for key in possible_keys:
    for M in cipher:
        a, b = decr([M[0], M[1]], [key[0], key[1]], f)
        a = number2letter(a)
        b = number2letter(b)
        if ((a.isupper() or a == " ") and (b.isupper() or b == " ")):
            print(a, b, end="", sep="")
        else: 
            break
    print ()

# solution:
# PRIESTAIJIDARBUVOISBANDZIUSIVISASKITASPRIEMONESIRNETBURTUSKURIAISTIKEJOSIVISDELTOBALTARAGIPRISIVILIOTI