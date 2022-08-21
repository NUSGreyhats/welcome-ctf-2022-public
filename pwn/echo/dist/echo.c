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

int main() {
    setup();

    char message[80];

    while (true) {
        printf("> ");
        memset(message, 0, 80);
        read(0, message, 0x80);
        if (!strncmp(message, "q", 2) || !strncmp(message, "q\n", 3)) {
            return 0;
        }
        printf("< %s", message);
    }
}
