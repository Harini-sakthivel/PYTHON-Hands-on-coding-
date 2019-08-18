'''


Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

5

'''

n1 = input()
english = set(input().split())
n2 = input()
french = set(input().split())
print(len((english.intersection(french))))
