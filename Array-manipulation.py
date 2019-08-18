'''
The first line contains two space-separated integers n and m,n the size of the array and m the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be  100 100 0   0   0.
After the second update list will be 100 200 100 100 100.
After the third update list will be  100 200 200 200 100.

The required answer will be 200
'''

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    listi = [0]*(n+1)
    for _ in range(m):
        a,b,add = map(int,input().split())
        listi[a-1] += add
        if(b-1 < n-1):
            listi[b] -= add
    each = 0
    maxi = 0
    for i in listi:
        each += i
        if(each > maxi):
            maxi = each
    print(maxi)