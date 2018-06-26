#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Extract the domain name from a URL.py 
@time: 2018/06/{DAY} 
描述: Extract the domain name from a URL

        Write a function that when given a URL as a string, parses out
    just the domain name and returns it as a string. For example:

    domain_name("http://github.com/carbonfive/raygun") == "github"
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"

    # TODO: Replace examples and use TDD development by writing your own tests
    # These are some of the methods available:
    #   test.expect(boolean, [optional] message)
    #   test.assert_equals(actual, expected, [optional] message)
    #   test.assert_not_equals(actual, expected, [optional] message)

    # You can use Test.describe and Test.it to write BDD style test groupings


"""

import re

def domain_name1(url):
    matchObj = re.match(r'https?:\/\/w?w?w?\.?(.+?)\..+\/?', url, re.I)
    return matchObj.group(1)


import re
def domain_name(url):
    return re.match(r'h?t?t?p?s?:?\/?\/?w?w?w?\.?(.+?)\..+\/?', url, re.I).group(1)


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))






