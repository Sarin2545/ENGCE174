# Dictionary comprehension to create a dictionary of squares
number = [1, 2, 3, 4, 5]
square_dict = {num: num**2 for num in number}
print("Dictionary of squares:", square_dict)

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}