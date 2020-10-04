list = [1, 5, 7, 8, 3, 22, 6]

largest = list[0]
for item in list:
    if item > largest:
        largest = item
print(f'Largest number in list = {largest}')
