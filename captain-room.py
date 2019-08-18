'''

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of k
members per group where ≠

.
The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear k

times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of

and the room number list.

Input Format

The first line consists of an integer,
, the size of each group.
The second line contains the unordered elements of the room number list.


Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output

8


'''
d=input();  #get rid of first line
a=input().split();  #store all to array
s1=set();  #all unique room number
s2=set();  #all unique room number occur more than once
for i in a:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3 = s1.difference(s2)
print(s3.pop())
