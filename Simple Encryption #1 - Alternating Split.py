#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Simple Encryption #1 - Alternating Split.py 
@time: 2018/05/{DAY} 
描述:
    For building the encrypted string:
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!

    Examples:

    "This is a test!", 1 -> "hsi  etTi sats!"
    "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
    Write two methods:

    def encrypt(text, n)
    def decrypt(encrypted_text, n)
    For both methods:
    If the input-string is null or empty return exactly this value!
    If n is <= 0 then return the input text.

    This kata is part of the Simple Encryption Series:
    Simple Encryption #1 - Alternating Split
    Simple Encryption #2 - Index-Difference
    Simple Encryption #3 - Turn The Bits Around
    Simple Encryption #4 - Qwerty

    Have fun coding it and please don't forget to vote and rank this kata! :-)

"""


def alternet(text):
    a = ''.join([text[i] for i in range(0, len(text), 2)])
    b = ''.join([text[i] for i in range(1, len(text), 2)])
    return b + a

def dealternet(encrypted_text):
    a = list(encrypted_text[:len(encrypted_text) // 2])
    b = list(encrypted_text[len(encrypted_text) // 2:])
    # print(a, len(a))
    # print(b, len(b))
    # print(b + a, len(b + a))
    # print(''.join([b[i] + a[i] for i in range(0, len(a))])[:-1])
    if len(encrypted_text) % 2 == 1:
        a.append(a[-1])
        return ''.join([b[i] + a[i] for i in range(0, len(a))])[:-1]
    else :
        return ''.join([b[i] + a[i] for i in range(0, len(a))])

def encrypt(text, n):
    m = max((n // abs(n) if n != 0 else 0) * (n % 4), 0)
    if n<= 0:
        return text
    elif n>= 1:
        tmp = alternet(text)
        return encrypt(tmp, n - 1)
    else:
        return alternet(text)

def decrypt(encrypted_text, n):
    m = max((n // abs(n) if n != 0 else 0) * (n % 4), 0)
    if n> 1:
        # print(m, "======", dealternet(encrypted_text))
        return decrypt(dealternet(encrypted_text), n - 1)
    elif n<= 0:
        return encrypted_text
    elif n== 1:
        # print(m, "######", dealternet(encrypted_text))
        return dealternet(encrypted_text)

'''
 HLM'[E
   n=332
"HL'[E" should equal "L'EHM["
'''

print(encrypt("HLM'[E", 332), "EEE","L'EHM[")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(decrypt("HLM'[E", 332),"DDD", "L'EHM[")
pass
# s eT ashi tist!


print(encrypt("This is a test!", 0), "This is a test!")
print(encrypt("This is a test!", 1), "hsi  etTi sats!")
print(encrypt("This is a test!", 2), "s eT ashi tist!")
print(encrypt("This is a test!", 3), " Tah itse sits!")
print(encrypt("This is a test!", 4), "This is a test!")
print(encrypt("This is a test!", -1), "This is a test!")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(decrypt("hsi  etTi sats!", 1), "This is a test!")
print(decrypt("s eT ashi tist!", 2), "This is a test!")
print(decrypt(" Tah itse sits!", 3), "This is a test!")
print(decrypt("This is a test!", 4), "This is a test!")



'''
# The Best Suloation!

def decrypt(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)

def encrypt(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s



'''

