m = 4
n = 4
ma = 2
lis = [[1,2,3,3],[4,2,3,4],[7,3,8,8],[1,7,8,8]]
big = 0
for i in lis:
    print(i)
for i in range(m-ma+1):
    for j in range(n-ma+1):
        sum = 0
        for k in range(ma):
            for m in range(ma):
                sum += lis[i+k][j+m]
                if(sum > big):
                    big = sum
                    it = i
                    jt = j
print(big)
print(it,jt)

'''

Output

[1, 2, 3, 3]
[4, 2, 3, 4]
[7, 3, 8, 8]
[1, 7, 8, 8]
32
(2, 2)

'''