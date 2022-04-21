""""
Made by 0xHaris
"""
import pyperclip as pc
import re

def input(filename):
    with open(filename, 'r') as f:
        pc.copy("".join(f.readlines())) #copying the file content to the clipboard
    return pc.paste()
def phone_extractor(content):

    phone_regex = re.compile(r"""(  #regex for US-based phone numbers
    (\d{3}|\(\d{3}\))?       #areacode
    (\s|-|\.)?               #seperator
    \d{3}                   #first 3 digits
    (\s|-|\.)               #seperator
    \d{4}                   #last 4 digits
    )""", re.VERBOSE | re.DOTALL)
    mo = phone_regex.findall(str(content)) # make a list of numbers found
    return mo


print(phone_extractor(input("essay.txt")))