# HackerRank_DataStructures > Arrays > Arrays-DS

from __future__ import print_function
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in reversed(arr):
    print(i, end = " ")
    
    # for item in my_list[::-1]:
    #   print item
    # This is slightly slower than using reversed in Python 2.7.
