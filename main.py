import os, sys, pprint
from mypy import api

if __name__ == "__main__":
    result = api.run(["analysis-test.py"])
    if result[0]:
        print('Type checking report:')
        print(result[0])  # stdout
    if result[1]:
        print('Error report:')
        print(result[1])  # stderr
    print('Exit status:', result[2])
