# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:53:20 2017

@author: Sam Fang
"""

# The example of how to use * for variable parameter function. 
# The type of parameter after *: 
#  1. Several necessary parameters without keyword
#  2. List or tuple
def personalInfo(name, *varParam):
    print("Name: ", name)
    for var in varParam:
        print("Address: ", var)
    return

personalInfo("Sam", "Shanghai", "Guizhou")

# the result is different if there is a * before list or not
list = ["Shanghai", "Guizhou"]
personalInfo("Sam", list)
personalInfo("Sam", *list)

# the result is different if there is a * before tuple or not
tuple = ("Shanghai", "Guizhou")
personalInfo("Sam", tuple)
personalInfo("Sam", *tuple)

# The example of howto use ** for variable parameter function
# The type of parameter after ** only can be dictionary (mapping)
def personalInfo(name, **varDict):
    print("Name: ", name, "Address: ", varDict)
    for key in varDict:
        print("Address: ", varDict.get(key))
    return

info = {'1':"Shanghai", '2':"Guizhou"}
personalInfo("Sam", **info)
