# -*- coding: utf-8 -*-
"""
Study Regular Expression functions named group and groups

@author: Song
"""

import re

"""
 在正则表达式中, ()表示一个正则表达式子组.
 如果正则表达式中有n个子组,
 1.对match函数返回值调用groups(),可以获取一个包含n个匹配子组的元组(tuple).
 2.对match函数返回值调用group(),可以在group()中传入参数index(1<=index<=n),这样可以
   获取每一个匹配的子组
"""
def how_to_use_group_and_groups():
    pattern = "(\w{3})-(\d{3})"
    str = "xyz-123"

    print("==== groups====")    
    print(re.match(pattern, str).groups())
    match_array = re.match(pattern, str).groups()
    for sub_array in match_array:
        print(sub_array)
    
    print("==== group====")
    m = re.match(pattern, str)
    print(m.group(1))
    print(m.group(2))
    

how_to_use_group_and_groups()