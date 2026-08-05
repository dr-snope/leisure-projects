task_list=[]
task = 0
remove_task = ""
while True:
    print("----------------------------------------")
    print("           Simple To-Do List            ")
    print("----------------------------------------")
    print("                  Menu                  ")
    print("----------------------------------------")
    print("1. Add tasks")
    print("2. Check tasks")
    print("----------------------------------------")
    choice = int(input("Select your desired operation number: "))
    if choice not in [1,2]:
        print("----------------------------------------")
        print("Invaild operation")
        print("Returning back...")
    if choice == 1:
        task_number = int(input("Enter number of tasks you want to enter: "))
        for i in range (task_number):
            task = input("Enter your task (Enter to quit): ")
            task_list.append(task)
        print("----------------------------------------")
        print("Tasks added! Returning back...")
    if choice == 2:
        for i in range (len(task_list)):
            x = task_list[i].capitalize()
            print(f"{i+1}. {x}")
        print("----------------------------------------")
        operation  = input("Do you want to check any tasks? (Yes/No): ")
        if operation.lower() != "yes":
            print("----------------------------------------")
            print("Ok, returning back...")
        if operation.lower() == "yes":
            while remove_task != 0:
                remove_task = int(input("Enter task number to mark it done (0 to quit): "))
                if remove_task != 0:
                    del task_list[remove_task - 1]
                    print("Task checked!")
            remove_task = ""
            print("----------------------------------------")
            print("Changes Saved! Returning back...")