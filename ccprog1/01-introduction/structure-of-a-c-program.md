# Structure of a C Program

Every C program follows a basic structure:

```c
#include <stdio.h>            // Preprocessor directive: includes standard I/O functions

#define MESSAGE "Hello CCPROG1! " // Macro definition: defines a constant MESSAGE

// Function definition: user-defined function that prints MESSAGE
void displayMessage()
{
    printf(MESSAGE);          // Statement: prints the macro string
}

// Main function: program execution starts here
int main(void)
{
    displayMessage();         // Function call: executes displayMessage()
    printf("See you soon!\n");  // Another statement printing text
    return 0;                 // Return statement: signals successful termination
}
```

---

## Parts of the Program

### 1. Preprocessor Directive

```c
#include <stdio.h>
```

- Tells the compiler to include the standard input/output library.
- Needed to use functions like `printf`.

### 2. Macro Definition

```c
#define MESSAGE "Hello CCPROG1!"
```

- Defines a constant called `MESSAGE`.
- During compilation, every `MESSAGE` in the code is replaced with `"Hello CCPROG1!"`.

### 3. Function Definition (User-defined)

```c
void displayMessage()
{
    printf(MESSAGE);
}
```

- Defines a reusable block of code.
- `displayMessage()` prints the `MESSAGE` string.

### 4. Main Function

```c
int main(void)
{
    displayMessage();
    printf("See you soon, DLSU CCS!\n");
    return 0;
}
```

- Every C program must have **one **``** function**.
- Program execution always begins here.

### 5. Function Call

```c
displayMessage();

```

- Runs the user-defined `displayMessage()` function.

### 6. Statements

```c
printf(MESSAGE);
printf("See you soon, DLSU CCS!\n");
```

- Instructions that output text to the screen.
- Each ends with a semicolon `;`.

### 7. Return Statement

```c
return 0;
```

- Indicates the program ended successfully.
- Returning a non-zero value usually means an error occurred.

---

## Comments and Documentation

Comments are ignored by the compiler but are important for explaining code. They help both you and others understand your program.

- **Single-line comment**: starts with `//`

  ```c
  // This is a single-line comment
  int age = 20; // Variable to store age
  ```

- **Multi-line comment**: enclosed in `/* ... */`

  ```c
  /*
   This program calculates the area of a rectangle.
   Author: Your Name
   Date: August 2025
  */
  ```

Comments can by stylized like so:

```c
/*
 * You can pad comments
 * like this
 */
```

```c
/************************
 * Or, you can box them *
 * around like this!    *
 ************************/
```

### Why Document Code?

- Makes programs & functions (more on this later) easier to read and maintain.
- Helps others (like professors or teammates) understand your thought process.
- Encouraged as part of good programming practice.

---

## Example: Hello World with proper documentation

```c
#include <stdio.h>   // Includes standard input/output functions

/*
 * Program: Hello World Example
 * Author: DLSU CCS Student
 * Description: A simple program that prints a message.
 */

int main(void) {     // Entry point of the program
    printf("Hello, DLSU CCS!\n");  // Prints text to the screen
    return 0;        // End of program
}
```

---

## Key Notes

- Without `#include <stdio.h>`, you cannot use `printf` or `scanf`.
- The **curly braces **`` group multiple statements together.
- Indentation is not required by the compiler but improves readability.
- The semicolon `;` is **mandatory** to end statements.
- Use comments to make your code clear and maintainable.
