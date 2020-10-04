weight = input("Weight: ")
l_or_k = input("(L)bs or (K)g: ").lower()

if l_or_k == 'l':
    print(f'You are {weight} pounds.')
elif l_or_k == 'k':
    print(f'You are {weight} Kilograms.')
else:
    print("Unknown conversion")
