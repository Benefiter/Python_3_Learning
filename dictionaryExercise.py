numbers_dictionary = {
    "1": "one", 
    "2": "two",
    "3": "three",
    "4": "four",
}

phone_number = input('Phone: ')

word_phone_number = ''
for item in phone_number:
    word_phone_number += numbers_dictionary[item] + ' '
print(word_phone_number)
