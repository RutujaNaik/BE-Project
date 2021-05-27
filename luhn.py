# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:21:19 2020

@author: harsh
"""

# implementing atm module


import math
from QR_scan_read import scan_read  

def bits_ip(cno):
# taking mii input from user
    mii = input("Enter the MII> ")

# getting the card 14 bits
# this will be scanned by the machine from the phone
    mb = cno
    
    a = str(mii)
    b = str(mb)
    full = a + b        # at this point the full card number is in string format
    
    luhn(full)          # string card number is passed to luhn to calculate cheksum and validate it
    
# luhn algo
def luhn(full):
    c = full
    bits = list(map(int, c))           # a list to store every bit of the card number as individual elements
    odd_sum = 0
    even_sum = 0
    total = 0           # sum of odd and even bits
        
#    print(bits)
    
    for i in range(0, len(bits)):
        
        if i == 0 or i % 2 == 0:
            even = bits[i] * 2
            if even > 9:
                even1 = even % 10
                even2 = math.trunc(even / 10) 
                add = even2 + even1
                even_sum += add
            else:
                even_sum += even 
        else:
            odd_sum += bits[i]
            

    total = odd_sum + even_sum

# validation and calulation of the checksum     
    pre_check = total % 10
    if pre_check == 0:
        luhn_bit = 0
    else:
        luhn_bit = 10 - pre_check
#    print("luhn_bit = ", luhn_bit) 
    
    if (pre_check + luhn_bit) != 10:
        print("something went wrong, try again")
        bits_ip()
    else:
        generate(full, luhn_bit)
    

# genning full no.
def generate(full, luhn_bit):
    l = str(luhn_bit)
    n = full
    
    c_num = n + l
    print("complete number =", c_num)  

def start():
    print("Welcome!")
    scan_read()
    
start() 