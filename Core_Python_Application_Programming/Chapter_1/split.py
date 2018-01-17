# -*- coding: utf-8 -*-
"""
Study Regular Expression functions named split

@author: Sam Fang
"""

import re

def how_to_use_split():
    DATA = ('Mountain View, CA 94040',
            'Sunnyvale, CA doweewe',
            'Los Altos, 94023 XAX',
            'Cupertino, 95014',
            'Palo Alto, CA'
            )
    
    """
     (?:pattern) 表示匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不
     进行存储供以后使用。这在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。
     例如， 'industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式。
     模式 (?:\d{5}|[A-Z]{2}) 代表的含义是匹配:空格后面跟5个数字或者空格后面跟2个大
     写字母
    """
    for datum in DATA:
        print(re.split(", |(?= (?:\d{5}|[A-Z]{2})) ", datum))
        #print(re.search(" (?=\d{5}|[A-Z]{2}) ", datum))
        #print(re.search("([A-Z]{2})|(\d{5})", datum).groups())
        #print(re.split("[A-Z]{2}", datum))
        # print(re.split(", ", datum))

how_to_use_split()