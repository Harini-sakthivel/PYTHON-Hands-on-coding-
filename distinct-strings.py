"""

Input Format

The first line contains an integer
the total number of country stamps.
The next

lines contains the name of the country where the stamp is from.

Constraints

Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France

Sample Output

5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set()
for _ in range(0,int(input())):
    s.add(input())
print(len(s))