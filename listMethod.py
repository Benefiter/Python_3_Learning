numbers = [5, 2, 1, 7, 4]

numbers.append(20)
print(numbers)

numbers.insert(0, 22)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers.index(7))

print(20 in numbers)

numbers.sort()
print(f'sorted numbers: {numbers}')

numbers.clear()
print(numbers)

number2 = numbers.copy()
numbers.append(100)
print(number2)

