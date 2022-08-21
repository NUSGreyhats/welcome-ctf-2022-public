from Crypto.Hash import SHAKE256

n = 4
rounds = 5
mod = 256
A = random_matrix(Zmod(mod), 4, 4)
B = random_matrix(Zmod(mod), 4, 4)

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

def hash(x):
    shake = SHAKE256.new()
    shake.update(x)
    t = shake.read(32).hex()
    X = number_to_matrix(int(t, 16))
    for _ in range(rounds):
        X = X * A + B
    return matrix_to_number(X)

def getFlag():
    message = b"https://forms.office.com/r/aDcxg7MK4s"
    return "greyhats{" + hash(message).hex() + "}"

msg = b"If you are interested in joining us as a core team member, please take some time out to fill up the form before 22th Aug (Monday) 2pm."

f = open("output.txt", "w")
f.writelines([hash(msg).hex() + "\n", matrix_to_number(A).hex()])

print(getFlag())