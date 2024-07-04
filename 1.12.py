person = {'name': 'Alice', 'age': 30}

# Using get() method to handle missinf keys
city = person.get('city', 'Unknown')
print("city:", city) # Output: Unknow