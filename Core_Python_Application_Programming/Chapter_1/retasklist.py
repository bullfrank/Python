# -*- coding: utf-8 -*-
"""
Study Regular Expresssion

@author: Sam Fang
"""

import os
import re

def list_task():
    fw = open("task.txt", "w")
    with os.popen("tasklist /nh", "r") as f:
        for eachline in f:
            lists = re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
                                eachline.rstrip())
            for item in lists:
                fw.write(re.sub('[()]', '', str(item)))
                fw.write("\n")
          
    f.close()
    fw.close()
    
list_task()

