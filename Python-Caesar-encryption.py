#!/usr/bin/python
# Python Caesar encryption

"""
Usage: Python-Caesar-encryption.py

A simple encryption technique based on
substitution cipher. A left shift of 3 
is used here for both letters and numbers

Options
-------

-h or help Displays this message
"""

import string
from sys import argv, exit

baseAlphabetsLower = string.ascii_lowercase
baseAlphabetsUpper = string.ascii_uppercase
baseNumbers = range(0, 10)
finalString = []

if len(argv) > 1:
    print(__doc__)
    exit(0)

userString =  raw_input("Enter your alphanumeric characters: ")

for char in userString:
    if char == " ":
        finalString.append(char)
    else:
        if char in baseAlphabetsLower:
            charIndexLower = baseAlphabetsLower.index(char)
            finalString.append(baseAlphabetsLower[charIndexLower - 3])
        elif char in baseAlphabetsUpper:
            charIndexUpper = baseAlphabetsUpper.index(char)
            finalString.append(baseAlphabetsUpper[charIndexUpper - 3])
        else:
            numIndex = baseNumbers.index(int(char))
            finalString.append(str(baseNumbers[numIndex - 3]))

encryptedString = "".join(finalString)
print "Your encrypted characters: ", encryptedString


