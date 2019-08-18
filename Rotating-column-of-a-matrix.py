m = 4
n = 4
lis = [[1,2,3,3],[4,5,6,4],[7,8,5,9],[1,7,2,4]]
lis2 = []
for i in lis:
    print(i)
for i in range(n):
    lis2.append([])
i = 0
rota = 1
num = rota%n
for j in lis:
    lis[i] = j[n-num:] + j[0:n - num]
    i += 1
for i in lis:
    print(i)

