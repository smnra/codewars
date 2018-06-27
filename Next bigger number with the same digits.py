#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Next bigger number with the same digits.py 
@time: 2018/06/{DAY} 
描述: Next bigger number with the same digits


        You have to create a function that takes a positive
    integer number and returns the next bigger number
    formed by the same digits:

    next_bigger(12)==21
    next_bigger(513)==531
    next_bigger(2017)==2071
    If no bigger number can be composed using those digits, return -1:

    next_bigger(9)==-1
    next_bigger(111)==-1
    next_bigger(531)==-1


Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)



"""

def next_bigger1(n):
    n = list(str(n)[::-1])
    if len(n)>=2:
        for i in range(1,len(n)):
            if int(n[i-1]) > int(n[i]) :
                n[i-1], n[i] = n[i], n[i-1]
                return int("".join(n[::-1]))
    return -1


from itertools import permutations

def next_bigger(n):
    n = list(str(n))
    if len(n)>=2:
        for i in range(len(n)-1):
            if n[-i-1] > n[-i-2]:
                tmpList = n[-i-2:]
                optList = list(permutations(tmpList, len(tmpList)))
                optList.sort(key=lambda x : x[0])
                for m in optList:
                    if int("".join(tmpList)) < int("".join(m)):
                        return  "".join(n).replace("".join(n[-i-2:]),"".join(m))
    return -1








print(next_bigger(1234567890),1234567908)
print(next_bigger(59884848495853),59884848483559)
print(next_bigger(1049116763807),1049116763708)
print(next_bigger(499897),499789)

print(next_bigger(513),531)
print(next_bigger(2017),2071)

print(next_bigger(111) , -1)
print(next_bigger(531) , -1)

print(next_bigger(9) , -1)
print(next_bigger(414),441)
print(next_bigger(414),441)
print(next_bigger(144),414)

