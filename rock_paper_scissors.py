import random
def check_win(opponent,player):
    win = False
    if opponent == "Rock" and player == "p":
        win = True
    if opponent == "Paper" and player == "s":
        win = True
    if opponent == "Scissors" and player == "r":
        win = True
    return win
def select_random(list):
    random_index = random.randint(0,len(list)-1)
    return list[random_index]
choices = ['Rock','Paper','Scissors'] 
streak = 0
is_running = True
print('------------------------------------')
print('Welcome to Rock-Paper-Scissors')
print('------------------------------------')
while is_running:
    bot_choice = select_random(choices)
    temp_input = input('Enter your choice(R/P/S): ')
    print('------------------------------------')
    player_choice = temp_input.lower()

    won = check_win(bot_choice,player_choice)
    print(f'Computer chose {bot_choice}')
    
    if won:
        print('------------------------------------')
        print("You win!")
        print('------------------------------------')
        streak += 1
    else:
        print('------------------------------------')
        print("You lose!")
        print('------------------------------------')
        streak = 0

    print(f'Streak: {streak}') 
    print('------------------------------------')
    quit = input('Would you like to quit?(q to quit): ')
    print('------------------------------------')
    if quit.lower() == 'q':
        is_running = False

print('------------------------------------')
print(f'Final winning streak: {streak}')
print('------------------------------------')
print('Good Game' if streak>=5 else 'Get good buddy')
print('------------------------------------')

