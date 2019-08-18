'''
Given an n x n square matrix, find sum of all sub-squares of size k x k where k is smaller than or equal to n.

Examples :

Input:
n = 5, k = 3
arr[][] = { {1, 1, 1, 1, 1},
{2, 2, 2, 2, 2},
{3, 3, 3, 3, 3},
{4, 4, 4, 4, 4},
{5, 5, 5, 5, 5},
};
Output:
18 18 18
27 27 27
36 36 36


Input:
n = 3, k = 2
arr[][] = { {1, 2, 3},
{4, 5, 6},
{7, 8, 9},
};
Output:
12 16
24 28

'''
m = 5
n = 5
ma = 3
lis = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
big = 0
for i in lis:
    print(i)
lis2 = []
for i in range(ma):
    lis2.append([])
for i in range(m-ma+1):
    for j in range(n-ma+1):
        sum = 0
        for k in range(ma):
            for m in range(ma):
                sum += lis[i+k][j+m]
        lis2[i].append(sum)
for i in lis2:
    print(i)