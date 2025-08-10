# Development Tools Setup 🛠

This section of the **DLSU CCS Starter Pack** covers all the essential tools you’ll need for **CCPROG1** and beyond.  
The goal is to make sure you can write, compile, and run C programs using **GCC** — the standard compiler for this course.

## 📋 Required Tools

### Text Editors / IDEs

You need a way to write your C code. Recommended options (covered in one guide):

- **[Text Editors & IDEs Setup](./text-editors.md)** — Includes:
  - Visual Studio Code (Windows & macOS)
  - Dev-C++ (Windows)

---

### Compiler

**GCC** — The standard C compiler for CCPROG1.

- Bundled with Dev-C++ (Windows)
- Installed via **Chocolatey** for Windows
- Installed via **Homebrew** (macOS)

Follow the editor/IDE setup guide above to ensure GCC is installed correctly.

---

### Terminal / Command Line

You’ll need basic terminal skills to compile and run C programs outside your IDE:

- **[Terminal Basics](./terminal-basics.md)** — Navigate folders, compile with `gcc`, run programs.
- Works on:
  - Command Prompt / PowerShell (Windows)
  - Terminal.app (macOS)

---

### Compiling & Running with GCC

Learn the commands you’ll use most often in CCPROG1:

- **[Compiling with GCC](./compiler.md)** — Step-by-step guide for Windows & macOS.
- Covers:
  - Compiling single-file programs
  - Running executables
  - Common compiler errors and fixes

---

## 📚 Recommended Order for Setup

1. Install your text editor or IDE → [Text Editors & IDEs Setup](./text-editors.md)
2. Install compiler (GCC) → [GCC Install](./compiler-install.md)
3. Learn basic **terminal commands** → [Terminal Basics](./terminal-basics.md)
4. Practice compiling → [Compiling with GCC](./compiler.md)

## 💡 Pro Tips

- Keep all your `.c` files organized in a dedicated folder for CCPROG1.
- Test compiling from both your IDE **and** the terminal — you’ll need both skills.
- Always compile with the following flags enabled:
  ```bash
  gcc -Wall -std=c99 filename.c -o output
  ```
