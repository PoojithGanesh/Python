#Write a python program to find the minimum number of jumps to reach end of an array(where each element represent the minimum jump length) 
Ex:(1,3,5,8,9,1,6,7,6,8,9)
arr = [1, 3, 5, 8, 9, 1, 6, 7, 6, 8, 9]
jumps, curr_end, curr_farthest = 0, 0, 0
for i in range(len(arr) - 1):
    curr_farthest = max(curr_farthest, i + arr[i])
    if i == curr_end:
        jumps += 1
        curr_end = curr_farthest
print(jumps)  # Output: 3
