"""
3. Feistelio šifro su trimis iteracijomis iteracijų raktai = [210, 247, 155].
Iteracijos funkcija F yra tokia: (r|k)^((r//16)&k).
Inicializacijos vektorius = [66, 107].
Iššifruokite šifrą, sudarytą CFB režimu:

[[121, 214], [82, 106], [105, 197], [85, 108], [119, 212], [86, 116], [122, 192], [93, 105], [125, 215], [82, 99], [101, 215], [76, 118], [100, 196], [75, 121], [119, 215], [86, 102], [106, 218], [66, 126], [127, 195], [68, 127], [120, 215], [95, 100], [124, 222], [90, 103], [116, 192], [76, 124], [111, 207], [92, 126], [127, 206], [83, 116], [117, 202], [90, 98], [119, 222], [93, 115], [126, 194], [89, 106], [125, 222], [79, 101], [97, 210], [71, 117], [102, 211], [73, 125], [114, 218], [91, 98], [124, 207], [72, 123], [109, 192], [78, 125], [105, 169]]
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

ciphertext = [[121, 214], [82, 106], [105, 197], [85, 108], [119, 212], [86, 116], [122, 192], [93, 105], [125, 215], [82, 99], [101, 215], [76, 118], [100, 196], [75, 121], [119, 215], [86, 102], [106, 218], [66, 126], [127, 195], [68, 127], [120, 215], [95, 100], [124, 222], [90, 103], [116, 192], [76, 124], [111, 207], [92, 126], [127, 206], [83, 116], [117, 202], [90, 98], [119, 222], [93, 115], [126, 194], [89, 106], [125, 222], [79, 101], [97, 210], [71, 117], [102, 211], [73, 125], [114, 218], [91, 98], [124, 207], [72, 123], [109, 192], [78, 125], [105, 169]] 
key = [210, 247, 155]
f = '(r|k)^((r//16)&k)'
IV = [66, 107]

M = feistel(IV, [key[0], key[1], key[2]], f)
print(number2letter(M[0] ^ ciphertext[0][0]), number2letter(M[1] ^ ciphertext[0][1]), sep="", end="")

for i in range(len(ciphertext) - 1):
    M = feistel(ciphertext[i], [key[0], key[1], key[2]], f) 
    print(number2letter(M[0] ^ ciphertext[i+1][0]), number2letter(M[1] ^ ciphertext[i+1][1]), sep="", end="")
    # Iterations after: they xor the currently being deciphered ciphertext block with previous ciphertext block 

# solution:
# TADAURSULENUKAITOKAIPAGUONAIRZODZIOPRATARTINEGALIZVILGTELEJOAKIUKAMPELIUJAUNIKISGRAZUSNEAPSAKOMAI