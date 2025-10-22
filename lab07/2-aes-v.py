"""
2. AES-V parametrai tokie patys, kaip 1 užduotyje.
Blokas M = [51, 18, 158, 127] buvo užšifruotas du kartus AES-V šifru
  su raktais K1 = ['?', 188, 148, 245] ir K2 = [199, '?', 262, 151].
Suraskite raktus meet-in-the middle ataka, jei šifras C = [25, 309, 112, 78].  
"""

# converts a number d to the corresponding Unicode character
def number2letter (d):
    return chr (d)

#print (number2letter (261), number2letter (65), number2letter (90), f"[{number2letter(32)}]")

# the inverse of a 2x2 matrix T modulo p
def matrix_inverse (T, p):
    det = T[0] * T[3] - T[1] * T[2] # determinant
    if(det != 0):
        for i in range(p):
            if (det * i % p == 1):
                det = i
                break
    inv_det = det           # inverse of the determinant3
    return [T[3] * inv_det % p, -T[1] * inv_det % p, -T[2] * inv_det % p, T[0] * inv_det % p]

#print (matrix_inverse ([1, 2, 3, 4], 5))

# 2x2 matrix T and 2x1 vector v multiplication modulo p
def mat_vect_mult (T, v, p):
    return [ (T[0] * v[0] + T[1] * v[1]) % p, (T[2] * v[0] + T[3] * v[1]) % p ]

#print (mat_vect_mult ([1,2,3,4], [4,2], 5))

def step4_inv (C, K, p):
    return [(C[i]-K[i]) % p for i in range(4)]

# print(step4_inv ([1,2,3,4], [2,3,4,5], 5)) 

def step3_inv (C, T_inv, p):
    col1 = mat_vect_mult (T_inv, [C[0],C[2]], p)
    col2 = mat_vect_mult (T_inv, [C[1],C[3]], p)
    return[col1[0], col2[0], col1[1], col2[1]]

def step2_inv (C):
    return[C[0], C[1], C[3], C[2]]

def step1_inv (C, a, b, p):
    return [((a/(c-b))%p for i in range(p)) if c != b else 0 for c in C]
    return [(i if for i in range(p)) if c != b else 0 for c in C]

print(step1_inv([1,2,3,4], 2, 4, 2))
            
def keys_iter (K, a, b, p):
    k11 = (K[0] + b + (a/K[3])%p if K[3] != 0 else 0) % p
    k12 = (K[1] + k11) % p
    k21 = (K[2] + k12) % p
    k22 = (K[3] + k21) % p
    return [k11, k12, k21, k22]

def keys(K1, a, b, p):
    K2 = keys_iter(K1, a, b, p)
    K3 = keys_iter(K2, a, b, p)
    return [K1, K2, K3]

p = 317
[a,b] = [13, 15]
T = [1, 11, 31, 4]
key = [195, 268, 227, 272]
ciphertext = [[154, 218, 286, 271], [63, 62, 225, 299], [180, 175, 308, 267], [196, 197, 189, 260], [265, 255, 138, 175], [68, 252, 172, 131], [2, 127, 291, 39], [203, 308, 3, 169], [296, 243, 276, 255], [169, 254, 298, 295], [88, 202, 196, 0], [143, 159, 88, 225], [64, 170, 40, 305], [26, 309, 147, 142], [65, 300, 217, 226]]
T_inv = matrix_inverse(T, p)

table2 = []
for k2 in range(p):
    C1 = decr(C, [183, k2, 110, 239], a, b, T_inv, p)
    table2.append([k2, C1])
print(table2)

# analogous table using encryption function (decr_iter steps in 1-4 order)