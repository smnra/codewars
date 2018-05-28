#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Delete occurrences of an element if it occurs more than n times.py 
@time: 2018/05/{DAY} 
描述: 

    Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')

# list.count(obj)
# 统计某个元素在列表中出现的次数
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置

"""



def high(x):
    wordList = x.split(" ")
    scores = list(range(len(wordList)))
    max = 0
    maxIndex = 0
    for i,word in enumerate(wordList) :
        for s in word :
            scores[i] = scores[i] + (ord(s) - 96)
        if scores[i] >= max :
            maxIndex = i
            max = scores[i]
    return wordList[maxIndex]



def strScore(x):
    str = 0
    m = []
    for s in x :
        if ord(s) > 96:
            print((ord(s) - 96),s)
            m.append((ord(s) - 96))
            str = str + (ord(s) - 96)
    return str


print(strScore('kuexvxtsw'), strScore('hyycbpxyxq'))
print(strScore('vrhnqusr'), strScore('axqjlmyqs'))
print(strScore('tltbjonz'), strScore('lsbsaotgz'))

print(high('kuexvxtsw hyycbpxyxq'), 'hyycbpxyxq')
print(high('vrhnqusr axqjlmyqs'), 'axqjlmyqs')
print(high('tltbjonz lsbsaotgz'), 'lsbsaotgz')







