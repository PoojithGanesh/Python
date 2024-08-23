#Find the frequency of each character in the given string and replace the each character in the string using alphabet which the distance is equal to frequency
from collections import Counter
s='hello world'
new_string=''.join(chr(((ord(char)-ord('a')+Counter(s)[char.lower()])%26)+ ord('a')) if char.isalpha() else char for char in s)
print(new_string)
