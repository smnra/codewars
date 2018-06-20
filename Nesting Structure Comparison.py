#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Nesting Structure Comparison.py 
@time: 2018/06/{DAY} 
描述: Nesting Structure Comparison
    Nesting Structure ComparisonComplete the function/method
    (depending on the language) to return true/True when its
    argument is an array that has the same nesting structure
    as the first array.

    For example:

    # should return True
    same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

    # should return False
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

    # should return True
    same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

    # should return False
    same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

Test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
Test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
"""


def same_structure_as(original,other):
    for i in range(len(original)):
        if type(original[i])==type(other[i])==type([]):
            return same_structure_as(original[i],other[i])
        elif type(original[i])!=type([]) or type(other[i])!=type([]):
            return False


    type(original[i])!=type([]) and type(other[i])!=type([]):

    return True


print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ),True)
print(same_structure_as([1,[1,1]],[2,[2,2]]), True)
print(same_structure_as([1,[1,1]],[[2,2],2]), False)

# should return True
print(same_structure_as([1, 1, 1], [2, 2, 2]),True)
print(same_structure_as([1, [1, 1]], [2, [2, 2]]),True)

# should return False
print(same_structure_as([1, [1, 1]], [[2, 2], 2]),False)
print(same_structure_as([1, [1, 1]], [[2], 2]),False)

# should return True
print(same_structure_as([[[], []]], [[[], []]]),True)

# should return False
print(same_structure_as([[[], []]], [[1, 1]]),False)