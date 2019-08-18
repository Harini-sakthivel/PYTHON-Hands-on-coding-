
"""
The first line of input contains an integer,
.
The second line contains space-separated integers.
The third line contains an integer, .
The fourth line contains

space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12

Sample Output

5
9
11
12
"""
if __name__ == "__main__":
    a = int(input())
    b = input().split()
    c = int(input())
    d = input().split()
    x = set(b)
    y = set(d)
    p = y.difference(x)
    q = x.difference(y)
    r = p.union(q)
    print("The symmetrial differene is ")
    print('\n'.join(sorted(r, key=int)))


