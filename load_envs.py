#!/usr/bin/env python3

import os

with open("rw.env") as f:
    lines = f.readlines()
    for l in lines:
        os.system(f"railway variables --set '{l}'")