#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Sum of the first nth term of Series.py 
@time: 2018/06/{DAY} 
描述: 
    Task:
    Your task is to write a function which returns
    the sum of following series upto nth term(parameter).

    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
    Rules:
    You need to round the answer to 2 decimal places and return it as String.

    If the given value is 0 then it should return 0.00

    You will only be given Natural Numbers as arguments.

    Examples:
    SeriesSum(1) => 1 = "1.00"
    SeriesSum(2) => 1 + 1/4 = "1.25"
    SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
    NOTE: In PHP the function is called series_sum().

1/(i*3-2)

Test.assert_equals(series_sum(1), "1.00")
Test.assert_equals(series_sum(2), "1.25")
Test.assert_equals(series_sum(3), "1.39")

"""


def series_sum1(n):
    if n:
        return "{:.2f}".format(sum([1/(i*3-2) for i in range(1,n+1)]))
    else:
        return "0.00"



def series_sum(n):
        return "{:.2f}".format(sum([1/(i*3-2) for i in range(1,n+1)]))



print(series_sum(0), type(series_sum(0)),"0.00")
print(series_sum(1), type(series_sum(1)),"1.00")
print(series_sum(2), type(series_sum(2)), "1.25")
print(series_sum(3), type(series_sum(3)), "1.39")
print(series_sum(453), type(series_sum(453)), "1.39")