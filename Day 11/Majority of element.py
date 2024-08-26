#Find majority of element in array that appear (n/2) times
nums = [2,2,1,1,2,2,2]
print(max(set(nums), key=nums.count))  # Output: 2
