#!/usr/bin/env python3
"""
check_laptop.py
CS 375 — Project 3 Arcata KACV fog nowcast

Author: Kevin Tieu

Print what this laptop looks like before any pip install.
"""

import os
import platform
import shutil
import subprocess


def run_command(command_words):
    try:
        result = subprocess.run(
            command_words,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return ""
    return (result.stdout or "") + (result.stderr or "")


def main():
    print("system=" + platform.system())
    print("machine=" + platform.machine())
    print("python=" + platform.python_version())
    print("which_python=" + (shutil.which("python3") or "missing"))
    print("which_gcc=" + (shutil.which("gcc") or "missing"))
    print("which_gxx=" + (shutil.which("g++") or "missing"))
    print("home=" + os.path.expanduser("~"))
    lspci_text = run_command(
        ["bash", "-lc", "lspci 2>/dev/null | grep -i -E 'vga|3d|display' || true"]
    )
    if lspci_text.strip():
        print("pci=")
        print(lspci_text.strip())
    else:
        print("pci=unavailable_here_run_on_the_laptop")
    print("note=Ryzen_7_8745HS_Radeon_780M_is_AMD_not_NVIDIA")
    print("note=install_CPU_torch_first")


if __name__ == "__main__":
    main()