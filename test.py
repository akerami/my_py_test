import sys
import os
from mypy import api

os.chdir("/mnt/hgfs/mypy/")
print(os.getcwd())

result = api.run(["setup.py"])
if result[0]:
    print('\nType checking report:\n')
    print(result[0])  # stdout
if result[1]:
    print('\nError report:\n')
    print(result[1])  # stderr
print('\nExit status:', result[2])
