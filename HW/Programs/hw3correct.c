// Program is in C
#include <stdio.h>
#include <stdlib.h>


// Function for even numbers (called indirectly  every time)
void print_func(int start, int end) {
    for (int i = start; i <= end; i++) {
        printf("%d ", i);
    }
}

// Function to check if the number is prime
int is_prime(int a) {
    if (a < 2)
        return 0; // Numbers less than 2 are not prime

    for (int i = 2; i * i <= a; i++) {
        if (a % i == 0) {
            return 0; // If num is divisible by any number i, it's not prime
        }
    }

    return 1; // If no divisor found, nnumber is prime
}

// Function to find prime numbers in the range (called indirectly)
void find_prime(int start, int end) {
    int primecount = 0;
    printf("\nAll prime numbers in the range are:\n");
    for (int i = start; i <= end; i++) {
        if (is_prime(i)) {
            printf("%d is a prime number\n", i);
            primecount++;
        }
    }
    
    if (primecount == 0) {
        printf("\nThere are no prime numbers in this number range");
    }
    

}

int main() {
    int start, end;
    int (*indirect_func)(int, int); // Function pointer (to point to other functions for indirect calls)

    // Get input range
    printf("Please enter 2 numbers (starting and ending values of the range) in seperate inputs\n");
    printf("\nEnter the first (starting number in the range): ");
    scanf("%d", &start);
    printf("\nEnter the second (end number in the range): ");
    scanf("%d", &end);
    
    if(start<= 0 || end <= 0){
        printf("\nInputs not valid. Enter two positive non zero numbers");
        return 1; 
    }

    if (start > end) {
        int temp = start;
        start = end;
        end = temp;
    }

    //indirectly calling function to print all numbers in range using indirect_func
    indirect_func = print_func;
    printf("\n All numbers in the range are:");
    indirect_func(start, end);
    
    //indirectly calling function to print all prime numbers in range using indirect_func
    indirect_func = find_prime;
    indirect_func(start, end);

    return 0;
}
