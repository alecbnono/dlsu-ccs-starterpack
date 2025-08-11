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
- macOS:

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

**Tip:** On both Windows and macOS, pressing the `↑` arrow cycles through previous commands.
