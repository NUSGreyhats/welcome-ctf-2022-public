main:
	gcc checksum.c -o checksum.bin; \
	patchelf --replace-needed libc.so.6 ./libc-2.31.so ./checksum.bin; \
	patchelf --set-interpreter ./ld-2.31.so ./checksum.bin; \
	chmod +x checksum.bin

dbg:
	gcc checksum.c -o checksum.bin; \
	patchelf --replace-needed libc.so.6 ./dist/libc-2.31.so ./checksum.bin; \
	patchelf --set-interpreter ./dist/ld-2.31.so ./checksum.bin; \
	chmod +x checksum.bin