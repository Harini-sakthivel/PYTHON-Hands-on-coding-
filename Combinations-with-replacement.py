from itertools import combinations_with_replacement
for i in combinations_with_replacement([1,2,3],2):
    print i


"""
This will give repeated combinantions of numbers

Output:
(1, 1)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(3, 3)
"""