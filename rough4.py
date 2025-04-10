import json
import os

# Function to load the to-do list from the JSON file
def load_tasks(filename="todo.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []

# Function to save the to-do list to the JSON file
def save_tasks(tasks, filename="todo.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else: 
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(tasks, task):
    tasks.append(task)    
    print(f"Task '{task}' added!")

# Function to remove a task
def remove_task(tasks, task_index):
    try:
        task = tasks.pop(task_index - 1)
        print(f"Task '{task}' removed!")
    except IndexError:
        print("Invalid task number.")

# Main program
def main():
    filename = "todo.json"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
                
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            add_task(tasks, new_task)
            save_tasks(tasks, filename)
        elif choice == "3":
            display_tasks(tasks)
            task_num = input("Enter the task number to remove: ").strip()
            if task_num.isdigit():
                remove_task(tasks, int(task_num))
                save_tasks(tasks, filename)
            else:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
