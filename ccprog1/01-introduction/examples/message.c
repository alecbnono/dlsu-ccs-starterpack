#include <stdio.h>            // Preprocessor directive: includes standard I/O functions

#define MESSAGE "Hello CCPROG1! " // Macro definition: defines a constant MESSAGE

// Function definition: user-defined function that prints MESSAGE
void displayMessage() {
    printf(MESSAGE);          // Statement: prints the macro string
}

// Main function: program execution starts here
int main(void)
{
    displayMessage();         // Function call: executes displayMessage()
    printf("See you soon!\n");  // Another statement printing text
    return 0;                 // Return statement: signals successful termination
}
