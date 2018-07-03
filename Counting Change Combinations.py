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
import timeit

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




def count_change5(money, coins):
        combs = []
        for n in range(money//max(coins), money//min(coins)+1):  # 解决方案中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
            combs = combs + [comb for comb in set(combinations_with_replacement(coins, n)) if sum(comb) == money]
        return len(combs)


def count_change(money, coins):
    coins.sort()


    def pos(value,list):
        '''
        此函数使用查找 list 列表中上一个小于或等于value的 元素的索引
        :param value: 数值
        :param list: 数值
        :return: list 的 索引
        '''
        list.append(value)
        if value==list[-1]: index = -1
        else: index = list.sort().index(value)
        return index



    for gongNWei in range(money // max(coins), money // min(coins) + 1):  # 解决方案中的列表中有可能有n个元素,n 为 money//coins[0] 到 money//coins[-1]
        result = []
        tempCoins = list(coins)  # 复制一份coins
        for n in range(len(gongNWei)):  # 当解决方案中的列表中的元素为 gongNWei 位时, 遍历解决方案中的列表的每一个元素 元素索引为 n
            result.append(tempCoins[n])  # 将 tempCoins 的第1 个元素 添加到 result 列表中
            a = pos(tempCoins[n], tempCoins)  # 确定 可能是第 n 位的数字 的 列表的开始 索引
            b = pos(money - sum(result), tempCoins)  # 确定 可能是第 n 位的数字 的 列表的结束 索引
            for diNWei in tempCoins[a:b + 1]:  # 遍历 可能是第 n 位的数字的列表
                if (money - sum(result) - diNWei) >= diNWei:  # 如果  money 减去sum(resule) 再 减去 diNWei 大于 下一个最小元素
                    pass
        return 0





"""
10
[2,3,4,5,6,7,8,9]

[2,8] [3,7] [4,6] ,[5,5]
[2,2,6] [2,3,5] [2,4,4] [3,3,4]
[2,2,2,4] [2,2,3,3]
[2,2,2,2,2]


"""

start = timeit.default_timer()
print(count_change5(10, [2,3,4,5,6,7,8,9]))
end = timeit.default_timer()
print(str(end-start))


start = timeit.default_timer()
print(count_change5(60, [1,5,2,3]))
end = timeit.default_timer()
print(str(end-start))


