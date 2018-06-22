#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Perimeter of squares in a rectangle.py 
@time: 2018/06/{DAY} 
描述: Perimeter of squares in a rectangle
        The drawing shows 6 squares the sides of which have
    a length of 1, 1, 2, 3, 5, 8. It's easy to see that
    the sum of the perimeters of these squares is :
    4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

        Could you give the sum of the perimeters of all the
    squares in a rectangle when there are n + 1 squares
    disposed in the same manner as in the drawing:



        alternative text
    #Hint: See Fibonacci sequence
    #Ref: http://oeis.org/A000045

        The function perimeter has for parameter n where n + 1
    is the number of squares (they are numbered from 0 to n)
    and returns the total perimeter of all the squares.

    perimeter(5)  should return 80
    perimeter(7)  should return 216



test.assert_equals(perimeter(5), 80)
test.assert_equals(perimeter(7), 216)
test.assert_equals(perimeter(20), 114624)
test.assert_equals(perimeter(30), 14098308)
test.assert_equals(perimeter(100), 6002082144827584333104)

4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

1 + 1 + 2 + 3 + 5 + 8 + 13

"""


def perimeter1(n):
    fibonacci = [1,1]
    for m in range(n-1):
        fibonacci.append(sum(fibonacci[-2:]))
    return sum(fibonacci)*4


def perimeter(n):
    fibonacci = [1,1]
    [fibonacci.append(sum(fibonacci[-2:])) for m in range(n-1)]
    return sum(fibonacci)*4

print(perimeter(5), 80)
print(perimeter(7), 216)
print(perimeter(20), 114624)
print(perimeter(30), 14098308)
print(perimeter(100), 6002082144827584333104)


















