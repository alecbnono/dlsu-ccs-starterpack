# Installing GCC on Windows (via Chocolatey Package Manager)

This guide shows you how to install **GCC** using **Chocolatey**, which is one of the easiest ways to get a working compiler for **CCPROG1**.

## 1. Install Chocolatey

Follow the instructions on the official [Chocolatey website](https://chocolatey.org/install)

Make sure you:

- Run the installation in **PowerShell as Administrator**.
- Close and reopen your terminal after installing.

## 2. Install MinGW via Chocolatey

1. Open **PowerShell as Administrator**.
2. Run:

   ```powershell
   choco install mingw -y
   ```

## 3. Refresh Environment Variables

After installation, run:

```powershell
refreshenv
```

If refreshenv is not available, just close and reopen your terminal or log out and back in.

## 4. Verify GCC Installation

Run:

```powershell
gcc --version
```

If everything is installed correctly, you should see GCC’s version information.
