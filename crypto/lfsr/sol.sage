from Crypto.Util.number import long_to_bytes
from Crypto.Hash import SHAKE256

class LFSR:
    def __init__(self, seed, taps):
        self.taps = taps
        self.state = seed
        self.length = len(seed)
        
    def next_bit(self):
        new_bit = 0
        for i in range(self.length):
            if i in self.taps:
                new_bit = new_bit + self.state[i]
        res = self.state[0]
        self.state = self.state[1:] + [new_bit]
        return res

def xor(a, b):
    return [((i ^^ j) >> k) & 1 for i,j in zip(a,b) for k in range(8)]

def getFlag(key1, key2):
    shake = SHAKE256.new()
    shake.update(long_to_bytes(key1) + long_to_bytes(key2))
    return "greyhats{" + shake.read(20).hex() + "}"

c = xor(open("dist/encrypted", 'rb').read(), open("dist/text.txt", 'rb').read())

R1 = PolynomialRing(GF(2), 'x', 128)
X = R1.gens()

R2 = PolynomialRing(GF(2), 'y', 128)
Y = R2.gens()

tap1 = [0, 4, 7, 11, 29, 30, 49, 50, 59, 72, 88, 127]
tap2 = [0, 9, 30, 45, 59, 60, 68, 86, 99, 100, 111, 127]
LFSR1 = LFSR([X[i] for i in range(128)], tap1)
LFSR2 = LFSR([Y[i] for i in range(128)], tap2)

Mx = []
Vx = []

My = []
Vy = []

count = 0

print(len(c))

for i in range(len(c)):
    f = LFSR1.next_bit()
    g = LFSR2.next_bit()
    if (c[i] == 1):
        nx = []; ny = []
        Vx.append(0); Vy.append(1)
        for j in range(128):
            nx.append(f.coefficient({X[j] : 1}))
            ny.append(g.coefficient({Y[j] : 1}))
        Mx.append(nx)
        My.append(ny)

Mx = Matrix(GF(2), Mx)
My = Matrix(GF(2), My)
Vx = vector(GF(2), Vx)
Vy = vector(GF(2), Vy)


conX = Mx.right_kernel().basis()
conY = My.solve_right(Vy)

conX = [int(conX[0][i]) for i in range(128)]
conY = [int(conY[i]) for i in range(128)]

for i in range(8000):
    t1 = conX[-1]
    for j in tap1[1:]:
        t1 = t1 ^^ conX[j - 1]
    conX = [t1] + conX[:-1]

    t2 = conY[-1]
    for j in tap2[1:]:
        t2 = t2 ^^ conY[j - 1]
    conY = [t2] + conY[:-1]

seed1 = 0
seed2 = 0
for i in range(128):
    seed1 += conX[i] << i
    seed2 += conY[i] << i

print(getFlag(seed1, seed2))

# greyhats{7bf0f53a7b824c1722de23e3afe78a9629251777}