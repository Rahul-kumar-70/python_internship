"""
Q1:Write a function to mask email address
Input:mayurkulkarni636@gmail.com
Output:m###############@gmail.com
"""
import re
def email_address(s):
    m = r'([a-zA-Z0-9_.+-])([a-zA-Z0-9_.+-]+)(@)([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    match = re.search(m, s)
    return  match.group(1) + '#' * len(match.group(2)) + match.group(3)+match.group(4)
s = 'user+tag@domain.co.in'
print(email_address(s))
