# Installing GCC on Windows (via Chocolatey Package Manager)

This guide shows you how to install **GCC** using **Chocolatey**, which is one of the easiest ways to get a working compiler for **CCPROG1**.

## on Windows (via Chocolatey Package Manager)

### 1. Install Chocolatey

Follow the instructions on the official [Chocolatey website](https://chocolatey.org/install)

Make sure you:

- Run the installation in **PowerShell as Administrator**.
- Close and reopen your terminal after installing.

### 2. Install MinGW via Chocolatey

1. Open **PowerShell as Administrator**.
2. Run:

   ```powershell
   choco install mingw -y
   ```

### 3. Refresh Environment Variables

After installation, run:

```powershell
refreshenv
```

If refreshenv is not available, just close and reopen your terminal or log out and back in.

### 4. Verify GCC Installation

Run:

```powershell
gcc --version
```

---

## macOS Installation (via Homebrew)

### 1. Install Homebrew

Follow the instructions on the official [Homebrew website](https://brew.sh)

Make sure you:

- Run the installation in **Terminal**.
- Follow any prompts to add Homebrew to your PATH.

### 2. Install GCC via Homebrew

Run:

```bash
brew install gcc
```

### 3. Verify GCC Installation

Run:

```bash
gcc --version
```

You should see GCC’s version information.  
If you see `Apple clang` instead, you may need to run `brew info gcc` to find the correct GCC executable name (for example, `gcc-14`) and use that in your compilation commands.

✅ Once installed on either platform, you can follow the **Using GCC** tutorial to compile and run your programs.
