#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Delete occurrences of an element if it occurs more than n times.py 
@time: 2018/05/{DAY} 
描述: Delete occurrences of an element if it occurs more than n times


    Enough is enough!
        Alice and Bob were on a holiday. Both of them took many pictures of the places they've been,
    and now they want to show Charlie their entire collection. However,
    Charlie doesn't like this sessions, since the motive usually repeats.
    He isn't fond of seeing the Eiffel tower 40 times.
    He tells them that he will only sit during the session if they show the same motive at most N times.
    Luckily, Alice and Bob are able to encode the motive as a number.
    Can you help them to remove numbers such that their list contains each number only up to N times,
    without changing the order?

    Task
        Given a list lst and a number N, create a new list that contains each number
    of lst at most N times without reordering. For example if N = 2, and the input
    is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would
    lead to 1 and 2 being in the result 3 times, and then take 3,
    which leads to [1,2,3,1,2,3].

    Example
    delete_nth ([1,1,1,1],2) # return [1,1]

    delete_nth ([20,37,20,21],1) # return [20,37,21]
    delete_nth([20,37,20,21], 1) #, [20,37,21])
    delete_nth([1,1,3,3,7,2,2,2,2], 3) #, [1, 1, 3, 3, 7, 2, 2, 2])
"""




def delete_nth2(order,max_e):
    order.reverse()  # 反转列表 order
    for _i in order :
        for n in order :            #遍历列表
            if order.count(n) > max_e :     #如果元素n 在 nlist中出现的次数大于 max_e
                order.remove(n)
                break
    order.reverse()         # 反转列表 nlist
    return  order





def delete_nth(order,max_e):
    maxCount = not order or max([[order.count(m), m] for m in order])
    if maxCount==True or maxCount[0]<=max_e :
        return order
    else :
        order.reverse()  # 反转列表 nlist
        order.remove(maxCount[1])
        order.reverse()  # 反转列表 nlist
        return delete_nth(order,max_e)





print(delete_nth ([], 5))
print(delete_nth ([20,37,20,21],1), '20,37,21')
print(delete_nth([20,37,20,21], 1), '20,37,21')
print(delete_nth([1,1,3,3,7,2,2,2,2], 3) , '1, 1, 3, 3, 7, 2, 2, 2')



def delete_nth_Best(order,max_e):
    return [order[i] for i in range(len(order)) if order[0:i+1].count(order[i]) <= max_e]