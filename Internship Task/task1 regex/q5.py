"""
Write a pattern which identifies if a string is a valid python
variable

 is_valid_variable('first_name') # True
 is_valid_variable('first-name') # False
 is_valid_variable('1first_name') # False
 is_valid_variable('firstname') # True
"""
import re
def valid_variable(s):
    pattern = r'[a-zA-Z_][a-zA-Z0-9_]+$'
    match = re.match(pattern, s)
    if match:
        return True
    else:
        return False
s = input()
print(valid_variable(s))