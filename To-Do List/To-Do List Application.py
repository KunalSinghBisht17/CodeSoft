import json
from datetime import datetime

# Load existing data or initialize an empty list
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        status = "[ ]" if not task['completed'] else "[X]"
        print(f"{index}. {status} {task['description']}")

def add_task():
    description = input("Enter the task description: ")
    task = {'description': description, 'completed': False, 'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def delete_task():
    display_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_completed():
    display_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main menu loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
