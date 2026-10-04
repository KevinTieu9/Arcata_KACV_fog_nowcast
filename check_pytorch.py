#!/usr/bin/env python3
"""
check_pytorch.py
Arcata KACV fog nowcast

Author: Kevin Tieu

"""


def print_laptop_notes():
    print("laptop=Ryzen_7_8745HS")
    print("gpu_expected=Radeon_780M")
    print("cuda_expected=no")
    print("default_device=cpu")


def print_torch_info():
    try:
        import torch
    except ImportError:
        print("torch=not_installed")
        return
    print("torch=" + torch.__version__)
    print("cuda_available=" + str(torch.cuda.is_available()))
    xpu_is_available = False
    if hasattr(torch, "xpu"):
        try:
            xpu_is_available = bool(torch.xpu.is_available())
        except Exception:
            xpu_is_available = False
    print("xpu_available=" + str(xpu_is_available))
    print("device=cpu")
    sample = torch.zeros(2, 3)
    print("tensor_sum=" + str(float(sample.sum())))


def main():
    print("python_ok")
    print_laptop_notes()
    print_torch_info()


if __name__ == "__main__":
    main()
