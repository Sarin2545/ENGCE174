n = int(input("INPUT NUMBER : "))
def print_row(row, max_row):
    if row < max_row:
        print('* ' * (row + 1))
        print_row(row + 1, max_row)

def print_reverse_row(row):
    if row > 0:
        print('* ' * row)
        print_reverse_row(row - 1)

def print_right_aligned_row(row, max_row):
    if row <= max_row:
        print(' ' * (max_row - row) + '* ' * row)
        print_right_aligned_row(row + 1, max_row)

def print_left_aligned_row(row, max_row):
    if row <= max_row:
        print(' ' * row + '* ' * (max_row - row))
        print_left_aligned_row(row + 1, max_row)

def print_pyramid_row(row, max_row):
    if row <= max_row:
        print('  ' * (max_row - row) + '* ' * row)
        print_pyramid_row(row + 1, max_row)

print_row(0, n)
print("------------------------------------")
print_reverse_row(n)
print("------------------------------------")
print_right_aligned_row(1, n)
print("------------------------------------")
print_left_aligned_row(0, n)
print("------------------------------------")
print_pyramid_row(1, n)
print("------------------------------------")