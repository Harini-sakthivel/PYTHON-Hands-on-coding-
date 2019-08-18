from itertools import permutations
from itertools import combinations
for i,j,k in (permutations([1,2,3])):
    print("{},{},{}".format(i,j,k))
for i,j in (combinations([1,2,3],2)):
    print("{},{}".format(i,j))

'''
Output:
permutations

1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1

combinations

1,2
1,3
2,3
'''