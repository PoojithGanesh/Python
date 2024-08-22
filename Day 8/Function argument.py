'''write a python function take the two strings as an argument and returns how many matches between the strings 
note:A matches is where the two strings char as two same index'''
def count_matches(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count += 1
    return count

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(count_matches(str1, str2))
