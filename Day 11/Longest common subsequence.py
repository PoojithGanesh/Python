#Find longest subsequence in given two string
def longest_common_subsequence(str1, str2):
    lcs = [x for x in str1 if x in str2]
    if lcs:
        return ''.join(lcs)
    else:
        return "No common subsequence found"

str1 = 'ABC'
str2 = 'ACD'
print("Longest Common Subsequence:", longest_common_subsequence(str1, str2))
