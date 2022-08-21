import random

flag = "greyhats{f0rK_1s_fOR_p4sTA_n07_For_r1C3}"
n = len(flag)
print(n)

pbox = [i for i in range(n)]
random.shuffle(pbox)

sbox = [i for i in range(0x100)]
random.shuffle(sbox)
sbox = sbox[:len(flag)]

out = [0] * len(flag)
for i in range(len(pbox)):
    out[pbox[i]] = ord(flag[i])
    
for i in range(len(sbox)):
    out[i] ^= sbox[i]

print("pbox: ", pbox)
print("sbox: ", sbox)
print(out)

