tasks = []

def add_task():
    title = input("Enter task title: ")
    desc = input("Enter description: ")
    
    task = {
        "title": title,
        "description": desc,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks found!\n")    
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['title']} - {task['description']} [{status}]")
    print()


def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!\n")
    except:
        print("Invalid input!\n")


def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        tasks[num - 1]["completed"] = True
        print("Task marked as completed!\n")
    except:
        print("Invalid input!\n")


def menu():
    while True:
        print("===== Task Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

menu()
