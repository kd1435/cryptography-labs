# converts a number d to the corresponding Unicode character
def number2letter (d):
    return chr (d)

#print (number2letter (261), number2letter (65), number2letter (90), f"[{number2letter(32)}]")

# the inverse of a 2x2 matrix T modulo p
def matrix_inverse (T, p):
    det = T[0] * T[3] - T[1] * T[2] # determinant
    inv_det = 1 / det % p           # inverse of the determinant
    return [T[3] * inv_det % p, -T[1] * inv_det % p, -T[2] * inv_det % p, T[0] * inv_det % p]

#print (matrix_inverse ([1, 2, 3, 4], 5))

# 2x2 matrix T and 2x1 vector v multiplication modulo p
def mat_vect_mult (T, v, p):
    return [ (T[0] * v[0] + T[1] * v[1]) % p, (T[2] * v[0] + T[3] * v[1]) % p ]

#print (mat_vect_mult ([1,2,3,4], [4,2], 5))