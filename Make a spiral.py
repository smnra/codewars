#!usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author:Administrator
@file: Make a spiral.py
@time: 2018/07/{DAY}
描述: Make a spiral
        Your task, is to create a NxN spiral with a given size.
    For example, spiral with size 5 should look like this:

    00000
        11110
    00010
        01110
    00000

    and with the size 10:

    0000000000
    1111111110
    0000000010
    0111111010
    0100001010
    0101101010
    0101111010
    0100000010
    0111111110
    0000000000

        Return value should contain array of arrays, of 0 and 1,
    for example for given size 5 result should be:

       [[1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

    Because of the edge-cases for tiny spirals, the size will be at least 5.

    General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


Test.assert_equals(spiralize(1), [[1]])
Test.assert_equals(spiralize(2), [[1,1],
                                  [0,1]])
Test.assert_equals(spiralize(3), [[1,1,1],
                                  [0,0,1],
                                  [1,1,1]])
Test.assert_equals(spiralize(5), [[1,1,1,1,1],
                                  [0,0,0,0,1],
                                  [1,1,1,0,1],
                                  [1,0,0,0,1],
                                  [1,1,1,1,1]])
Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                  [0,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,0,1],
                                  [1,0,0,0,0,1,0,1],
                                  [1,0,1,0,0,1,0,1],
                                  [1,0,1,1,1,1,0,1],
                                  [1,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,1,1]])

"""


def spiralize(size):
    if size<=0 : return []
    list_2 = [list(range(0,size)) for ioo in range(0,size)]
    for i in range(0,size):
        start = i
        end = size - i -1
        index = size - i -1
        value = (i+1) % 2

        setRowValue(list_2,start,start-1,end,value)               # 横

        setColValue(list_2, start, end, index, value)             # 竖

        setRowValue(list_2, end, start, end, value)               # 横

        setColValue(list_2, start + 2, end, start, value)         # 竖

    if size % 2 == 0:
        specialLocate = int(size/2)
        list_2[specialLocate][specialLocate -1 ] = 0

    return list_2


def setRowValue(list_t,i,s,e,value_t = 1):
    # 二维列表 list_t 的第i 个 元素 的 第s个元素开始 到 第e 个元素 的 值 设置为 value_t
    if s < 0:s=0
    list_len = len(list_t[i])
    index = 0
    for list_o in list_t[i]:
        if s<=index<=e :
            list_t[i][index] = value_t
        index+=1

def setColValue(list_t ,s,e,i,value_t = 1):
    # 二维列表 list_t 的第一维度元素 从 s 开始 到 e 结束
    # 其中 每一个元素 的 第 i 个 元素 的值 设为 value_t
    for list_o in list_t[s:e]:
        list_o[i] = value_t

for i in range(0,21):
    list_rect = spiralize(i)
    [print(row) for row in list_rect ]



