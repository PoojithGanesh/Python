Sen="Welcome to SIMATS"
vowels=sum(1 for c in sen if c in "aeiouAEIOU")
consonents=sum(1 for c in sen if c.isalpha() and c not in "aeiouAEIOU")
print("No. of vowels:", vowels)
print("No. of cosonents:", consonents)
