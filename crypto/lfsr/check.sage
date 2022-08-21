from secrets import randbits

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

class LFSRO:
    def __init__(self, seed_num, taps):
        seed = [(seed_num >> i) & 1 for i in range(128)]
        self.taps = taps
        self.state = seed
        self.length = len(seed)

    def next_bit(self):
        new_bit = 0
        for i in range(self.length):
            if i in self.taps:
                new_bit = new_bit ^^ self.state[i]
        res = self.state[0]
        self.state = self.state[1:] + [new_bit]
        return res



R1 = PolynomialRing(GF(2), 'x', 128)
X = R1.gens()

R2 = PolynomialRing(GF(2), 'y', 128)
Y = R2.gens()

LFSR1 = LFSR([X[i] for i in range(128)], [0, 4, 29, 30, 72, 88, 127])
LFSR2 = LFSR([Y[i] for i in range(128)], [0, 9, 45, 59, 100, 111, 127])

LFSRO1 = LFSRO(randbits(128), [0, 4, 29, 30, 72, 88, 127])
LFSRO2 = LFSRO(randbits(128), [0, 9, 45, 59, 100, 111, 127])

def get_random_bit():
    a = LFSRO1.next_bit()
    b = LFSRO2.next_bit()
    return ((a ^ b) & (a | b)) ^ (a ^ (a & b))

Mx = []
Vx = []

My = []
Vy = []

count = 0

for i in range(1500):
    f = LFSR1.next_bit()
    g = LFSR2.next_bit()
    if (get_random_bit() == 1):
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

print(Mx.rref())
# print(Mx.solve_right(Vx))