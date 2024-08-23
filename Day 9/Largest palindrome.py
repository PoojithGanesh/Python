#Find largest palindrome made from the product of two four digit numbers.
print(max(i*j for i in range(9999, 9000, -1) for j in range(i, 9000, -1) if str(i*j) == str(i*j)[::-1]))
