# Terminal Basics (Windows Command Prompt & macOS Terminal)

This guide covers the essential terminal commands you’ll need for **CCPROG1** and general programming work.  
It includes examples for **Windows** (Command Prompt) and **macOS** (Terminal), focusing on navigation, viewing files, running programs, and using input/output redirection.

---

## 1. Opening the Terminal

- **Windows**: Press `Win + R`, type `cmd`, and press Enter.
- **macOS**: Press `Cmd + Space`, type `Terminal`, and press Enter.

---

## 2. Navigating Directories

### Show Current Directory

- Windows:

```cmd
  cd
```

- macOS:

```bash
  pwd
```

### Change Directory

- Windows:

```cmd
  cd path\to\folder
```

- macOS:

```bash
  cd /path/to/folder
```

### Go Up One Directory

- Windows & macOS:

```bash
  cd ..
```

---

## 3. Viewing Files and Folders

- Windows:

```cmd
  dir
```

- macOS:

```bash
  ls
```

Add options for macOS:

- `ls -l` → detailed list
- `ls -a` → include hidden files

## 4. Running Programs

- Windows:

```cmd
  programname.exe
```

- macOS:

```bash
  ./programname
```

---

## 5. Input and Output Redirection

### Redirect Output to a File

- Windows:

```cmd
  programname.exe > input.txt
```

- macOS:

```bash
  ./programname > input.txt
```

### Redirect Input from a File

- Windows:

```cmd
  programname.exe < input.txt
```

- macOS:

```bash
  ./programname < input.txt
```

### Combine Input and Output Redirection

- Windows:

```cmd
  programname.exe < input.txt > output.txt
```

- macOS:

```bash
  ./programname < input.txt > output.txt
```

## 6. Clearing the Screen

- Windows:

```cmd
  cls
```

- macOS:

```bash
  clear
```

---

## 7. Using Tab for Auto-Completion

- Press **Tab** while typing a **command** to let the terminal auto-complete it.
  - Example: typing `gc` + Tab → `gcc` (if installed).
- Press **Tab** while typing a **filename or folder name** to complete it automatically.
  - Example: typing `mes` + Tab → `message.c`.
- If there are multiple matches, press **Tab** twice to see a list of all possible completions.

This saves time and helps avoid typos when working with commands and files.

---

## 8. Using Command History

- Press the **Up Arrow** ↑ to cycle through your previously entered commands.
- Press the **Down Arrow** ↓ to move forward in the history.
- This is especially useful when you need to re-run long commands (like compilation) without typing them again.

Instead of typing `gcc message.c -o message.exe` again, just press ↑ and hit **Enter**.
