is_running = True

print("Welcome to Calculator")
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for mutiplication")
print("Enter 4 for division")

while is_running:
    choice = None
    try:
        choice = int(input("What operation would you like to do?: "))
    except ValueError:
        pass
        
    if choice == 1:
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Answer is {x+y}")
        except:
            print("Error")
    elif choice == 2:
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Answer is {x-y}")
        except:
            print("Error")
    elif choice == 3:
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Answer is {x*y}")
        except:
            print("Error")
    elif choice == 4:
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            print(f"Answer is {x/y}")
        except:
            print("Error")
    else:
        print("Invaild choice")

    rerun = input("Would you like to rerun the program? (Q to quit): ")
    if rerun.lower() == "q":
        is_running = False