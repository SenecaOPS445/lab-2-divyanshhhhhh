#!/usr/bin/env python3
#Author: Divyansh Pandya
#Author ID: 161112214
#Date Created: 2025-01-24
import sys

if len(sys.argv) != 2:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1
    
print('blast off!')
