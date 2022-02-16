# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:30:52 2022

@author: mrobbins
"""

def odds(items):
    # Add all odd numbers to a list
    result = []
    for item in items:
        if item % 2 == 1:
            result += [item]
            
    return result
            
    
def main():
    all_items = list(range(1,10))
    print(all_items)
    
    odd_items = odds(all_items)
    
    print(odd_items)
    print(odds(all_items))

main()



