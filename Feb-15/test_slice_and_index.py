# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:03:05 2022

@author: mrobbins
"""

def main():
    data = [10,20,30,40,50]
    
    print(data[0])
    
    by_sevens = list(range(0,100,7))
    # [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
    print(by_sevens)
    
    print(by_sevens[2:7])
    print(by_sevens[-3])
    
    print(by_sevens[1:2])
    
   
    
main()