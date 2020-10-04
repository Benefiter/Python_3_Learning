numbers = [1, 2, 3, 4, 5, 1, 3, 2]
unique_numbers = []

for item in numbers:
    if item not in unique_numbers:
        unique_numbers.append(item)

print(f'unique list = {unique_numbers}')