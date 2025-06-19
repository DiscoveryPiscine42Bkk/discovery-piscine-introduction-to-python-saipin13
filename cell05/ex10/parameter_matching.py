#!/usr/bin/env python3
import sys

args = sys.argv[1:]  # ตัด index 0 ที่เป็นชื่อไฟล์ออก

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for param in args:
        print(f"{param}: {len(param)}")