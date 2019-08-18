m = 3
n = 3
lis = [[1,2,3],[4,5,6],[7,8,9]]
lis2 = []
for i in lis:
  print(i)
for i in range(n):
  lis2.append([])
print("The transpose of the matrix is")
for i in range(n):
  for j in range(m):
    lis2[i].append(lis[j][i])
for i in lis2:
  print(i)

