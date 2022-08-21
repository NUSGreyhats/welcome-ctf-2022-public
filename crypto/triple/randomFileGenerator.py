import os

size = 311108

with open('1', 'wb+') as fout:
    fout.write(os.urandom(size))
fout.close()

with open('2', 'wb+') as fout:
    fout.write(os.urandom(size))
fout.close()

with open('3', 'wb+') as fout:
    fout.write(os.urandom(size))
fout.close()
