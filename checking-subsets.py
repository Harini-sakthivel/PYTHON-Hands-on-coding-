'''

Sample Input

set a

1 2 3 5 6

set b

9 8 5 6 3 2 1 4 7

Sample Output

True

'''

seta = set(map(int,input().split()))
setb = set(map(int,input().split()))
if(seta == seta.intersection(setb)):
    print("True")
else:
    print("False")
