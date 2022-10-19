
from dataclasses import replace
from pickletools import int4
from string import digits

Digits= input('Enter the numnbers? ')
for digit in Digits:
    if digits == "0":
        digit = Digits.replace('0','x')
        break
    print(digit)