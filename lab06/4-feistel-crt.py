"""
4. Feistelio šifro su trimis iteracijomis iteracijų raktai = [210, 247, 155].
Iteracijos funkcija F yra tokia: (r|k)^((r//16)&k).
Skaitliuko funkcija grąžina porą [a, a],
  kur a yra reikšmė iteracijos funkcijos F su argumentais
  r - bloko numeris, k - pirmosios iteracijos raktas.
Iššifruokite šifrą, sudarytą CRT režimu:

[[238, 113], [252, 109], [250, 100], [232, 126], [242, 109], [236, 112], [237, 96], [236, 114], [238, 120], [241, 105], [237, 108], [250, 109], [245, 127], [246, 98], [246, 104], [235, 102], [248, 97], [252, 114], [252, 113], [246, 107], [234, 99], [236, 115], [243, 96], [240, 115], [246, 120], [243, 104], [232, 126], [244, 99], [234, 107], [252, 124], [234, 124], [234, 97], [216, 85], [214, 67], [221, 66], [214, 84], [218, 87], [200, 67], [208, 70], [218, 80], [209, 74], [222, 94], [214, 74], [221, 79], [215, 95], [218, 88], [218, 76], [210, 65], [211, 66], [221, 73], [209, 66], [211, 79]]
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

ciphertext = [[238, 113], [252, 109], [250, 100], [232, 126], [242, 109], [236, 112], [237, 96], [236, 114], [238, 120], [241, 105], [237, 108], [250, 109], [245, 127], [246, 98], [246, 104], [235, 102], [248, 97], [252, 114], [252, 113], [246, 107], [234, 99], [236, 115], [243, 96], [240, 115], [246, 120], [243, 104], [232, 126], [244, 99], [234, 107], [252, 124], [234, 124], [234, 97], [216, 85], [214, 67], [221, 66], [214, 84], [218, 87], [200, 67], [208, 70], [218, 80], [209, 74], [222, 94], [214, 74], [221, 79], [215, 95], [218, 88], [218, 76], [210, 65], [211, 66], [221, 73], [209, 66], [211, 79]]
key = [210, 247, 155]
f = '(r|k)^((r//16)&k)'

r = 0
k = key[0]
a = eval(f)
ctr = [a, a]

for block in ciphertext:
    k = key[0]
    a = eval(f)
    ctr = [a, a]
    M = feistel(ctr, [key[0], key[1], key[2]], f)
    print(number2letter(M[0] ^ ciphertext[r][0]), number2letter(M[1] ^ ciphertext[r][1]), sep="", end="")
    r += 1
    # Iterations after: they xor current deciphered ciphertext block with previous ciphertext block 

# solution:
# STAIGAUZKLUPTAURSULEPAGALVOJOARNEDAVATKOSBUSJAISKUNDUSIOSBETSUSIGRIEBEIRATSAKEARNEAPIEBALTARAGIKLEBONELI