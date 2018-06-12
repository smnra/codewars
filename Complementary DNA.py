#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: Complementary DNA.py 
@time: 2018/06/{DAY} 
描述: Complementary DNA
      Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of
      cells and carries the "instructions" for the development and
      functioning of living organisms.

        If you want to know more http://en.wikipedia.org/wiki/DNA

        In DNA strings, symbols "A" and "T" are complements of each
        other, as "C" and "G". You have function with one side of the
        DNA (string, except for Haskell); you need to get the other
        complementary side. DNA strand is never empty or there is
        no DNA at all (again, except for Haskell).

        DNA_strand ("ATTGC") # return "TAACG"

        DNA_strand ("GTAT") # return "CATA"



    Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
    Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
    Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
"""


def DNA_strand(dna):
    tab = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([tab[s] for s in dna])


def DNA_strand2(dna):
    result = list(dna)
    for i,s in enumerate(result):
        if s=='A': result[i] = 'T'
        elif s=='T': result[i] = 'A'
        elif s=='C': result[i] = 'G'
        elif s=='G': result[i] = 'C'
    return "".join(result)


print(DNA_strand("AAAA"),"TTTT","String AAAA is")
print(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
print(DNA_strand("GTAT"),"CATA","String GTAT is")





