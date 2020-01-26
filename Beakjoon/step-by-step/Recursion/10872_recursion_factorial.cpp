#include <stdio.h>
int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

int main() {
    int input;
    scanf("%d", &input);
    int output = factorial(a);
    printf("%d", output);
}