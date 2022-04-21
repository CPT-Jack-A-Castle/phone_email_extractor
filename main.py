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
    (\d{3})                   #first 3 digits
    (\s|-|\.)               #seperator
    (\d{4})                   #last 4 digits
    )""", re.VERBOSE | re.DOTALL)
    mo = phone_regex.findall(str(content)) # make a list of numbers found
    return mo

def email_extractor(content):
    email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username
    @               #@symbol
    [a-zA-Z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4})  #dot-something  
    )''', re.VERBOSE)
    mo2 = email_regex.findall(content)
    return mo2

text = input("essay.txt")
matches = []
for groups in phone_extractor(text):
    print(groups)
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
for groups in email_extractor(text):
     matches.append(groups[0])
