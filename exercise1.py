is_quit = False
is_started = False
is_stopped = True

while not is_quit:
    command = input("> ").lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game    
    ''')
    elif command == 'start':
        if is_started:
            print('Car already started!')
        else:
            print('Car started!')
            is_started = True
            is_stopped = False
    elif command == "stop":
        if is_stopped:
            print('The car is already stopped!')
        else:
            print('Car stopped!')
            is_started = False
            is_stopped = True
    elif command == 'quit':
        is_quit = True
    else:
        print("I don't understand!")