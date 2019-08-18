'''

Input

ABCDCDC
CDC

Output

2


'''
string = input()
sub_string = input()
count = 0
for j in range(len(string)):
    if string[j:j + len(sub_string)] == sub_string:
        count += 1
print(count)
