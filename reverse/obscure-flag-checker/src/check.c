#include <stdio.h>
#include <string.h>

#define true 1
#define false 0
#define bool char

const int N = 40;

char sbox[] = {228, 32, 78, 63, 152, 7, 145, 202, 73, 213, 117, 132, 70, 92, 61, 112, 71, 162, 60, 89, 91, 222, 22, 255, 146, 125, 57, 25, 200, 0, 129, 41, 85, 240, 77, 88, 122, 6, 102, 229};

char pbox[] = {5, 15, 12, 4, 19, 36, 8, 11, 25, 23, 29, 3, 6, 30, 35, 9, 27, 16, 7, 37, 34, 1, 17, 26, 39, 22, 38, 18, 28, 2, 14, 33, 0, 32, 24, 13, 10, 31, 20, 21};

char target[] = {139, 80, 121, 77, 225, 96, 218, 133, 61, 166, 68, 247, 35, 46, 98, 2, 33, 150, 82, 49, 104, 163, 87, 153, 205, 6, 74, 70, 248, 48, 222, 106, 39, 182, 18, 105, 27, 84, 57, 177};

bool check(char* input, size_t length) {
    if (length != N) {
        return false;
    }

    char tmp[N];

    for (int i = 0; i < N; i++) {
        tmp[pbox[i]] = input[i];
    }

    for (int i = 0; i < N; i++) {
        tmp[i] ^= sbox[i];
    }

    for (int i = 0; i < N; i++) {
        if (tmp[i] != target[i]) {
            return false;
        }
    }

    return true;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        return 1;
    }

    char* input = argv[1];

    if(check(input, strlen(input))) {
        return 0;
    }

    return 1;
}
