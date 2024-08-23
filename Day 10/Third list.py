'''Take two lists as input create a third list with appending 1st element of 1st list and 1st element of 2nd list and so on.. if the length of
lists not same the remaining elements append to last'''
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c','d','e','f','g']

result = [val for pair in zip(list1, list2) for val in pair] + list1[len(list2):] + list2[len(list1):]
print(result)
