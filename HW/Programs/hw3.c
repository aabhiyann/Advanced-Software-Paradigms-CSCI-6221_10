// Program is in C
#include <stdio.h>

// Function for even numbers (called indirectly  every time)
void even_func(int start, int end) {
    for (int i = start; i <= end; i++) {
        if (i % 2 == 0) {
            printf("%d ", i);
        }
    }
}

// Function for odd numbers (called indirectly every time)
void odd_func(int start, int end) {
    for (int i = start; i <= end; i++) {
        if (i % 2 != 0) {
            printf("%d ", i);
        }
    }
}

// Function to add even numbers (called indirectly accourind to the condition)
void add_even(int start, int end) {
    int sum = 0;
    for (int i = start; i <= end; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    printf("\nSum of even numbers in the range: %d", sum);
}

// Function to add odd numbers (called indirectly accourind to the condition)
void add_odd(int start, int end) {
    int sum = 0;
    for (int i = start; i <= end; i++) {
        if (i % 2 != 0) {
            sum += i;
        }
    }
    printf("\nSum of odd numbers in the range: %d", sum);
}

int main() {
    int start, end;
    int (*indirect_func)(int, int); // Function pointer (to point to other functions for indirect calls)

    // Get input range
    printf("Please enter the starting and ending values of the range in seperate inputs\n");
    printf("\nEnter the starting number in the range: ");
    scanf("%d", &start);
    printf("\nEnter the end number in the range: ");
    scanf("%d", &end);

    // Choose processing function based on user input
    printf("\nEnter type of numbers to process (1: add all even numbers, 2: add all odd numbers): ");
    int choice;
    scanf("%d", &choice);
    
    //indirectly calling even handling function using indirect_func
    indirect_func = even_func;
    printf("\nEven numbers in the range:");
    indirect_func(start, end);
    
    //indirectly calling odd handling function using indirect_func
    indirect_func = odd_func;
    printf("\nOdd numbers in the range:");
    indirect_func(start, end);

    // if choice is even, indirectly call the function to handle add even 
    if (choice == 1) {
        indirect_func = add_even;
    } else if (choice == 2) {
        indirect_func = add_odd; // if choice is odd, indirectly call the function to handle odd odd
    } else {
        printf("\nInvalid choice! (enter 1: for even addition. 2: for odd additon.)");
        return 1; 
    }

    // Indirect calls using pointers (according to the input condition)
    indirect_func(start, end);

    return 0;
}
