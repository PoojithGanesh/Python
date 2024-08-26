#Find the length of the inreasing sequence 
sequence = [10, 22, 9, 33, 41, 50, 41, 60]
length = 1
max_length = 1
for i in range(1, len(sequence)):
    if sequence[i] > sequence[i-1]:
        length += 1
        max_length = max(max_length, length)
    else:
        length = 1
print(max_length)
