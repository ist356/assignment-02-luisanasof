'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code
from packaging import parse_packaging, calc_total_units, get_unit
#parse_packaging takes str as input
#other two functions take dictionary 

import json

filename = "data/packaging.txt"
packages = []

with open(filename, "r") as f:
    contents = f.readlines()
    #readlines?
    #read function reads each character, readlines reads each line
    for line in contents: 
        parsed_packaging = parse_packaging(line)
        total_units = calc_total_units(parsed_packaging)
        unit = get_unit(parsed_packaging)
        print(f"{line} => total units: {total_units} {unit}")
        packages.append(parsed_packaging)
        #saving as json to file:
        with open("data/packaging.json", "a") as f:
            json.dump(packages, f, indent=4)