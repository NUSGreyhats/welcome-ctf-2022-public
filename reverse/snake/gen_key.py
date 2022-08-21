lcg_a = 75
lcg_c = 74
lcg_m = 65537
lcg_x = 73
def lcg():
    global lcg_a, lcg_c, lcg_m, lcg_x
    old_x = lcg_x
    lcg_x = (lcg_x * lcg_a + lcg_c) % lcg_m
    return old_x

FLAG = b"greyhats{d1d_y0u_3nj0y_th3_g4m3?}"
key = []

for c in FLAG:
    k = lcg()
    print(k, c, k ^ c)
    key.append(k ^ c)

print(key)