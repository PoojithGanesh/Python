#Find difference between sum of the squares of frst 200 natural numbers and squares of the sum
print(sum(range(1, 201))**2 - sum(i**2 for i in range(1, 201)))
