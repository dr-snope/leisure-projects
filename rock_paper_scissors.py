import random

RULES = {
    'r': {'name': 'Rock', 'beats': 'Scissors'},
    'p': {'name': 'Paper', 'beats': 'Rock'},
    's': {'name': 'Scissors', 'beats': 'Paper'}
}

streak = 0
is_running = True

print('------------------------------------')
print('Welcome to Rock-Paper-Scissors')
print('------------------------------------')

while is_running:
    bot_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    
    user_input = input('Enter your choice (R/P/S): ').strip().lower()
    print('------------------------------------')

    if user_input not in RULES:
        print("Invalid choice! Please enter 'r', 'p', or 's'.")
        print('------------------------------------')
        continue

    player_name = RULES[user_input]['name']
    print(f'You chose: {player_name}')
    print(f'Computer chose: {bot_choice}')
    print('------------------------------------')

    if player_name == bot_choice:
        print("It's a tie!")
    elif RULES[user_input]['beats'] == bot_choice:
        print("You win!")
        streak += 1
    else:
        print("You lose!")
        streak = 0

    print('------------------------------------')
    print(f'Current Streak: {streak}')
    print('------------------------------------')

    play_again = input('Would you like to quit? (q to quit): ').strip().lower()
    print('------------------------------------')
    if play_again == 'q':
        is_running = False

print(f'Final winning streak: {streak}')
print('------------------------------------')
print('Good Game' if streak >= 5 else 'Get good buddy')
print('------------------------------------')


