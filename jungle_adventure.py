import time
import random
game_continue2 = False
game_continue = False
secret_path = False
random_number = random.randint(1, 2)
print("Hello, welcome to the game!")
time.sleep(1)
x=input("What is your name? ")
print(f"Nice to meet you, {x}!")
time.sleep(1)
print("Let's start the game!")
time.sleep(1)
print("Your enter a jungle")
time.sleep(1)
print("You see 2 doors labelled 1 and 2")
time.sleep(2)
print("You have to choose one door")
time.sleep(1)
chosen_door = int(input("Which door do you choose? "))
if chosen_door == random_number:
    print("Congratulations! You chose the correct door and survived")
    game_continue = True
else:
    print("You place your foot on the floor only to realise that there is nothing beneath")
    time.sleep(4)
    print("You fall into a pit and your legs twists as you hit the ground")
    time.sleep(4)
    print("You see around you and begin to panic as you can see nothing except darkness")
    time.sleep(4)
    print("Your broken legs also begin to bleed and you feel every single drop of blood leaving your body")
    time.sleep(4)
    print("You scream in hope of help but you can only hear your own voice echoing back at you")
    time.sleep(4)
    print("You slowly bleed out and die in the darkness")
    time.sleep(4)
    print("Game Over!")

if game_continue:
    print("You see a river in front of you")
    time.sleep(2)
    print("You have to choose to swim across or build a raft")
    time.sleep(3)
    choice = input("Do you want to swim or build a raft? (swim/raft) ")
    choice_lower = choice.lower()
    if choice_lower == "swim":
        print("You start swimming across the river")
        time.sleep(4)
        print("You see a crocodile swimming towards you.")
        time.sleep(4)
        print("The crocodile bites off your leg and you slowly begin to bleed")
        time.sleep(4)
        print("You try to keep swimming but it bites off your other leg and you can no longer swim")
        time.sleep(4)
        print("You begin to drown, your consiousness slowly fading as u succumb to the darkness")
        time.sleep(4)
        print("Game Over!")
    elif choice_lower == "raft":
        print("You gather some wood and build a raft")
        time.sleep(2)
        print("You successfully cross the river and continue your adventure!")
        time.sleep(3)
        game_continue2 = True
    elif choice_lower in ("no", "nah", "nothing", "nope", "n", "none"):
        print("Wow!,you don't want to do anything? That's a bold choice")
        time.sleep(2.5)
        print("Lets give you a secret ending")
        time.sleep(1.5)
        secret_path= True
    else:
        print("Invalid choice!")
        time.sleep(2)
        print("Game Over!")

if secret_path:
    print("You find a secret path that leads you to a cave")
    time.sleep(3)
    print("You have to choose to enter the cave or continue walking")
    time.sleep(3)
    choice2 = input("Do you want to enter the cave or continue walking? (enter/continue) ")
    choice2_lower = choice2.lower()
    if choice2_lower == "enter":
        print("You enter the cave and find a treasure chest filled with gold and jewels!")
        time.sleep(4)
        print("Secret ending unlocked!")
    elif choice2_lower == "continue":
        print("You continue walking and eventually get lost in the jungle!")
        time.sleep(3)
        print("Congratulations! You lose the game!")
    else:
        print("Invalid choice!")
        time.sleep(2)
        print("Game Over!")

if game_continue2:
        print("You continue walking and find a village")
        time.sleep(2)
        print("The villagers welcome you and you live happily ever after!")
        time.sleep(2)
        print("Congratulations! You win the game! P.S. There is a secret ending somewhere near the river, try to find it!")
