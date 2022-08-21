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

void win() {
    system("/bin/sh");
}

typedef long long i64;

#define HISTORY_SZ 0x10

void banner() {
    puts("Checksum Sum Checker");
    puts("--- math is hard ---");
    puts("1: View history");
    puts("2: Sum numbers");
}

// this is what checksum does, right?
bool checksum(i64 n) {
    if (n == 1337) {
        puts("wow! you win!");
        return true;
    }
    return false;
}

int main() {
    setup();

    i64 history[HISTORY_SZ];
    i64 history_idx = 0;
    i64 x;
    i64 opt, read_idx;

    banner();
    
    while(1) {
        printf("opt >> ");
        scanf("%lld", &opt);
        switch (opt) {
            case 1:
                printf("idx >> ");
                scanf("%lld", &read_idx);
                if (read_idx >= HISTORY_SZ)
                    exit(1);
                printf("<< %lld\n", history[read_idx]);
                break;

            case 2:
                printf("x >> ");
                scanf("%lld", &x);
                history[history_idx] = x;
                if(checksum(x)) return 0;
                history_idx++;
                break;
        }
    }
}
