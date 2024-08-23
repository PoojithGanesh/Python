#Get the string as input insert cap(^) if vowel found after the capital if not insert @ symbol
print(''.join(c + '^' if c in 'aeiouAEIOU' else c + '@' for c in input("Enter the string:")))
