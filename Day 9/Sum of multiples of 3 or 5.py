#Write a python program to compute sum of all the multiples of 3 or 5 below 500.
print("The sum of all the multiples of 3 or 5 below 500 is:", sum(i for i in range(500) if i % 3 == 0 or i % 5 == 0))
