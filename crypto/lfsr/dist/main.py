from Crypto.Util.number import long_to_bytes
from Crypto.Hash import SHAKE256
from secrets import randbits

class LFSR:
    def __init__(self, seed_num, taps):
        seed = [(seed_num >> i) & 1 for i in range(128)]
        self.taps = taps
        self.state = seed
        self.length = len(seed)
        
    def next_byte(self):
        res = 0
        for i in range(8):
            res += (self.next_bit() << i)
        return res

    def next_bit(self):
        new_bit = 0
        for i in range(self.length):
            if i in self.taps:
                new_bit ^= self.state[i]
        res = self.state[0]
        self.state = self.state[1:] + [new_bit]
        return res

def get_random_byte():
    a = LFSR1.next_byte()
    b = LFSR2.next_byte()
    return ((a ^ b) & (a | b)) ^ (a ^ (a & b))

def encrypt(s):
    encrypted = b""
    for i in range(len(s)):
        encrypted += long_to_bytes(s[i] ^ get_random_byte())
    return encrypted

def getFlag(key1, key2):
    shake = SHAKE256.new()
    shake.update(long_to_bytes(key1) + long_to_bytes(key2))
    return "greyhats{" + shake.read(20).hex() + "}"

key1 = randbits(128)
key2 = randbits(128)
    
LFSR1 = LFSR(key1, [0, 4, 7, 11, 29, 30, 49, 50, 59, 72, 88, 127])
LFSR2 = LFSR(key2, [0, 9, 30, 45, 59, 60, 68, 86, 99, 100, 111, 127])

for _ in range(1000):
    get_random_byte()

f = open("text.txt", "rb").read()
open("encrypted", "wb").write(encrypt(f))

print(getFlag(key1, key2))