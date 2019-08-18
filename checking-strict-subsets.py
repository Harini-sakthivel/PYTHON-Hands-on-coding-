
'''

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78

100 11 12

Sample Output

False


'''

seta = set(input().split())
sub = set(input().split())
if(sub.intersection(seta)== sub and len(seta) > len(sub)):
    print("True")
else:
    print("False")
