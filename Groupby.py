'''
Given input as

Input:
bbbbaaaaaaacc

To find which occurs continuosly manytimes

Ouput:
a : 7

'''
from itertools import groupby
a = 'bbbbaaaaaaacc'
big = 0
for i,j in groupby(a):
    length = len(list(j))
    if(length > big):
        big = length
        ans = i
print("{} is the highest continuosly occuring character of {} times".format(ans,big))