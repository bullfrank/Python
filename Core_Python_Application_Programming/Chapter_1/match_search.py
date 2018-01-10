# -*- coding: utf-8 -*-
"""
Study Regular Expression functions named match and search


@author: Sam Fang
"""

import re

"""
 1.match函数只能从字符串的起始位置进行匹配正则表达式中代表的字符串.如果正则表达式匹配的
   子串在字符串的除开头以外的其他位置，则match返回None,无法匹配
 2.search函数可以从字符串的任意位置开始查找正则表达式中代表的字符串
"""
def how_to_use_match():
    str1 = "food"
    str2 = "This is food"
    str3 = "seafood"
    str4 = "food is good"
    patt1 = "foo"
    patt2 = "food"
    patt3 = "fo*d"
    patt4 = "fo?d"

    print("==== how to use match ===")
    print("Patten 1")
    print(re.match(patt1, str1).group())
    #print(re.match(patt1, str2).group())  # AttributeError
    #print(re.match(patt1, str3).group())  # AttributeError
    print(re.match(patt1, str4).group())
    
    print("\nPatten 2")
    print(re.match(patt2, str1).group())
    print(re.match(patt2, str4).group())
    
    print("\nPatten 3")
    print(re.match(patt3, str1).group())
    print(re.match(patt3, str4).group())
    
    print("\nPatten 4")
    #print(re.match(patt4, str1).group())  # AttributeError
    print(re.match(patt4, "fd").group())
    print(re.match(patt4, "fod").group())
    
    print("\nPatten 5")
    print(re.match("find|found", "foundation").group())
    
    print("\nPatten 6")
    print(re.match("f\w+d", str1).group())

how_to_use_match()

def how_to_use_search():
    str = "find a foundation"
    patt1 = "found"
    patt2 = "f\w+d"
    patt3 = "fo*d"
    
    print("\n==== how to use search ===")
    print(re.search(patt1, str).group())
    print(re.search(patt2, str).group())
    #print(re.search(patt3, str).group()) # AttributeError

how_to_use_search()

    
