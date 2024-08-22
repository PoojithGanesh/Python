#Take the array as an input and array should have only repeated element find that repeated elements.
array = list(map(int, input("Enter the array elements (space separated): ").split()))
repeated_elements = [element for element in set(array) if array.count(element) > 1]
print("Repeated elements: ", repeated_elements)
