# Tokens and Expressions in C

In C, programs are written using **tokens**. Tokens combine to form **expressions**, which are the building blocks of all computations.

---

## Tokens in C

A **token** is the smallest unit of a program that the compiler can understand.

### Types of Tokens:

1. **Keywords** – Reserved words in C (e.g., `int`, `return`, `if`, `while`).
2. **Identifiers** – Names for variables, functions, etc. (e.g., `age`, `sum`, `main`).
3. **Constants** – Fixed values (e.g., `10`, `3.14`, `'A'`).
4. **Operators** – Symbols that perform actions (e.g., `+`, `-`, `*`, `/`).
5. **Punctuation (Separators)** – Characters like `;`, `{}`, `()`, `,`.

**Example:**

```c
int age = 20;
printf("Age: %d\n", age);
```

Here:

- `int` → keyword
- `age` → identifier
- `20` → constant
- `=` → operator
- `;` → punctuation

---

## Expressions in C

An **expression** is a combination of variables, constants, and operators that produces a value.

### Arithmetic Expressions

- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a * b`
- Division: `a / b`
- Modulus: `a % b` (remainder)

### Operator Precedence

Some operators are evaluated before others:

- `*`, `/`, `%` are evaluated before `+`, `-`.
- Use parentheses `()` to control the order.
- (Operator precedence has a lot of parallels with PEMDAS!)

Full list/chart of operator precedence can be found [here](https://en.cppreference.com/w/c/language/operator_precedence.html)

**Example:**

```c
int a = 10, b = 3;
int result = a + b * 2;  // result = 10 + (3*2) = 16
printf("%d\n", result);
```

---

## Summary

- **Tokens** are the smallest elements in C (keywords, identifiers, constants, operators, punctuation).
- **Expressions** combine tokens to perform calculations.
- Understanding these is essential before learning **variables, input/output, and conditionals**.
