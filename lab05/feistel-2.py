""" 
2. Feistelio šifro su dviem iteracijomis raktas = ['?', 139].
Iteracijos funkcija yra tokia: (r|k)^((r//16)&k).
Iššifruokite šifrą 

[[245, 181], [234, 162], [243, 176], [238, 162], [238, 161], [251, 191], [227, 184], [241, 179], [252, 185], [224, 179], [253, 191], [226, 173], [227, 178], [244, 160], [237, 161], [227, 178], [253, 191], [226, 173], [227, 178], [241, 171], [245, 176], [228, 173], [245, 183], [248, 169], [240, 167], [238, 166], [224, 162], [247, 179], [229, 178], [253, 191], [245, 177], [226, 173], [228, 167], [228, 174], [249, 184], [249, 184], [250, 184], [229, 178], [227, 186], [239, 171], [227, 184], [251, 191], [224, 167], [224, 190], [225, 173], [249, 177], [229, 178], [225, 165], [236, 170], [227, 178], [227, 186]]"""


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
    M = iter(M, key[1], f)
    M = iter(M, key[0], f)
    return [M[1], M[0]]

f='(r|k)^((r//16)&k)'

cipher = [[245, 181], [234, 162], [243, 176], [238, 162], [238, 161], [251, 191], [227, 184], [241, 179], [252, 185], [224, 179], [253, 191], [226, 173], [227, 178], [244, 160], [237, 161], [227, 178], [253, 191], [226, 173], [227, 178], [241, 171], [245, 176], [228, 173], [245, 183], [248, 169], [240, 167], [238, 166], [224, 162], [247, 179], [229, 178], [253, 191], [245, 177], [226, 173], [228, 167], [228, 174], [249, 184], [249, 184], [250, 184], [229, 178], [227, 186], [239, 171], [227, 184], [251, 191], [224, 167], [224, 190], [225, 173], [249, 177], [229, 178], [225, 165], [236, 170], [227, 178], [227, 186]]

k2 = 139

for k1 in range(256):
    good_text = True
    for left, right in cipher:
        a, b = decr([left, right], [k1, k2], f)
        a = number2letter(a)
        b = number2letter(b)
        if ((a.isupper() or a == " ") and (b.isupper() or b == " ")):
            print(a, b, end="", sep="")
        else: 
            break
    print ()

# solution:
# VAIKSCIOJOTOKSPASLAPTINGASSUKLASTINGASYPSENATARYTUMKAAPGAUTIRENGDAMASISIRJAUISANKSTODELTODZIAUGDAMASIS