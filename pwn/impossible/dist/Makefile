main:
	gcc  -fno-stack-protector -no-pie impossible.c -o impossible.bin; \
	patchelf --replace-needed libc.so.6 ./libc-2.31.so ./impossible.bin; \
	patchelf --set-interpreter ./ld-2.31.so ./impossible.bin; \
	chmod +x impossible.bin

dbg:
	gcc  -fno-stack-protector -no-pie impossible.c -o impossible.bin; \
	patchelf --replace-needed libc.so.6 ./dist/libc-2.31.so ./impossible.bin; \
	patchelf --set-interpreter ./dist/ld-2.31.so ./impossible.bin; \
	chmod +x impossible.bin