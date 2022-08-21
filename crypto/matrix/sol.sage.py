

# This file was *autogenerated* from the file sol.sage
from sage.all_cmdline import *   # import sage library

_sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_256 = Integer(256); _sage_const_0 = Integer(0); _sage_const_32 = Integer(32); _sage_const_16 = Integer(16); _sage_const_1 = Integer(1)
from Crypto.Hash import SHAKE256

n = _sage_const_4 
rounds = _sage_const_5 
mod = _sage_const_256 

def number_to_matrix(t):
    X = Matrix(Zmod(mod), n, n)
    for i in range(n):
        for j in range(n):
            X[i, j] = t % mod
            t = t // mod
    return X

def matrix_to_number(X):
    x = _sage_const_0 
    for i in range(n):
        for j in range(n):
            x = x + int(X[i, j]) * (mod**(i * n + j))
    return x

def hash(x, A, B):
    shake = SHAKE256.new()
    shake.update(x)
    t = shake.read(_sage_const_32 ).hex()
    X = number_to_matrix(int(t, _sage_const_16 ))
    for _ in range(rounds):
        X = X * A + B
    return matrix_to_number(X)

def getFlag(A, B):
    message = b"https://forms.office.com/r/aDcxg7MK4s"
    return "greyhats{" + hash(message, A, B).hex() + "}"

f = open("dist/output.txt", "r").read().split("\n")
A = number_to_matrix(int(f[_sage_const_1 ], _sage_const_16 ))
C = number_to_matrix(int(f[_sage_const_0 ], _sage_const_16 ))
A = Matrix(Zmod(mod), A)
C = Matrix(Zmod(mod), C)

R1 = PolynomialRing(Zmod(mod), 'x', _sage_const_16 )
vars = R1.gens()
B = Matrix(R1, n, n)
for i in range(n):
    for j in range(n):
        B[i, j] = R1.gens()[i * n + j]

msg = b"If you are interested in joining us as a core team member, please take some time out to fill up the form before 22th Aug (Monday) 2pm."
shake = SHAKE256.new()
shake.update(msg)
t = shake.read(_sage_const_32 ).hex()
X = number_to_matrix(int(t, _sage_const_16 ))

for _ in range(rounds):
    X = X * A + B

polys = []

for i in range(_sage_const_4 ):
    for j in range(_sage_const_4 ):
        polys.append(X[i, j] - C[i, j])

I = Ideal(polys).groebner_basis()

B = Matrix(Zmod(mod), n, n)

print(I)

for i in range(_sage_const_4 ):
    for j in range(_sage_const_4 ):
        B[i, j] = -I[i * _sage_const_4  + j].subs({vars[i * _sage_const_4  + j]: _sage_const_0 })

print(getFlag(A, B))

