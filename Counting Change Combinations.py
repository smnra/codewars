#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Counting Change Combinations.py 
@time: 2018/06/{DAY} 
描述: Counting Change Combinations
        Write a function that counts how many different ways you can make
     change for an amount of money, given an array of coin denominations.
     For example, there are 3 ways to give change for 4 if you have coins
     with denomination 1 and 2:

    1+1+1+1, 1+1+2, 2+2.
    The order of coins does not matter:

    1+1+2 == 2+1+1
    Also, assume that you have an infinite amount of coins.

        Your function should take an amount to change and an array of unique
    denominations for the coins:

    count_change(4, [1,2]) # => 3
    count_change(10, [5,2,3]) # => 4
    count_change(11, [5,7]) # => 0

test.assert_equals(3, count_change(4, [1,2]))
test.assert_equals(4, count_change(10, [5,2,3]))
test.assert_equals(0, count_change(11, [5,7]))



"""
from itertools import *

def count_change1(money, coins):
    coins.sort()
    combs = []
    elements = []
    source = [[coin]*(money//coin) for coin in coins if money>=coin]
    for element in source: elements = elements + element
    for n in range(money//coins[-1],money//coins[0] +1):        # 解决方案中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
        for comb in set(combinations(elements, n)):                  # 每种n 可能的 元素组合方式
            if sum(comb)==money:
                combs.append(comb)
                #print(comb)
    return len(combs)



def count_change2(money, coins):
    coins.sort()
    combs = []
    elements = []
    source = [[coin]*(money//coin) for coin in coins if money>=coin]
    for element in source: elements = elements + element
    for n in range(money//coins[-1],money//coins[0] +1):        # 解决方案中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
        combs = combs + [comb for comb in set(combinations(elements, n)) if sum(comb)==money]                 # 每种n 可能的 元素组合方式
    return len(combs)



def count_change3(money, coins):
    coins.sort()
    combs = []
    for n in range(money//coins[-1],money//coins[0] +1):        # 解决方案中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
        for comb in set(combinations_with_replacement(coins, n)):
            if sum(comb)==money:
                combs.append(comb)
                print(comb)
    return len(combs)

def count_change4(money, coins):
        combs = []
        for n in range(money // max(coins), money // min(coins) + 1):  # 解决方案中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
            for comb in set(combinations_with_replacement(coins, n)):
                if sum(comb) == money: combs.append(comb)
        return len(combs)



from itertools import combinations_with_replacement
def count_change(money, coins):
        combs = []
        for n in range(money//max(coins), money//min(coins)+1):  # 解决方案中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
            combs = combs + [comb for comb in set(combinations_with_replacement(coins, n)) if sum(comb) == money]
        return len(combs)



    #
print(3, count_change(4, [1,2]))
print(4, count_change(10, [5,2,3]))
print(0, count_change(11, [5,7]))


print(count_change(40, [1,5,2,3]))








