secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess:"))
    if guess == secret_number:
        print("You guessed correctly!")
        break
    guess_count += 1
else:
    print('You have exceeded the max. number of guesses')