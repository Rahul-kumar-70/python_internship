"""
Q2:Write a function to check weather email is valid or invalid
"""
def email_check(s):
    import re
    pattern = r'([a-zA-Z0-9_.+-])([a-zA-Z0-9_.+-]+)(@)([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    ma= re.search(pattern, s)
    if ma :
        return 'valid'
    else:
        return  'invalid'
s = input()
print(email_check(s))
