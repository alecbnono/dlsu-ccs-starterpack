# Using GCC to Compile C Programs (Windows & macOS)

This guide will show you how to compile and run C programs in **CCPROG1** using the **GCC** compiler.  
The instructions apply to:

- **Windows** — Command Prompt or PowerShell
- **macOS** — Terminal

---

## 1. Create Your C File

Save your program as a `.c` file. Example: `hello.c`

```c
#include <stdio.h>

int main(void) {
    printf("Hello, CCPROG1!\n");
    return 0;
}
```

---

## 2. Open Your Terminal

- **Windows**:  
  Open **Command Prompt**
  Use `cd` to navigate to the folder where your `.c` file is located:

  ```cmd
  cd path\to\your\folder
  ```

- **macOS**:  
  Open **Terminal**.  
  Use `cd` to navigate to your file’s folder:
  ```bash
  cd /path/to/your/folder
  ```

---

## 3. Compile with GCC

Run the following command in your terminal:

```
gcc -Wall -std=c99 hello.c -o hello
```

**Explanation of flags:**

- `-Wall` → Enables common warnings to help catch mistakes early.
- `-std=c99` → Uses the C99 standard, which is the standard for CCPROG1.
- `hello.c` → The source code file.
- `-o hello` → Sets the output file name to `hello` (without extension).

If there are no errors, this command creates a compiled program:

- On **Windows**: `hello.exe`
- On **macOS**: `hello` (no extension)

---

## 4. Run Your Program

- **Windows**:

```cmd
hello.exe
```

- **macOS**:

```bash
./hello
```

Expected output:

```
Hello, CCPROG1!
```

---

✅ You are now ready to compile and run C programs for CCPROG1 on both Windows and macOS!
