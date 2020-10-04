car_started = False
cmd = input('>').lower()
while cmd != 'quit':
    if cmd == 'start' and car_started:
        print("Car is already running!")
    elif cmd == 'start':
        car_started = True
        print('Car started... ready to go!')
    elif cmd == 'stop' and not car_started:
        print('Car is not running!')
    elif cmd == 'stop':
        car_started = False
        print('Car stopped.')
    elif cmd == 'help':
        print('''
        quit: Exit
        stop: Stop the car
        start: start the car
        ''')
    else:
        print("I don't understand that...")
    cmd = input('>').lower()
print('Game ended')