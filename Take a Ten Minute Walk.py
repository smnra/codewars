#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Take a Ten Minute Walk.py 
@time: 2018/06/{DAY} 
描述: Take a Ten Minute Walk
    You live in the city of Cartesia where all roads
    are laid out in a perfect grid. You arrived ten
    minutes too early to an appointment, so you
    decided to take the opportunity to go for a short
    walk. The city provides its citizens with a Walk
    Generating App on their phones -- everytime you
    press the button it sends you an array of one-letter
    strings representing directions to walk
    (eg. ['n', 's', 'w', 'e']). You always walk only a
    single block in a direction and you know it
    takes you one minute to traverse one city block,
    so create a function that will return true if the
    walk the app gives you will take you exactly ten
    minutes (you don't want to be early or late!)
    and will, of course, return you to your starting
    point. Return false otherwise.

    Note: you will always receive a valid array containing
    a random assortment of direction letters
    ('n', 's', 'e', or 'w' only). It will never give you
    an empty array (that's not a walk, that's standing still!).


    for i in range(2): # test as many times as you want, just change the number
        test1 = create_tests(random.randint(0,20))
        test.assert_equals(isValidWalk(test1[0]),test1[1])



"""
from numpy import array

def isValidWalk(walk):
    if len(walk)==10:
        result = array([0,0])
        action = {'n': array([1,0]), 's':array([-1,0]), 'e':array([0,1]), 'w':array([0,-1])}
        for d in walk:
            if d in "nsew":
                result += action[d]
        return (result==array([0,0])).all()
    else:
        return False






def isValidWalk_best(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



print(isValidWalk(['n','e', 'e', 'e', 'e','s','w', 'w', 'w', 's']))
print(isValidWalk(['n','e', 'e', 'e', 'e','s','w', 'w', 'w', 'w']))
print(isValidWalk(['n','e', 'm', 'e', 'e','s','w', 'w', 'w', 'w']))









