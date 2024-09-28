# micro
#include <stdio.h>

int main() {
    int n, first_term = 0, second_term = 1, next_term, i;
 
    // Ask user to input number of terms 
    printf("Enter the number of terms: ");
    scanf("%d", &n);
 
    printf("First %d terms of the Fibonacci series:\n", n);
    for (i = 0; i < n; i++) {
        if (i <= 1) {
            next_term = i;
        } else {
            next_term = first_term + second_term;
            first_term = second_term;
            second_term = next_term;
        }
        printf("%d ", next_term);
    }
    printf("\n");

    return 0;
}
