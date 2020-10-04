def find_max(numbers_list):
    max = numbers_list[0]
    for number in numbers_list:
        if number > max:
            max = number
    return max