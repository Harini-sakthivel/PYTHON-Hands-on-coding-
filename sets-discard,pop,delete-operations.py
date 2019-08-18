'''
.remove(x)

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0



.discard(x)

>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])

.pop()

>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set

input:

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

op

{2, 3, 4, 5, 6, 7, 8, 9}
{2, 3, 4, 5, 6, 7, 8}
{2, 3, 4, 5, 6, 7, 8}
{2, 3, 4, 5, 6, 7}
{2, 3, 4, 5, 6}
{3, 4, 5, 6}
{3, 4, 5}
{3, 4}
{4}

4

'''

n = int(input())
s = set(map(int, input().split()))
methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}
for _ in range(int(input())):
    method, *args = input().split()
    methods[method](*map(int,args))
print(sum(s))
print(s)