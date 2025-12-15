# Simple To-Do List Manager
# Phase 1: Basic functionality

def show_menu():
    """Display the menu options to the user"""
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

def view_tasks(tasks):
    """Show all current tasks"""
    if len(tasks) == 0:
        print("\nNo tasks yet! You're all caught up.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("\nWhat task do you want to add? ")
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(tasks):
    """Remove a task from the list"""
    view_tasks(tasks)
    if len(tasks) > 0:
        try:
            task_num = int(input("\nWhich task number do you want to remove? "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")

# Main program starts here
def main():
    tasks = []  # This list will hold all our tasks
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1-4.")

# This runs the program
if __name__ == "__main__":
    main()