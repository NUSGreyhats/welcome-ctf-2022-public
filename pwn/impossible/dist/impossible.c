#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void setup()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

typedef unsigned int uint;

void check(uint a, uint b) {
    if (a + b == 1337) {
        puts("you win? i guess??");
    }
}

uint read_uint(char* prompt) {
    puts(prompt);
    char buf[0x20];
    gets(buf);
    return strtoul(buf, NULL, 10);
}

int main() {
    setup();
    uint a = read_uint("a >> ");
    uint b = read_uint("b >> ");
    check(a, b);
}
