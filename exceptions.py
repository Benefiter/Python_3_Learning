valid_value_entered = False
while not valid_value_entered:
    try:
        valid_value_entered = True
        age = int(input('Age: '))
        print(age)
    except ValueError:
        print('Invalid value')