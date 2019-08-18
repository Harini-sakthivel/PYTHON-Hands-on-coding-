'''

Input Format

The first line contains two space-separated integers
and , the size of and the number of left rotations you must perform.
The second line contains space-separated integers


Output Format

Print a single line of
space-separated integers denoting the final state of the array after performing
left rotations.


Sample Input

5 4
1 2 3 4 5


Sample Output

5 1 2 3 4

'''

def rotLeft(a, num):
    length = len(a)
    b = []
    if(num > length):
        num = num % length
    b = a[num:length] + a[0:num]
    return b



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))
