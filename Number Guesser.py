import random
num = random.randint(1,100)
running = True
guesses = 1
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while running:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 100:
        print("Invalid guess! Please enter a number between 1 and 100.")
        continue
    elif guess < num:
        print("Too low! Try again.")
        guesses += 1
    elif guess > num:
        print("Too high! Try again.")
        guesses += 1
    else:
        print("Congratulations! You guessed the number!")
        print(f"Number of guesses: {guesses}")
        guesses = 1
        play_again = input("Would you like to quit (press q): ")
        if play_again.lower() == "q":
            running = False

        