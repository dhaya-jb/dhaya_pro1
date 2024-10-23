"""

tasks = []

while True:
    print("1.Add task")
    print("2.Remove task")
    print("3.List task")
    print("4.Quit")

    choice = int(input("Enter Your choice :"))

    if choice == 1:
        task=input("Enter your task :")
        tasks.append(task)
    elif choice == 2:
        task=input("Enter task to remove :")
        if task in tasks:
            tasks.remove(task)
        else:
            print("task not found.")
    elif choice == 3:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif choice == 4:
        break

    else:
        print("Invalid Option.")

"""


tasks = []

def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Quit")

while True:
    display_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"'{task}' has been added to your task list.")
    
    elif choice == 2:
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"'{task}' has been removed from your task list.")
        else:
            print(f"'{task}' not found in the task list.")

    elif choice == 3:
        if tasks:
            print("\n--- Task List ---")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")
    
    elif choice == 4:
        print("Exiting the task manager. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number between 1 and 4.")
