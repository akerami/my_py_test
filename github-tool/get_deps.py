'''
 First do:
    pip install ghtopdep
    pip install openpyxl
'''

import json
from openpyxl import Workbook

def get_parsable_json_string(output_given):
    res = ""
    is_there = False

    for i in str(output_given):
        if i == "[":
            is_there = True
        if i =="]":
            res += i 
            break
        if is_there:
            res += i
    return res


# Example command: (ghtopdep https://github.com/python/mypy --json --rows 20000 --minstar 0)

library_address = "https://github.com/python/mypy"
FILENAME = "sample.xlsx"

import subprocess
# Number repos to show is set to 1000000 in order to get all the repos, this method is chosen because there is not 
test = subprocess.Popen(["ghtopdep",library_address, "--json", "--rows", "1000000", "--minstar", "0"], stdout=subprocess.PIPE)
output = test.communicate()[0]

parsed_json_string = get_parsable_json_string(output)
out_dict = json.loads(parsed_json_string)

'''
    Write the dictionary to an Excel output file.
'''
def write_to_workbook(out_dict_param):
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active
    ws.append(["Repo URL", "Number of stars"])

    for item in out_dict_param:
        ws.append([item["url"], item["stars"]])

    # Save the file
    wb.save(FILENAME)

write_to_workbook(out_dict)






















