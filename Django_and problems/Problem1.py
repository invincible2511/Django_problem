""" Implement a group_by_owners function that:
-- accepts a dict containing the file owner name for each file name.
-- Returns a dict containing a list of file names for each owner name, in any order.
For eg: {
 'Input.txt': 'Randy',
 'Code.py': 'Stan',
 'Output.txt': 'Randy'
 } 
the group_by_owners function should return {“randy”: [“input.txt”, “output.txt”], “stan”: [“code.py”]} """

# Solution

from collections import defaultdict


def group_by_owners(file):
    owners = defaultdict(list)
    for file, owner in file.items():
        owners[owner].append(file)
    return owners


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))