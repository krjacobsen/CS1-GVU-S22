# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:48:03 2022

@author: mrobbins
"""

def find(target, items):
    """Return the first index of target in items, or -1."""
    for i in range(len(items)):
        if target == items[i]:
            return i
    
    return -1

def find_easy(target, items):
    if target in items:
        print("YAY!")
    else:
        print("BOO!")
    
    
def main():
    list1 = [8, 5, 3, 6, 4, 9, 7]
    target1 = 3
    target2 = 1203
    
    #result_index = find(target1, list1)
    
    #print(result_index)

    #print(find(target2, list1))

    find_easy(target1, list1)
    find_easy(target2, list1)


