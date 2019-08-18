m = 4
n = 4
lis = [[1,2,3,3],[4,5,6,4],[7,8,5,9],[1,7,2,4]]
lis2 = []
for i in lis:
  print(i)
for i in range(n):
  lis2.append([])
res = 0
i = 0
j = 0
while(i < m and j < n):
  res += lis[i][j]
  i += 1
  j += 1
print("The sum of left diagonal elements is {}".format(res))
i = m-1
j = 0
resu = 0
while(i >= 0 and j < n):
  resu += lis[i][j]
  i -= 1
  j += 1
print("The sum of right diagonal elements is {}".format(resu))
