#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Bit Counting.py 
@time: 2018/06/{DAY} 
描述: Bit Counting
    Write a function that takes an (unsigned) integer
    as input, and returns the number of bits that are
    equal to one in the binary representation of that
    number.

    Example: The binary representation of
    1234 is 10011010010, so the function
    should return 5 in this case


print(countBits(0), 0);
print(countBits(4), 1);
print(countBits(7), 3);
print(countBits(9), 2);
print(countBits(10), 2);
"""


def countBits(n):
    return str(bin(n)).count('1')




print(countBits(0), 0)
print(countBits(4), 1)
print(countBits(7), 3)
print(countBits(9), 2)
print(countBits(1234), 5)

