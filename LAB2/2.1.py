input = int(input("INPUT NUMBER : ")) 
print("--------------------------")
for i in range(1, input+1): 
    print('* ' * i) 
print("--------------------------")
for i in range(input, 0, -1): 
    print('* ' * i) 
print("--------------------------")
for i in range(1, input+1): 
    print(' ' * (input - i) + ' *' * i) 
print("--------------------------")
for i in range(input, 0, -1): 
    print(' ' * (input - i) + ' *' * i) 
print("--------------------------")
for i in range(1, input+1):
    print('  ' * (input - i) + '* ' * i) 
print("--------------------------")