from re import T
from pwn import *
from decimal import Decimal, getcontext

getcontext().prec = 30
g = Decimal(-9.8)

r = remote("localhost", 4000)


for i in range(100):
    r.recvuntil("Round")
    r.recvline()
    s1 = list(map(lambda x : Decimal(x), r.recvline().decode()[1:-2].strip().split(", ")))
    s2 = list(map(lambda x : Decimal(x), r.recvline().decode()[1:-2].strip().split(", ")))

    if (s2[3] < s1[3]):
        s1, s2 = s2, s1

    t = Decimal(s2[3] - s1[3])

    vx = Decimal(s2[0] - s1[0]) / t
    vy = Decimal(s2[1] - s1[1]) / t
    tz = (Decimal(s2[2] - s1[2]) - g * t * t / 2) / t

    sx = s1[0] - s1[3] * vx
    sy = s1[1] - s1[3] * vy
    sz = s1[2] + tz * (-s1[3]) + g * (s1[3]) * (s1[3]) / 2 

    vz = tz + g * (-s1[3])

    maxT = (-vz - Decimal(vz * vz - 2 * g * sz).sqrt()) / g

    r.sendline(f"({sx}, {sy}, {sz})")
    r.sendline(f"({vx}, {vy}, {vz + g * maxT})")

r.interactive()