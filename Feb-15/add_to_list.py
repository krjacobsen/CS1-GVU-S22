# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:06:42 2022

@author: mrobbins
"""

def add_to_list(value, items):
    """ add value to items if it is not already there """
    if value not in items:
        items += [value]

def main():
    list1 = [8, 5, 3, 6, 4, 9, 7]
    target1 = 3
    target2 = 1203
    
    add_to_list(target2, list1)
    
    print(list1)

main()