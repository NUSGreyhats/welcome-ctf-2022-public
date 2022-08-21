from Crypto.Hash import SHAKE256

n = 4
rounds = 5
mod = 256

def number_to_matrix(t):
    X = Matrix(Zmod(mod), n, n)
    for i in range(n):
        for j in range(n):
            X[i, j] = t % mod
            t = t // mod
    return X

def matrix_to_number(X):
    x = 0
    for i in range(n):
        for j in range(n):
            x = x + int(X[i, j]) * (mod^(i * n + j))
    return x

def hash(x, A, B):
    shake = SHAKE256.new()
    shake.update(x)
    t = shake.read(32).hex()
    X = number_to_matrix(int(t, 16))
    for _ in range(rounds):
        X = X * A + B
    return matrix_to_number(X)

def getFlag(A, B):
    message = b"https://forms.office.com/r/aDcxg7MK4s"
    return "greyhats{" + hash(message, A, B).hex() + "}"

f = open("dist/output.txt", "r").read().split("\n")
A = number_to_matrix(int(f[1], 16))
C = number_to_matrix(int(f[0], 16))
A = Matrix(Zmod(mod), A)
C = Matrix(Zmod(mod), C)

R1 = PolynomialRing(Zmod(mod), 'x', 16)
vars = R1.gens()
B = Matrix(R1, n, n)
for i in range(n):
    for j in range(n):
        B[i, j] = R1.gens()[i * n + j]

msg = b"If you are interested in joining us as a core team member, please take some time out to fill up the form before 22th Aug (Monday) 2pm."
shake = SHAKE256.new()
shake.update(msg)
t = shake.read(32).hex()
X = number_to_matrix(int(t, 16))

for _ in range(rounds):
    X = X * A + B

polys = []

for i in range(4):
    for j in range(4):
        polys.append(X[i, j] - C[i, j])

I = Ideal(polys).groebner_basis()

B = Matrix(Zmod(mod), n, n)

for i in range(4):
    for j in range(4):
        B[i, j] = -I[i * 4 + j].subs({vars[i * 4 + j]: 0})

print(getFlag(A, B))

# greyhats{19a8b656314c2eefa4d43bdd2155984b}