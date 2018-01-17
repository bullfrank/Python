# -*- coding: utf-8 -*-
"""
Study Regular Expression functions named findall

@author: Sam Fang
"""

import re

def how_to_use_findall():
    s = "This or that"
    """
    ()表示匹配封闭的正则表达式.注意用上这个符号和不用,得到的结果不一样
    """
    g = re.findall("th\w+ or th\w+", s, re.I)
    print(g) # result is: ["This or that"]
    
    g = re.findall("(th\w+) or (th\w+)", s, re.I)
    print(g) # result is: ['This', 'that']
    
how_to_use_findall()
    