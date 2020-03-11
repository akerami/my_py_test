import os, sys, pprint
import mypy

from mypy import api

result = api.run(["analysis-test.py"])
if result[0]:
    print('Type checking report:')
    print(result[0])  # stdout
if result[1]:
    print('Error report:')
    print(result[1])  # stderr
print('Exit status:', result[2])
