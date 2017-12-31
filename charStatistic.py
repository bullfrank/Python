# -*- coding: utf-8 -*-
"""
Use dictionary to count the amount of each character in a sentence

@author: Song
"""

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def initDictionary():
    dict = {}
    for key in keys:
        dict.setdefault(key, 0)
    return dict

def countCharAmout(sentence, dict):
    sentence = sentence.lower()
    sentence = sentence.replace(' ', '')
    length = len(sentence)
    i = 0
    while length > 0:
        key = sentence[i]
        dict[key] += 1
        length -= 1
        i += 1
    
#sentence = "This is a test"
sentence = "THIS IS A TEST"
dict = initDictionary()
countCharAmout(sentence, dict)

print("result: %s"% dict.items())
        

