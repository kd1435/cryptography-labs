""" 
1. Feistelio šifro su trimis iteracijomis raktas = [36, 47, 24].
Iteracijos funkcija yra tokia: (r&k)^((k%16)|r).
Iššifruokite šifrą 

[[78, 65], [94, 91], [90, 89], [76, 74], [85, 74], [86, 95], [82, 73], [88, 93], [70, 70], [82, 71], [66, 69], [85, 66], [94, 88], [67, 88], [78, 74], [93, 91], [78, 74], [86, 91], [94, 95], [72, 64], [70, 64], [84, 79], [76, 68], [73, 66], [77, 78], [76, 68], [78, 74], [71, 91], [82, 74], [84, 64], [78, 72], [92, 94], [87, 78], [81, 68], [84, 66], [68, 94], [70, 70], [82, 71], [72, 69], [82, 74], [84, 64], [66, 95], [84, 88], [70, 66], [68, 94], [66, 64], [70, 79], [70, 70], [85, 66], [81, 64], [83, 74], [67, 68], [74, 74], [87, 74], [84, 78], [72, 66], [70, 79], [70, 70], [70, 70], [82, 71], [78, 69], [78, 69], [76, 69], [82, 74], [77, 81], [75, 66], [67, 88], [73, 74], [78, 72], [71, 94], [70, 71], [92, 94], [94, 94], [71, 89], [86, 89], [78, 88], [70, 79], [70, 70], [86, 91], [66, 88], [67, 91], [70, 66], [83, 69], [70, 70], [82, 71], [72, 69], [71, 88], [85, 74], [82, 69]]
"""


# converts a number d to the corresponding Unicode character
def number2letter (d):
    return chr (d)

print (number2letter (261), number2letter (65), number2letter (90), f"[{number2letter(32)}]")

# One iteration of the Feistel scheme.
# Takes as input a message M (a list of two bytes - left and right), 
# a key k (a byte), and an iteration function f 
# that takes as input the right side r of the message M and the key k, and outputs a byte
def iter(M, k, f):
    r = M[1]
    l = M[0] ^ eval(f)
    return [r, l]

def decr (M, key, f):
    M = iter(M, key[2], f)
    M = iter(M, key[1], f)
    M = iter(M, key[0], f)
    return [M[1], M[0]]

f='(r&k)^((k%16)|r)'; M=[123,55]; k=112; print(iter(M,k,f))

cipher = [[78, 65], [94, 91], [90, 89], [76, 74], [85, 74], [86, 95], [82, 73], [88, 93], [70, 70], [82, 71], [66, 69], [85, 66], [94, 88], [67, 88], [78, 74], [93, 91], [78, 74], [86, 91], [94, 95], [72, 64], [70, 64], [84, 79], [76, 68], [73, 66], [77, 78], [76, 68], [78, 74], [71, 91], [82, 74], [84, 64], [78, 72], [92, 94], [87, 78], [81, 68], [84, 66], [68, 94], [70, 70], [82, 71], [72, 69], [82, 74], [84, 64], [66, 95], [84, 88], [70, 66], [68, 94], [66, 64], [70, 79], [70, 70], [85, 66], [81, 64], [83, 74], [67, 68], [74, 74], [87, 74], [84, 78], [72, 66], [70, 79], [70, 70], [70, 70], [82, 71], [78, 69], [78, 69], [76, 69], [82, 74], [77, 81], [75, 66], [67, 88], [73, 74], [78, 72], [71, 94], [70, 71], [92, 94], [94, 94], [71, 89], [86, 89], [78, 88], [70, 79], [70, 70], [86, 91], [66, 88], [67, 91], [70, 66], [83, 69], [70, 70], [82, 71], [72, 69], [71, 88], [85, 74], [82, 69]]

key = [36, 47, 24]

for left, right in cipher:
    a, b = decr([left, right], key, f)
    print(number2letter(a), number2letter(b), end="", sep="")

# solution:
# JIPIRMAKARTABUVOMALUNEIRSISTAIPJAIPATIKOKADSOKINEJOKAIPPAUKSCIUKEPOVISUSMALUNOAUKSTUSCIAUSKEDAMAIRKVATODAMAPESIODAMAMALUNININKAUZZILSTANCIUPLAUKUIRPRASYDAMAPASUPTIANTMALUNOSPARNU