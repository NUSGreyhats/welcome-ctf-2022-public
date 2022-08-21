# Obscure Flag Checker

### Challenge Details
binary creates another binary at runtime, which contains the actual flag routine.

### Key Concepts
UPX, fork & subprocesses, basic binary reversing

### Solution
Observe the file that is created at runtime and executed with a forked process, dump those bytes and reverse that binary instead.

### Learning Objectives
UPX packing (and unpacking). Understand how subprocesses are created.

### Flag
`greyhats{f0rK_1s_fOR_p4sTA_n07_For_r1C3}`
