import random

print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100. Can you guess it?")

num = random.randint(1, 100)
guesses = 1
running = True

while running:
    user_input = input("Enter your guess: ").strip()

    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    if guess < 1 or guess > 100:
        print("Out of range! Please enter a number between 1 and 100.")
        continue

    if guess < num:
        print("Too low! Try again.")
        guesses += 1
    elif guess > num:
        print("Too high! Try again.")
        guesses += 1
    else:
        print(f"Congratulations! You guessed the number in {guesses} guesses!")
        
        play_again = input("\nPress 'q' to quit, or any other key to play again: ").strip().lower()
        if play_again == "q":
            print("Thanks for playing!")
            running = False
        else:
            num = random.randint(1, 100)
            guesses = 1
            print("\nNew round started! Guess a number between 1 and 100.")

        
