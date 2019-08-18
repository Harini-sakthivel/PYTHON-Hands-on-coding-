'''

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).


str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).


str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

'''

stri = input()
print(any(str.isalnum() for str in stri))
print(any(str.isalpha() for str in stri))
print(any(str.isdigit() for str in stri))
print(any(str.islower() for str in stri))
print(any(str.isupper() for str in stri))
